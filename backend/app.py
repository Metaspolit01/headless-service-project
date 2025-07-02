from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "mydb")
DB_USER = os.environ.get("DB_USER", "myuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mypassword")

@app.route('/api')
def hello():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT,
            database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute('SELECT NOW();')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({'status': 'ok', 'time': row[0].isoformat()})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

