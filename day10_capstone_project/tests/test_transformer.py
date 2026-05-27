# ============================================================
# Capstone Tests — transformer.py
# Run: pytest tests/ -v
# ============================================================

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.transformer import transform_users, transform_posts, compute_user_stats

# ── Fixtures ──────────────────────────────────

@pytest.fixture
def raw_users():
    return [
        {"id": 1, "name": " Alice Johnson ", "email": "ALICE@Example.com",
         "username": "alice", "address": {"city": "NYC"},
         "company": {"name": "TechCorp"}},
        {"id": 2, "name": "Bob Smith", "email": "bob@example.com",
         "username": "bob", "address": {"city": "Chicago"},
         "company": {"name": "DesignCo"}},
    ]

@pytest.fixture
def raw_posts():
    return [
        {"id": 1, "userId": 1, "title": "hello world",
         "body": "one two three four five"},
        {"id": 2, "userId": 1, "title": "second post",
         "body": "alpha beta gamma"},
        {"id": 3, "userId": 2, "title": "bob post",
         "body": "lorem ipsum dolor sit amet consectetur"},
    ]

@pytest.fixture
def clean_users(raw_users):
    return transform_users(raw_users)

@pytest.fixture
def clean_posts(raw_posts, clean_users):
    return transform_posts(raw_posts, clean_users)


# ── transform_users ───────────────────────────

class TestTransformUsers:
    def test_count(self, raw_users, clean_users):
        assert len(clean_users) == len(raw_users)

    def test_email_lowercased(self, clean_users):
        assert clean_users[0]["email"] == "alice@example.com"

    def test_name_stripped(self, clean_users):
        assert clean_users[0]["name"] == "Alice Johnson"

    def test_city_extracted(self, clean_users):
        assert clean_users[0]["city"] == "NYC"

    def test_company_extracted(self, clean_users):
        assert clean_users[0]["company"] == "TechCorp"

    def test_empty_input(self):
        assert transform_users([]) == []

    def test_malformed_skipped(self):
        bad = [{"id": "not-an-int", "missing_fields": True}]
        result = transform_users(bad)
        assert len(result) == 0


# ── transform_posts ───────────────────────────

class TestTransformPosts:
    def test_count(self, raw_posts, clean_posts):
        assert len(clean_posts) == len(raw_posts)

    def test_author_enriched(self, clean_posts):
        assert clean_posts[0]["author"] == "Alice Johnson"
        assert clean_posts[2]["author"] == "Bob Smith"

    def test_word_count(self, clean_posts):
        assert clean_posts[0]["word_count"] == 5   # "one two three four five"
        assert clean_posts[1]["word_count"] == 3   # "alpha beta gamma"

    def test_char_count(self, clean_posts):
        assert clean_posts[0]["char_count"] == len("one two three four five")

    def test_empty_input(self, clean_users):
        assert transform_posts([], clean_users) == []

    def test_unknown_author(self, clean_users):
        posts = [{"id": 99, "userId": 999, "title": "x", "body": "y"}]
        result = transform_posts(posts, clean_users)
        assert result[0]["author"] == "Unknown"


# ── compute_user_stats ────────────────────────

class TestComputeUserStats:
    def test_post_count(self, clean_users, clean_posts):
        stats = compute_user_stats(clean_users, clean_posts)
        alice_stat = next(s for s in stats if s["name"] == "Alice Johnson")
        assert alice_stat["post_count"] == 2

    def test_avg_words(self, clean_users, clean_posts):
        stats = compute_user_stats(clean_users, clean_posts)
        alice_stat = next(s for s in stats if s["name"] == "Alice Johnson")
        # Alice: 5 words + 3 words = avg 4.0
        assert alice_stat["avg_words"] == 4.0

    def test_sorted_by_post_count_desc(self, clean_users, clean_posts):
        stats = compute_user_stats(clean_users, clean_posts)
        counts = [s["post_count"] for s in stats]
        assert counts == sorted(counts, reverse=True)

    def test_user_with_no_posts(self, clean_users):
        stats = compute_user_stats(clean_users, [])
        for s in stats:
            assert s["post_count"] == 0
            assert s["avg_words"] == 0
