def add(a, b):
    return a + b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
def subtract(a, b): return a - b

def multiply(a, b): return a * b

# INTENTIONAL VULNERABILITY 1: Hardcoded Secret
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyza"

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


