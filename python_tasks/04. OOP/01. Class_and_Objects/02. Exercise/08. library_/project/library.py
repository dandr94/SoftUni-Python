class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if any([x for x in self.user_records if x == user]):
            return f'User with id = {user.user_id} already registered in the library!'

        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return 'We could not find such user to remove!'

    def change_username(self, user_id, new_username):
        users_list = [x for x in self.user_records if x.user_id == user_id]

        if users_list:
            user = users_list[0]

            if user.username != new_username:
                old_username = user.username
                user.username = new_username
                if old_username in self.rented_books:
                    user_books = self.rented_books[old_username]
                    del self.rented_books[old_username]
                    self.rented_books[user.username] = user_books
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            else:
                return f'Please check again the provided username ' \
                       f'- it should be different than the username used so far!'

        else:
            return f"There is no user with id = {user_id}!"
