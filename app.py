from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "devops"),
            password=os.getenv("DB_PASSWORD", "devopspass"),
            database=os.getenv("DB_NAME", "devopsdb")
        )
        conn.close()
        return "<h1>Hello Kossi — Database Connected Successfully!</h1>"
    except Exception as e:
        return f"<h1>Database Connection Failed</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)