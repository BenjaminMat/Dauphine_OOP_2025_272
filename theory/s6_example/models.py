

class User:
    def __init__(self, username):
        self.username = username

    def get_data(self):
        return DataService.fetch_user_data(self.username)