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
        return """
<!DOCTYPE html>
<html>
<head>
    <title>Kossi DevOps Lab</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #06121f, #0f5132, #00c896);
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .card {
            background: rgba(255, 255, 255, 0.12);
            padding: 50px;
            border-radius: 25px;
            text-align: center;
            box-shadow: 0 0 40px rgba(0, 255, 170, 0.45);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            max-width: 700px;
        }

        h1 {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .status {
            color: #9cffc7;
            font-size: 24px;
            margin-bottom: 20px;
        }

        p {
            font-size: 18px;
            line-height: 1.6;
        }

        .badge {
            display: inline-block;
            margin-top: 25px;
            padding: 12px 25px;
            background: #00ffae;
            color: #06121f;
            border-radius: 30px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 David Hevi DevOps Lab</h1>
        <div class="status">Database Connected Successfully ✅</div>
        <p>
            This Flask application is running inside Docker, connected to MySQL,
            deployed through Jenkins, and managed with Docker Compose so exicted about the bext steps.
        </p>
        <div class="badge">CI/CD Pipeline Active</div>
    </div>
</body>
</html>
"""
    except Exception as e:
        return f"<h1>Database Connection Failed</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)