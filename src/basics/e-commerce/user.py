class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get_details(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}"
