class Profile:
    def __init__(self, username, password):
        if 5 <= len(username) <= 15:
            self.username = username
        else:
            raise ValueError('The username must be between 5 and 15 characters.')
        if len(password) >= 8 and \
                any(x for x in password if x.isupper()) and \
                any(x for x in password if x.isdigit()):
            self.password = password
        else:
            raise ValueError('The password must be 8 or more characters '
                             'with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.username}" ' \
               f'and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
