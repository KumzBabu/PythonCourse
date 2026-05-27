# ============================================================
# Capstone — Data Fetcher
# Handles all HTTP communication (sync + async)
# ============================================================

import logging
import time
import asyncio
import requests

logger = logging.getLogger(__name__)

try:
    import aiohttp
    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False
    logger.warning("aiohttp not installed — async fetch will use asyncio.sleep simulation")


# ─────────────────────────────────────────────
# Sync fetcher (with retry)
# ─────────────────────────────────────────────

def fetch_json(url: str, params: dict = None, max_retries: int = 3,
               timeout: int = 10) -> dict | list | None:
    """
    Fetch JSON from a URL with exponential-backoff retry.
    Returns parsed JSON or None on failure.
    """
    for attempt in range(1, max_retries + 1):
        try:
            logger.debug(f"GET {url} (attempt {attempt})")
            r = requests.get(url, params=params, timeout=timeout)
            r.raise_for_status()
            data = r.json()
            logger.info(f"Fetched {url} — {len(data) if isinstance(data, list) else 1} record(s)")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP {e.response.status_code} on {url}")
            return None
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            wait = 1.5 ** attempt
            logger.warning(f"Attempt {attempt} failed ({e}). Retrying in {wait:.1f}s…")
            if attempt < max_retries:
                time.sleep(wait)
    logger.error(f"All {max_retries} attempts failed for {url}")
    return None


# ─────────────────────────────────────────────
# Async fetcher
# ─────────────────────────────────────────────

async def async_fetch_json(url: str, session=None, params: dict = None) -> dict | list | None:
    """Async version of fetch_json using aiohttp."""
    if not AIOHTTP_AVAILABLE:
        # Fallback: sync call in executor
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, fetch_json, url)

    try:
        async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as r:
            r.raise_for_status()
            data = await r.json()
            logger.debug(f"Async fetched: {url}")
            return data
    except Exception as e:
        logger.error(f"Async fetch failed for {url}: {e}")
        return None


async def fetch_all_async(urls: list[str]) -> list:
    """Fetch multiple URLs concurrently."""
    if AIOHTTP_AVAILABLE:
        async with aiohttp.ClientSession() as session:
            tasks = [async_fetch_json(url, session) for url in urls]
            return await asyncio.gather(*tasks)
    else:
        tasks = [async_fetch_json(url) for url in urls]
        return await asyncio.gather(*tasks)
