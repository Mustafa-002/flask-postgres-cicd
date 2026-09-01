import os
import time
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "devops_db")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres_password")

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    return None

@app.route('/')
def home():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"status": "success", "message": "Connected to PostgreSQL database!"}), 200
    return jsonify({"status": "error", "message": "Database connection failed!"}), 500

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
