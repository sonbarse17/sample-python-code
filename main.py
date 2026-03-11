def add(a, b):
    return a + b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
def subtract(a, b): return a - b

def multiply(a, b): return a * b

# INTENTIONAL VULNERABILITY 1: Hardcoded Secret (Gitleaks will catch this)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

# INTENTIONAL VULNERABILITY 2: Command Injection (CodeQL and Bandit will catch this)
import os
def execute_system_command(user_input):
    return os.system("ping -c 1 " + user_input)

