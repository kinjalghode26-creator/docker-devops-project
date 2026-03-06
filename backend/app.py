from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="mydb"
        )
        return "Backend connected to MySQL successfully!"
    except:
        return "Database connection failed"

app.run(host="0.0.0.0", port=5000)
