def add(a, b):
    return a + b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
def subtract(a, b): return a - b

def multiply(a, b): return a * b

# INTENTIONAL VULNERABILITY 1: Hardcoded Secret
# Gitleaks uses Shannon Entropy. Low-entropy strings (like 12345...) are ignored as false positives.
# This is a high-entropy fake token that will force Gitleaks to explode.
GITHUB_TOKEN = "ghp_8XoY2aB6k9Z1wQ0eR7tP4uI3lA5sD2fG1hJ4"

# INTENTIONAL VULNERABILITY 2 & 3: Command Injection & SQL Injection
from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

@app.route('/ping')
def ping():
    # Source: user input from request.args
    target = request.args.get('target', '')
    # Sink: OS command (CodeQL will flag this!)
    os.system("ping -c 1 " + target)
    return "Pinged " + target

@app.route('/user')
def get_user():
    username = request.args.get('username', '')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Sink: SQL execution (CodeQL will flag this!)
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return str(cursor.fetchall())


