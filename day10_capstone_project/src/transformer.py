# ============================================================
# Capstone — Data Transformer
# Cleans, enriches, and structures raw API data
# ============================================================

import logging

logger = logging.getLogger(__name__)

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    logger.warning("pandas not installed — transformations will use plain dicts")


def transform_users(raw_users: list[dict]) -> list[dict]:
    """Flatten and validate user records from JSONPlaceholder."""
    if not raw_users:
        return []

    transformed = []
    for u in raw_users:
        try:
            transformed.append({
                "id":       int(u["id"]),
                "name":     u["name"].strip(),
                "email":    u["email"].lower().strip(),
                "username": u.get("username", ""),
                "city":     u.get("address", {}).get("city", "Unknown"),
                "company":  u.get("company", {}).get("name", "Unknown"),
            })
        except (KeyError, ValueError, TypeError) as e:
            logger.warning(f"Skipping malformed user record {u.get('id')}: {e}")

    logger.info(f"Transformed {len(transformed)}/{len(raw_users)} user records")
    return transformed


def transform_posts(raw_posts: list[dict], users: list[dict]) -> list[dict]:
    """Enrich posts with author info and computed fields."""
    if not raw_posts:
        return []

    user_map = {u["id"]: u["name"] for u in users}
    transformed = []

    for p in raw_posts:
        try:
            transformed.append({
                "id":         int(p["id"]),
                "user_id":    int(p["userId"]),
                "author":     user_map.get(p["userId"], "Unknown"),
                "title":      p["title"].strip().title(),
                "body":       p["body"].strip(),
                "word_count": len(p["body"].split()),
                "char_count": len(p["body"]),
            })
        except (KeyError, ValueError, TypeError) as e:
            logger.warning(f"Skipping malformed post {p.get('id')}: {e}")

    logger.info(f"Transformed {len(transformed)} posts")
    return transformed


def compute_user_stats(users: list[dict], posts: list[dict]) -> list[dict]:
    """Compute per-user statistics from posts."""
    from collections import defaultdict

    user_posts: dict[int, list] = defaultdict(list)
    for p in posts:
        user_posts[p["user_id"]].append(p)

    stats = []
    for u in users:
        uid = u["id"]
        uposts = user_posts[uid]
        stats.append({
            "user_id":       uid,
            "name":          u["name"],
            "post_count":    len(uposts),
            "avg_words":     round(sum(p["word_count"] for p in uposts) / len(uposts), 1) if uposts else 0,
            "total_chars":   sum(p["char_count"] for p in uposts),
        })

    return sorted(stats, key=lambda x: x["post_count"], reverse=True)


def to_dataframe(records: list[dict]):
    """Convert records to a pandas DataFrame (if available)."""
    if not PANDAS_AVAILABLE:
        logger.warning("pandas not available — returning raw list")
        return records
    return pd.DataFrame(records)
