clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print(f'Client {client_name} has alredy been registered')


def list_clients():
    print(clients)


def _add_comma():
    global clients

    clients += ','


def print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    print_welcome()
    command = input("Choice a option:\n-> ")

    if command == 'C':
        client_name = input("Give me your name, please:\n-> ")
        create_client(client_name)
    elif command == 'D':
        pass
    else:
        print('Invalid command')

    list_clients()