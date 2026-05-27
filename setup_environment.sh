#!/usr/bin/env bash
# ============================================================
# Python Intensive — Environment Setup Script
# Usage: bash setup_environment.sh
# ============================================================

set -e   # exit on any error

echo "======================================================"
echo "  Python Intensive — Environment Setup"
echo "======================================================"

# ── 1. Check Python version ───────────────────
echo ""
echo "▶  Checking Python version..."
python_version=$(python3 --version 2>&1 || python --version 2>&1)
echo "   Found: $python_version"

# Require Python 3.10+
required="3.10"
current=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || \
          python  -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")

if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)" 2>/dev/null; then
    echo "   ✅ Python $current — OK"
else
    echo "   ❌ Python 3.10+ required (found $current)"
    echo "   Download: https://www.python.org/downloads/"
    exit 1
fi

# ── 2. Create virtual environment ─────────────
echo ""
echo "▶  Creating virtual environment (.venv)..."
if [ -d ".venv" ]; then
    echo "   ⚠  .venv already exists — skipping creation"
else
    python3 -m venv .venv
    echo "   ✅ .venv created"
fi

# ── 3. Activate venv ──────────────────────────
echo ""
echo "▶  Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OS" == "Windows_NT" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi
echo "   ✅ Activated"

# ── 4. Upgrade pip ────────────────────────────
echo ""
echo "▶  Upgrading pip..."
pip install --upgrade pip --quiet
echo "   ✅ pip upgraded"

# ── 5. Install dependencies ───────────────────
echo ""
echo "▶  Installing dependencies from requirements.txt..."
pip install -r requirements.txt --quiet
echo "   ✅ All packages installed"

# ── 6. Verify key imports ─────────────────────
echo ""
echo "▶  Verifying installations..."

check_import() {
    pkg=$1
    python3 -c "import $pkg; print(f'   ✅ {\"$pkg\"} OK')" 2>/dev/null || \
    echo "   ⚠  $pkg not importable"
}

check_import pandas
check_import numpy
check_import requests
check_import sqlite3
check_import pytest

# ── 7. Run sample tests ───────────────────────
echo ""
echo "▶  Running module 12 tests as smoke test..."
if [ -f "12_testing/test_examples.py" ]; then
    pytest 12_testing/test_examples.py -q --tb=short 2>&1 | tail -5
else
    echo "   (test file not found — skip)"
fi

# ── 8. Print next steps ───────────────────────
echo ""
echo "======================================================"
echo "  ✅  Setup complete!"
echo "======================================================"
echo ""
echo "  To activate this environment in future sessions:"
echo ""
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OS" == "Windows_NT" ]]; then
    echo "    .venv\\Scripts\\activate"
else
    echo "    source .venv/bin/activate"
fi
echo ""
echo "  Start learning:"
echo "    Day 1  → cd 01_basics && python lesson.py"
echo "    Day 4  → cd 08_pandas_data_wrangling && python lesson.py"
echo "    Day 10 → cd day10_capstone_project && python -m src.cli run"
echo ""
echo "  See ARCHITECTURE.md for the full 10-day roadmap."
echo "======================================================"
