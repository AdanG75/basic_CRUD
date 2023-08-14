PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Write your password:\n-> ')
        if password == PASSWORD:
            print('Welcome')
            func()
        else:
            print('The password not match')

    return wrapper


@password_required
def needs_password():
    print('Very sensitive information of user')


if __name__ == '__main__':
    needs_password()