import click


from clients.services import ClientService
from clients.models import Client as ClientModel


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option(
    '-n', 
    '--name', 
    type=str, 
    prompt=True, 
    help='The client name'
    )
@click.option(
    '-c', 
    '--company', 
    type=str, 
    prompt=True, 
    help='The client company'
    )
@click.option(
    '-e', 
    '--email', 
    type=str, 
    prompt=True, 
    help='The client email'
    )
@click.option(
    '-p', 
    '--position', 
    type=str, 
    prompt=True, 
    help='The client position'
    )
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new Client"""
    client = ClientModel(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    click.echo('  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*' * 80)

    for client in client_service.list_clients():
        click.echo('{} | {} | {} | {} | {}'.format(
            client['uid'],
            client['name'],
            client['company'],
            client['email'],
            client['position']
        ))


@clients.command()
@click.option(
    '-u', 
    '--uid', 
    type=str, 
    prompt=True, 
    help='The client ID'
    )
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = client_service.get_client(uid)
    
    if client is None:
        click.echo("Client not found")
    else:
        client = _updated_client_flow(client)
        was_client_updated = client_service.update_client(client)

        if was_client_updated:
            click.echo(f"Client with ID:{uid} was updated")
        else:
            click.echo("Client not found")


def _updated_client_flow(client: ClientModel) -> ClientModel:
    click.echo('Leave empty if you do not want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New Company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.option(
    '-u', 
    '--uid', 
    type=str, 
    prompt=True, 
    help='The client ID'
    )
@click.pass_context
def delete(ctx, uid):
    """Deleles a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    was_client_deleted = client_service.delete_client(uid=uid)

    if was_client_deleted:
        click.echo(f"Client with ID:{uid} was deleted")
    else:
        click.echo("Client not found")


all = clients