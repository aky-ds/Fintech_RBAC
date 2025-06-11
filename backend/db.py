# Creating a backend database

users = {
    "alice@finsolve.com": {"password": "secure123", "role": "finance"},
    "bob@finsolve.com": {"password": "secure456", "role": "employee"},
    "carol@finsolve.com": {"password": "secure789", "role": "executive"}
}    # dummy users

def get_user(email):    # Retrieve user by email
    return users.get(email, None)

def add_user(email, password, role): # Add a new user
    if email in users:
        return False
    users[email] = {"password": password, "role": role}
    return True
