class Profile:
    min_lenght_username = 5
    max_lenght_username = 15

    min_lenght_password = 8
    min_uppercase_letters = 1
    min_digits = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if self.min_lenght_username > len(username) or self.max_lenght_username < len(username):
            raise ValueError("The username must be between 5 and 15 characters.")

    def __validate_password(self, password):
        if len(password) < self.min_lenght_password:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in password if x.isupper()]) < self.min_uppercase_letters:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in password if x.isdigit()]) < self.min_digits:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def password(self):
        return "".join("*" * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'


profile_with_invalid_username = Profile('Too_long_username', 'Any')
print(profile_with_invalid_username)