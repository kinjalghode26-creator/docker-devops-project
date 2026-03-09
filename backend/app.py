from flask import Flask, request
import mysql.connector
import time

app = Flask(__name__)

# Wait for MySQL to start
while True:
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="mydb"
        )
        break
    except:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
)
""")

@app.route("/")
def home():
    return "Backend running!"

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")

    sql = "INSERT INTO users (name) VALUES (%s)"
    val = (name,)
    cursor.execute(sql, val)
    db.commit()

    return f"User {name} added to database!"

@app.route("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    return str(result)

app.run(host="0.0.0.0", port=5000)
