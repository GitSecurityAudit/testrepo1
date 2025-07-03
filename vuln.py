import os
# Mock vulnerability: Hardcoded secret
API_KEY = "abc123xyz789secret"

# Mock vulnerability: Insecure deserialization
import pickle
def load_data(file):
    return pickle.load(file)  # Insecure deserialization

# Mock vulnerability: SQL injection
def query_user(user_input):
    return f"SELECT * FROM users WHERE id = {user_input}"  # SQL injection
