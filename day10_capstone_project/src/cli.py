# ============================================================
# Capstone — CLI Entry Point
# Usage: python -m src.cli [command]
# ============================================================

import sys
import logging
import asyncio
from datetime import datetime

# ── Logging setup ─────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("cli")

# ── Local imports ─────────────────────────────
sys.path.insert(0, str(__file__ + "/../../"))
from src.fetcher     import fetch_json, fetch_all_async
from src.transformer import transform_users, transform_posts, compute_user_stats
from src.storage     import Database

DB_PATH = "data/capstone.db"

ENDPOINTS = {
    "users": "https://jsonplaceholder.typicode.com/users",
    "posts": "https://jsonplaceholder.typicode.com/posts",
}


def cmd_run():
    """Full pipeline: fetch → transform → store → report."""
    logger.info("▶  Starting full pipeline")
    t0 = datetime.now()

    # Fetch
    logger.info("Fetching users and posts…")
    raw_users = fetch_json(ENDPOINTS["users"]) or []
    raw_posts  = fetch_json(ENDPOINTS["posts"]) or []

    # Transform
    users = transform_users(raw_users)
    posts  = transform_posts(raw_posts, users)
    stats  = compute_user_stats(users, posts)

    # Store
    with Database(DB_PATH) as db:
        db.init_schema()
        db.upsert_users(users)
        db.upsert_posts(posts)
        db.upsert_stats(stats)

    elapsed = (datetime.now() - t0).total_seconds()
    logger.info(f"✅  Pipeline done in {elapsed:.2f}s")

    cmd_report()


def cmd_report():
    """Print a summary report from the database."""
    print("\n" + "=" * 60)
    print("  CAPSTONE REPORT")
    print("=" * 60)

    try:
        with Database(DB_PATH) as db:
            print(f"  Users:  {db.count('users')}")
            print(f"  Posts:  {db.count('posts')}")

            print("\n── Top 5 Authors ──────────────────────────────────")
            rows = db.query(
                "SELECT name, post_count, avg_words FROM user_stats "
                "ORDER BY post_count DESC LIMIT 5"
            )
            for r in rows:
                print(f"  {r['name']:<25} posts={r['post_count']}  "
                      f"avg_words={r['avg_words']:.1f}")

            print("\n── Cities ─────────────────────────────────────────")
            rows = db.query(
                "SELECT city, COUNT(*) AS n FROM users GROUP BY city ORDER BY n DESC"
            )
            for r in rows:
                print(f"  {r['city']:<20} {r['n']} users")

    except Exception as e:
        logger.error(f"Report failed: {e}")

    print("=" * 60)


def cmd_fetch(source: str = "users"):
    """Fetch a single source and print raw record count."""
    url = ENDPOINTS.get(source)
    if not url:
        print(f"Unknown source '{source}'. Options: {list(ENDPOINTS)}")
        return
    data = fetch_json(url) or []
    print(f"Fetched {len(data)} records from '{source}'")


COMMANDS = {
    "run":    cmd_run,
    "report": cmd_report,
    "fetch":  cmd_fetch,
}

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd  = args[0] if args else "run"
    rest = args[1:]

    if cmd not in COMMANDS:
        print(f"Available commands: {list(COMMANDS)}")
        sys.exit(1)

    COMMANDS[cmd](*rest)
