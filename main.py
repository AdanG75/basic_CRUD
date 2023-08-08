import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    } ,
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]


def create_client(client):
    for current_client in clients:
        if current_client['email'] == client['email']:
            client_email = client['email']
            print(f'Email {client_email} has alredy been registered')
            return

    clients.append(client)
    

def search_client(key: str, value):
    for client in clients:
        if client[key] == value:
            print(f'Client\'s {key}: {value} is in the list')
            return
        
    _show_not_found_client_message(key, value)


def search_client_by_name(name: str):
    search_client('name', name)


def search_client_by_email(email: str):
    search_client('email', email)


def update_client(client_email: str):
    for index, client in enumerate(clients):
        if client['email'] == client_email:
            print("\t***** New Name *****")
            updated_client = _get_client_data()
            clients[index] = updated_client
            return
    
    _show_not_found_client_message('email', client_email)


def delete_client(client_email: str):

    for index, client in enumerate(clients):
        if client['email'] == client_email:
            clients.pop(index)
            return

    _show_not_found_client_message('email', client_email)


def list_clients():
    for index, client in enumerate(clients):
        print(f"{index}- {client}")


def _add_comma():
    global clients

    clients += ','


def _get_client_data():
    client_name = _get_data('name')
    client_email = _get_data('email')
    client_position = _get_data('position')
    client_company = _get_data('company')

    return {
        'name': client_name,
        'company': client_company,
        'email': client_email,
        'position': client_position
    }


def _get_data(data_required: str):
    client_data = None

    while not client_data:
        client_data = input(f"Give me the {data_required} of client, please:\n-> ")
    
        if client_data == 'exit':
            sys.exit()

    return client_data 


def _show_not_found_client_message(client_property, client_data):
    print(f"Client\'s {client_property}: {client_data} is not in the list")


def print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[S]earch client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[V]iew clients')


if __name__ == '__main__':
    print_welcome()
    command = input("Choice a option:\n-> ")
    command =  command.upper()

    if command == 'C':
        client = _get_client_data()
        create_client(client)
    elif command == 'S':
        client_name = _get_data('name')
        search_client_by_name(client_name)
    elif command == 'D':
        client_email = _get_data('email')
        delete_client(client_email)
    elif command == 'U':
        client_email = _get_data('email')
        update_client(client_email)
    elif command == 'V':
        print('\t*** Clients ***')
        list_clients()
    else:
        print('Invalid command')

    list_clients()