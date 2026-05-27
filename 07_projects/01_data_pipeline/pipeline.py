# ============================================================
# Mini-Project: Data Pipeline
# Fetch → Clean → Store → Report
# ============================================================
# pip install requests pandas
# ============================================================

import requests
import sqlite3
import json
from datetime import datetime

# Optional pandas
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False
    print("Note: pandas not installed — using raw dicts")


# ─────────────────────────────────────────────
# STEP 1: FETCH
# ─────────────────────────────────────────────

def fetch_users() -> list[dict]:
    """Fetch user records from JSONPlaceholder API."""
    print("📡 Fetching users...")
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
        r.raise_for_status()
        users = r.json()
        print(f"   ✅ Fetched {len(users)} users")
        return users
    except requests.RequestException as e:
        print(f"   ❌ Fetch failed: {e}")
        return []

def fetch_posts() -> list[dict]:
    """Fetch post records."""
    print("📡 Fetching posts...")
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
        r.raise_for_status()
        posts = r.json()
        print(f"   ✅ Fetched {len(posts)} posts")
        return posts
    except requests.RequestException as e:
        print(f"   ❌ Fetch failed: {e}")
        return []


# ─────────────────────────────────────────────
# STEP 2: CLEAN & TRANSFORM
# ─────────────────────────────────────────────

def clean_users(users: list[dict]) -> list[dict]:
    """Flatten and clean user records."""
    print("\n🔧 Cleaning users...")
    cleaned = []
    for u in users:
        cleaned.append({
            "id":       u["id"],
            "name":     u["name"].strip(),
            "email":    u["email"].lower().strip(),
            "username": u["username"],
            "city":     u["address"]["city"],
            "company":  u["company"]["name"],
            "website":  u["website"] if u["website"].startswith("http") else f"https://{u['website']}"
        })
    print(f"   ✅ Cleaned {len(cleaned)} users")
    return cleaned

def enrich_posts(posts: list[dict], users: list[dict]) -> list[dict]:
    """Add author name to each post."""
    user_map = {u["id"]: u["name"] for u in users}
    for post in posts:
        post["author"] = user_map.get(post["userId"], "Unknown")
        post["word_count"] = len(post["body"].split())
    return posts


# ─────────────────────────────────────────────
# STEP 3: STORE
# ─────────────────────────────────────────────

def init_db(conn: sqlite3.Connection):
    conn.executescript("""
        DROP TABLE IF EXISTS posts;
        DROP TABLE IF EXISTS users;

        CREATE TABLE users (
            id       INTEGER PRIMARY KEY,
            name     TEXT,
            email    TEXT,
            username TEXT,
            city     TEXT,
            company  TEXT,
            website  TEXT
        );

        CREATE TABLE posts (
            id         INTEGER PRIMARY KEY,
            user_id    INTEGER,
            author     TEXT,
            title      TEXT,
            body       TEXT,
            word_count INTEGER
        );
    """)
    conn.commit()
    print("\n💾 Database initialised")

def store_users(conn: sqlite3.Connection, users: list[dict]):
    conn.executemany(
        "INSERT INTO users VALUES (:id,:name,:email,:username,:city,:company,:website)",
        users
    )
    conn.commit()
    print(f"   ✅ Stored {len(users)} users")

def store_posts(conn: sqlite3.Connection, posts: list[dict]):
    conn.executemany(
        "INSERT INTO posts (id,user_id,author,title,body,word_count) "
        "VALUES (:id,:userId,:author,:title,:body,:word_count)",
        posts
    )
    conn.commit()
    print(f"   ✅ Stored {len(posts)} posts")


# ─────────────────────────────────────────────
# STEP 4: REPORT
# ─────────────────────────────────────────────

def generate_report(conn: sqlite3.Connection):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    print("\n" + "=" * 55)
    print("📊  PIPELINE REPORT")
    print("=" * 55)

    c.execute("SELECT COUNT(*) AS n FROM users")
    print(f"Total users : {c.fetchone()['n']}")

    c.execute("SELECT COUNT(*) AS n FROM posts")
    print(f"Total posts : {c.fetchone()['n']}")

    c.execute("""
        SELECT author, COUNT(*) AS posts, AVG(word_count) AS avg_words
        FROM   posts GROUP BY author ORDER BY posts DESC LIMIT 5
    """)
    print("\n── Top 5 authors by post count ──")
    for row in c.fetchall():
        print(f"  {row['author']:<25} posts={row['posts']}  avg_words={row['avg_words']:.0f}")

    c.execute("SELECT city, COUNT(*) AS n FROM users GROUP BY city ORDER BY n DESC")
    print("\n── Users by city ──")
    for row in c.fetchall():
        print(f"  {row['city']:<20} {row['n']}")

    print("\n" + "=" * 55)
    print(f"✅  Pipeline completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def run_pipeline():
    # Fetch
    users = fetch_users()
    posts = fetch_posts()
    if not users or not posts:
        print("Aborting — fetch failed.")
        return

    # Clean
    clean = clean_users(users)
    enriched = enrich_posts(posts, clean)

    # Store
    conn = sqlite3.connect("pipeline_output.db")
    init_db(conn)
    store_users(conn, clean)
    store_posts(conn, enriched)

    # Report
    generate_report(conn)
    conn.close()

if __name__ == "__main__":
    run_pipeline()
