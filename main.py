import sys


clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print(f'Client {client_name} has alredy been registered')


def search_client(client_name):
    if client_name in clients:
        print(f'Client {client_name} is in the list')
    else:
        _show_not_found_client_message(client_name)


def update_client(client_name):
    global clients
    
    if client_name in clients:
        print("\t***** New Name *****")
        updated_client_name = _get_client_name()
        clients = clients.replace(client_name, updated_client_name)

    else:
        _show_not_found_client_message(client_name)


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')

    else:
        _show_not_found_client_message(client_name)


def list_clients():
    print(clients)


def _add_comma():
    global clients

    clients += ','


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("Give me your name, please:\n-> ")
    
        if client_name == 'exit':
            sys.exit()

    return client_name 


def _show_not_found_client_message(client_name):
    print(f"Client {client_name} is not in the list")


def print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[S]earch client')
    print('[U]pdate client')
    print('[D]elete client')


if __name__ == '__main__':
    print_welcome()
    command = input("Choice a option:\n-> ")
    command =  command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        search_client(client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        older_name = _get_client_name()
        update_client(older_name)
    else:
        print('Invalid command')

    list_clients()