import sqlite3
from faker import Faker
import time


# conn = sqlite3.connect("customer_db.db")
# c = conn.cursor()

# conn.execute("CREATE INDEX email_index ON customers(email);")
# c.close()
# conn.close()

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

start = time.perf_counter_ns()

c.execute("SELECT * FROM customers WHERE email='johnsonseth@example.net'")

results = c.fetchall()

end = time.perf_counter_ns()

print(results)
print(end - start, "ns")

c.close()
conn.close()

exit()

fake = Faker()

conn = sqlite3.connect("customer_db.db")
c = conn.cursor()

c.execute("""CREATE TABLE customers
(id INTEGER PRIMARY KEY,
name TEXT,
email TEXT,
phone TEXT)
""")

for _ in range(50000):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    c.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
              (name, email, phone))

conn.commit()
c.close()
conn.close()
