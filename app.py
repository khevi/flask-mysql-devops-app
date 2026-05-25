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
    cursor.execute("SELECT id, name FROM visitors ORDER BY id DESC")
    visitors = cursor.fetchall()
    cursor.close()
    conn.close()

    visitor_list = "".join([
        f"""
        <li>
            <span>{name}</span>
            <div>
                <a class="edit-btn" href="/edit/{visitor_id}">Edit</a>
                <form method="POST" action="/delete/{visitor_id}" style="display:inline;">
                    <button class="delete-btn" type="submit">Delete</button>
                </form>
            </div>
        </li>
        """
        for visitor_id, name in visitors
    ])

    return page_template(f"""
        <h1>🚀 Kossi DevOps CRUD Lab</h1>
        <p>Flask + MySQL + Docker Compose + Jenkins + Nginx</p>

        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <button type="submit">Save</button>
        </form>

        <h2>Saved Visitors</h2>
        <ul>{visitor_list}</ul>
    """)

@app.route("/edit/<int:visitor_id>", methods=["GET", "POST"])
def edit(visitor_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        new_name = request.form.get("name")
        cursor.execute("UPDATE visitors SET name = %s WHERE id = %s", (new_name, visitor_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    cursor.execute("SELECT name FROM visitors WHERE id = %s", (visitor_id,))
    visitor = cursor.fetchone()
    cursor.close()
    conn.close()

    if not visitor:
        return redirect("/")

    return page_template(f"""
        <h1>✏️ Edit Visitor</h1>
        <form method="POST">
            <input type="text" name="name" value="{visitor[0]}" required>
            <button type="submit">Update</button>
        </form>
        <br>
        <a class="back-btn" href="/">Back</a>
    """)

@app.route("/delete/<int:visitor_id>", methods=["POST"])
def delete(visitor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM visitors WHERE id = %s", (visitor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

def page_template(content):
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
                max-width: 800px;
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
            button, .edit-btn, .back-btn {{
                padding: 10px 18px;
                border: none;
                border-radius: 10px;
                background: #00ffae;
                color: #06121f;
                font-weight: bold;
                cursor: pointer;
                font-size: 15px;
                text-decoration: none;
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
                width: 75%;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .delete-btn {{
                background: #ff4d4d;
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """
 
@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "healthy", "database": "connected"}, 200
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)