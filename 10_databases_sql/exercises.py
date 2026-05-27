# ============================================================
# MODULE 10: Databases & SQL — Exercises
# ============================================================
# Run lesson.py FIRST to create & populate sample.db
# Then run this file: python exercises.py
# ============================================================

import sqlite3

conn = sqlite3.connect("sample.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


# ── EXERCISE 1 ──────────────────────────────────────────────
# List all products in the "Electronics" category,
# sorted by price ascending. Print name and price.
print("=" * 55)
print("Exercise 1: Electronics catalog")
print("=" * 55)

# YOUR CODE HERE ↓
# cursor.execute(...)
# for row in cursor.fetchall(): print(...)


# ── EXERCISE 2 ──────────────────────────────────────────────
# Find all customers who have placed MORE THAN 1 order.
# Print: customer name, number of orders.
print("\n" + "=" * 55)
print("Exercise 2: Repeat customers")
print("=" * 55)

# YOUR CODE HERE ↓
# Hint: GROUP BY + HAVING COUNT > 1


# ── EXERCISE 3 ──────────────────────────────────────────────
# Calculate the total revenue generated per product.
# Show: product name, units sold, total revenue.
# Sort by total revenue descending.
print("\n" + "=" * 55)
print("Exercise 3: Revenue per product")
print("=" * 55)

# YOUR CODE HERE ↓


# ── EXERCISE 4 ──────────────────────────────────────────────
# Find the most expensive item each customer has ordered.
# Print: customer name, most expensive product, price.
print("\n" + "=" * 55)
print("Exercise 4: Most expensive item per customer")
print("=" * 55)

# YOUR CODE HERE ↓
# Hint: Use a subquery or window function (MAX)


# ── EXERCISE 5 ──────────────────────────────────────────────
# Add a new customer and immediately place an order for them.
# Use a transaction — if the order insert fails, rollback both.
# New customer: "Frank Ocean", "frank@example.com", "Miami"
# Order: product_id=3, quantity=2
print("\n" + "=" * 55)
print("Exercise 5: Transaction — new customer + order")
print("=" * 55)

# YOUR CODE HERE ↓
try:
    # cursor.execute("INSERT INTO customers ...", (...))
    # new_cust_id = cursor.lastrowid
    # cursor.execute("INSERT INTO orders ...", (...))
    # conn.commit()
    print("Transaction committed!")
except Exception as e:
    conn.rollback()
    print(f"Rolled back: {e}")


# ── EXERCISE 6 ──────────────────────────────────────────────
# Write a function search_products(keyword, max_price=None)
# that returns products whose name contains the keyword
# (case-insensitive) and optionally filters by max price.
print("\n" + "=" * 55)
print("Exercise 6: Product search function")
print("=" * 55)

def search_products(keyword: str, max_price: float = None) -> list:
    """Return products matching keyword, optionally within max_price."""
    # YOUR CODE HERE ↓
    # Use LIKE '%?%' — note: LIKE requires special handling
    # Tip: use cursor.execute("... WHERE name LIKE ?", (f"%{keyword}%",))
    pass

results = search_products("pro")
print(f"Results for 'pro': {results}")

results = search_products("book", max_price=50)
print(f"Results for 'book' under $50: {results}")


# ── EXERCISE 7 (CHALLENGE) ──────────────────────────────────
# Create a VIEW called "order_summary" that combines:
# customer name, product name, quantity, total price, order date.
# Then query the view to find orders placed in January 2024.
print("\n" + "=" * 55)
print("Exercise 7 (Challenge): SQL View")
print("=" * 55)

# YOUR CODE HERE ↓
# cursor.execute("DROP VIEW IF EXISTS order_summary")
# cursor.execute("CREATE VIEW order_summary AS SELECT ...")
# cursor.execute("SELECT * FROM order_summary WHERE order_date LIKE '2024-01-%'")
# for row in cursor.fetchall(): print(dict(row))


# ── EXERCISE 8 (CHALLENGE) ──────────────────────────────────
# Add an INDEX on orders(customer_id) and orders(product_id).
# Explain why indexes speed up JOIN queries.
# Then use EXPLAIN QUERY PLAN to verify it's being used.
print("\n" + "=" * 55)
print("Exercise 8 (Challenge): Indexes & EXPLAIN")
print("=" * 55)

# YOUR CODE HERE ↓
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id)")
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_product  ON orders(product_id)")
# cursor.execute("EXPLAIN QUERY PLAN SELECT ... FROM orders JOIN ...")
# for row in cursor.fetchall(): print(dict(row))


conn.close()
print("\nDone.")
