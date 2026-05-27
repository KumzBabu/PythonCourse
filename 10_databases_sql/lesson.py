# ============================================================
# MODULE 10: Databases & SQL with Python
# Day 6 of 10-Day Python Intensive
# ============================================================
# Uses: sqlite3 (built-in) — no install needed!
# Optional: pip install sqlalchemy pandas
# ============================================================

import sqlite3
import os

DB_PATH = "sample.db"

# ─────────────────────────────────────────────
# 1. CONNECTING & CREATING A DATABASE
# ─────────────────────────────────────────────

conn = sqlite3.connect(DB_PATH)   # creates file if not exists
cursor = conn.cursor()

print(f"Connected to: {DB_PATH}")
print(f"SQLite version: {sqlite3.sqlite_version}")


# ─────────────────────────────────────────────
# 2. CREATE TABLES
# ─────────────────────────────────────────────

cursor.executescript("""
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS customers;

    CREATE TABLE customers (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT    NOT NULL,
        email       TEXT    UNIQUE NOT NULL,
        city        TEXT,
        joined_date TEXT    DEFAULT (date('now'))
    );

    CREATE TABLE products (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        name     TEXT    NOT NULL,
        category TEXT,
        price    REAL    NOT NULL,
        stock    INTEGER DEFAULT 0
    );

    CREATE TABLE orders (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        product_id  INTEGER NOT NULL,
        quantity    INTEGER NOT NULL,
        order_date  TEXT    DEFAULT (date('now')),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id)  REFERENCES products(id)
    );
""")
conn.commit()
print("Tables created.")


# ─────────────────────────────────────────────
# 3. INSERT DATA
# ─────────────────────────────────────────────

# executemany — batch insert (safe from SQL injection)
customers = [
    ("Alice Johnson", "alice@example.com", "New York"),
    ("Bob Smith",     "bob@example.com",   "Chicago"),
    ("Carol White",   "carol@example.com", "San Francisco"),
    ("David Brown",   "david@example.com", "Austin"),
    ("Eve Davis",     "eve@example.com",   "New York"),
]
cursor.executemany(
    "INSERT INTO customers (name, email, city) VALUES (?, ?, ?)",
    customers
)

products = [
    ("Laptop Pro",    "Electronics", 1299.99, 15),
    ("Wireless Mouse","Electronics",   29.99, 150),
    ("Python Book",   "Books",          39.99, 80),
    ("Standing Desk", "Furniture",     499.99, 10),
    ("Noise Cancelling Headphones", "Electronics", 199.99, 45),
    ("Web Dev Course","Education",     149.99, 999),
    ("Coffee Maker",  "Appliances",     89.99, 30),
]
cursor.executemany(
    "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
    products
)

orders = [
    (1, 1, 1, "2024-01-15"),   # Alice bought 1 Laptop
    (1, 2, 2, "2024-01-16"),   # Alice bought 2 Mice
    (2, 3, 1, "2024-01-17"),   # Bob bought 1 Book
    (3, 1, 1, "2024-01-18"),   # Carol bought 1 Laptop
    (3, 5, 1, "2024-01-18"),   # Carol bought 1 Headphones
    (4, 6, 2, "2024-01-19"),   # David bought 2 Courses
    (5, 7, 1, "2024-01-20"),   # Eve bought 1 Coffee Maker
    (2, 4, 1, "2024-01-21"),   # Bob bought 1 Desk
    (1, 6, 1, "2024-01-22"),   # Alice bought 1 Course
    (5, 2, 3, "2024-01-22"),   # Eve bought 3 Mice
]
cursor.executemany(
    "INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)",
    orders
)
conn.commit()
print("Sample data inserted.")


# ─────────────────────────────────────────────
# 4. READ — SELECT QUERIES
# ─────────────────────────────────────────────

# fetchall → list of tuples
print("\n── All customers ──")
cursor.execute("SELECT id, name, city FROM customers")
for row in cursor.fetchall():
    print(f"  {row}")

# fetchone → single row
cursor.execute("SELECT * FROM products WHERE price > 100 ORDER BY price DESC")
print("\n── Premium products (price > $100) ──")
for row in cursor.fetchall():
    print(f"  {row}")

# Row factory — access columns by name
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT name, price, category FROM products ORDER BY category, price")
print("\n── Products with named columns ──")
for row in cursor.fetchall():
    print(f"  [{row['category']}] {row['name']} — ${row['price']:.2f}")


# ─────────────────────────────────────────────
# 5. JOINs
# ─────────────────────────────────────────────

query = """
    SELECT
        c.name        AS customer,
        p.name        AS product,
        p.price,
        o.quantity,
        ROUND(p.price * o.quantity, 2) AS total,
        o.order_date
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products  p ON o.product_id  = p.id
    ORDER BY o.order_date, c.name
"""
cursor.execute(query)
print("\n── Order details ──")
for row in cursor.fetchall():
    print(f"  {row['customer']:<15} {row['product']:<35} ${row['total']:.2f}")


# ─────────────────────────────────────────────
# 6. AGGREGATE QUERIES
# ─────────────────────────────────────────────

# Total revenue per customer
revenue_query = """
    SELECT
        c.name,
        COUNT(o.id)                         AS order_count,
        ROUND(SUM(p.price * o.quantity), 2) AS total_spent
    FROM customers c
    JOIN orders   o ON c.id = o.customer_id
    JOIN products p ON o.product_id = p.id
    GROUP BY c.id
    ORDER BY total_spent DESC
"""
cursor.execute(revenue_query)
print("\n── Revenue per customer ──")
for row in cursor.fetchall():
    print(f"  {row['name']:<15} orders={row['order_count']}  spent=${row['total_spent']:.2f}")

# Best-selling product category
cursor.execute("""
    SELECT p.category, SUM(o.quantity) AS units_sold
    FROM   orders o JOIN products p ON o.product_id = p.id
    GROUP  BY p.category
    ORDER  BY units_sold DESC
""")
print("\n── Sales by category ──")
for row in cursor.fetchall():
    print(f"  {row['category']:<15} {row['units_sold']} units")


# ─────────────────────────────────────────────
# 7. UPDATE & DELETE
# ─────────────────────────────────────────────

# UPDATE — raise price of all books by 10%
cursor.execute(
    "UPDATE products SET price = ROUND(price * 1.10, 2) WHERE category = 'Books'"
)
print(f"\nUpdated {cursor.rowcount} book(s) price (+10%)")

# DELETE — remove out-of-stock items (hypothetically)
cursor.execute("DELETE FROM products WHERE stock = 0")
print(f"Deleted {cursor.rowcount} out-of-stock products")

conn.commit()


# ─────────────────────────────────────────────
# 8. PARAMETERISED QUERIES — SQL Injection Safety
# ─────────────────────────────────────────────

def get_customer_orders(customer_name: str):
    """SAFE: always use ? placeholders, never f-strings in SQL."""
    cursor.execute("""
        SELECT c.name, p.name AS product, o.quantity, o.order_date
        FROM   orders o
        JOIN   customers c ON o.customer_id = c.id
        JOIN   products  p ON o.product_id  = p.id
        WHERE  c.name = ?
    """, (customer_name,))
    return cursor.fetchall()

alice_orders = get_customer_orders("Alice Johnson")
print(f"\n── Alice's orders ({len(alice_orders)}) ──")
for o in alice_orders:
    print(f"  {o['product']} × {o['quantity']}  on {o['order_date']}")

# ❌ NEVER do this (SQL injection risk):
# cursor.execute(f"SELECT * FROM customers WHERE name = '{user_input}'")


# ─────────────────────────────────────────────
# 9. TRANSACTIONS
# ─────────────────────────────────────────────

def transfer_stock(from_product_id: int, to_product_id: int, qty: int):
    """Move stock between products atomically."""
    try:
        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (qty, from_product_id)
        )
        cursor.execute(
            "UPDATE products SET stock = stock + ? WHERE id = ?",
            (qty, to_product_id)
        )
        conn.commit()
        print(f"Transferred {qty} units from product {from_product_id} → {to_product_id}")
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed, rolled back: {e}")

transfer_stock(1, 2, 5)


# ─────────────────────────────────────────────
# 10. USING PANDAS WITH SQLITE
# ─────────────────────────────────────────────

try:
    import pandas as pd

    # Read SQL query result directly into DataFrame
    df = pd.read_sql_query(
        "SELECT c.name, SUM(p.price * o.quantity) AS spent "
        "FROM orders o JOIN customers c ON c.id=o.customer_id "
        "JOIN products p ON p.id=o.product_id GROUP BY c.id",
        conn
    )
    print("\n── Pandas + SQLite ──")
    print(df.sort_values("spent", ascending=False))

    # Write a DataFrame to SQL
    import random
    new_data = pd.DataFrame({
        "customer_id": [1, 2, 3],
        "amount": [random.uniform(10, 200) for _ in range(3)]
    })
    # new_data.to_sql("temp_transactions", conn, if_exists="replace", index=False)

except ImportError:
    print("\n(pandas not installed — skip section 10)")


# ─────────────────────────────────────────────
# CLEANUP
# ─────────────────────────────────────────────

conn.close()
print("\nConnection closed.")


# ─────────────────────────────────────────────
# KEY TAKEAWAYS
# ─────────────────────────────────────────────
"""
SQLITE3 QUICK REFERENCE
═══════════════════════
Connect   : conn = sqlite3.connect("file.db")
Cursor    : cursor = conn.cursor()
Execute   : cursor.execute(sql, params=(?,))
Batch     : cursor.executemany(sql, list_of_tuples)
Script    : cursor.executescript(multi_sql)
Fetch     : .fetchone()  .fetchall()  iterate cursor
Named cols: conn.row_factory = sqlite3.Row
Commit    : conn.commit()
Rollback  : conn.rollback()
Close     : conn.close()

SQL VERBS
─────────
CREATE TABLE … (col type constraints)
INSERT INTO … VALUES (?, ?)
SELECT … FROM … JOIN … WHERE … GROUP BY … ORDER BY … LIMIT
UPDATE … SET col=? WHERE …
DELETE FROM … WHERE …
"""
