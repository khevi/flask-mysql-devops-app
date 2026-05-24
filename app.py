from flask import Flask, request, redirect
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devopspass"),
        database=os.getenv("DB_NAME", "devopsdb")
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    init_db()

    if request.method == "POST":
        name = request.form.get("name")
        if name:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO visitors (name) VALUES (%s)", (name,))
            conn.commit()
            cursor.close()
            conn.close()
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM visitors ORDER BY id DESC")
    visitors = cursor.fetchall()
    cursor.close()
    conn.close()

    visitor_list = "".join([f"<li>{v[0]}</li>" for v in visitors])

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kossi DevOps CRUD Lab</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #06121f, #0f5132, #00c896);
                color: white;
                text-align: center;
                padding: 60px;
            }}
            .card {{
                max-width: 700px;
                margin: auto;
                background: rgba(255,255,255,0.12);
                padding: 40px;
                border-radius: 25px;
                box-shadow: 0 0 35px rgba(0,255,170,0.35);
            }}
            input {{
                padding: 14px;
                width: 60%;
                border-radius: 10px;
                border: none;
                font-size: 18px;
            }}
            button {{
                padding: 14px 25px;
                border: none;
                border-radius: 10px;
                background: #00ffae;
                font-weight: bold;
                cursor: pointer;
                font-size: 18px;
            }}
            ul {{
                list-style: none;
                padding: 0;
                margin-top: 30px;
            }}
            li {{
                background: rgba(255,255,255,0.18);
                margin: 10px auto;
                padding: 12px;
                border-radius: 10px;
                width: 60%;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Kossi DevOps CRUD Lab</h1>
            <p>Flask + MySQL + Docker Compose + Jenkins + Nginx</p>

            <form method="POST">
                <input type="text" name="name" placeholder="Enter your name" required>
                <button type="submit">Save</button>
            </form>

            <h2>Saved Visitors</h2>
            <ul>
                {visitor_list}
            </ul>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)