# ============================================================
# Capstone — Storage Layer
# SQLite persistence with full error handling
# ============================================================

import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class Database:
    """Context-manager-aware SQLite wrapper."""

    def __init__(self, path: str):
        self.path = path
        self.conn: sqlite3.Connection | None = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
            logger.error(f"DB transaction rolled back due to: {exc_val}")
        self.close()
        return False   # don't suppress exceptions

    def connect(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        logger.debug(f"Connected to {self.path}")

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def commit(self):
        if self.conn:
            self.conn.commit()

    def rollback(self):
        if self.conn:
            self.conn.rollback()

    def init_schema(self):
        """Create tables if they don't exist."""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY,
                name     TEXT NOT NULL,
                email    TEXT UNIQUE NOT NULL,
                username TEXT,
                city     TEXT,
                company  TEXT
            );

            CREATE TABLE IF NOT EXISTS posts (
                id         INTEGER PRIMARY KEY,
                user_id    INTEGER NOT NULL,
                author     TEXT,
                title      TEXT,
                body       TEXT,
                word_count INTEGER,
                char_count INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS user_stats (
                user_id    INTEGER PRIMARY KEY,
                name       TEXT,
                post_count INTEGER,
                avg_words  REAL,
                total_chars INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE INDEX IF NOT EXISTS idx_posts_user ON posts(user_id);
        """)
        self.conn.commit()
        logger.info("Schema initialised")

    def upsert_users(self, users: list[dict]) -> int:
        """Insert or replace user records."""
        if not users:
            return 0
        try:
            self.conn.executemany(
                "INSERT OR REPLACE INTO users (id,name,email,username,city,company) "
                "VALUES (:id,:name,:email,:username,:city,:company)",
                users
            )
            self.conn.commit()
            logger.info(f"Upserted {len(users)} users")
            return len(users)
        except sqlite3.Error as e:
            self.rollback()
            logger.error(f"Failed to upsert users: {e}")
            raise

    def upsert_posts(self, posts: list[dict]) -> int:
        if not posts:
            return 0
        try:
            self.conn.executemany(
                "INSERT OR REPLACE INTO posts "
                "(id,user_id,author,title,body,word_count,char_count) "
                "VALUES (:id,:user_id,:author,:title,:body,:word_count,:char_count)",
                posts
            )
            self.conn.commit()
            logger.info(f"Upserted {len(posts)} posts")
            return len(posts)
        except sqlite3.Error as e:
            self.rollback()
            logger.error(f"Failed to upsert posts: {e}")
            raise

    def upsert_stats(self, stats: list[dict]) -> int:
        if not stats:
            return 0
        self.conn.executemany(
            "INSERT OR REPLACE INTO user_stats "
            "(user_id,name,post_count,avg_words,total_chars) "
            "VALUES (:user_id,:name,:post_count,:avg_words,:total_chars)",
            stats
        )
        self.conn.commit()
        return len(stats)

    def query(self, sql: str, params=()) -> list[sqlite3.Row]:
        c = self.conn.cursor()
        c.execute(sql, params)
        return c.fetchall()

    def count(self, table: str) -> int:
        row = self.query(f"SELECT COUNT(*) AS n FROM {table}")
        return row[0]["n"] if row else 0
