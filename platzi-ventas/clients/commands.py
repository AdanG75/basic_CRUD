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
def update(ctx, uid, name, company, email, position):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.update_client(
        ClientModel(
            name=name,
            company=company,
            email=email,
            position=position,
            uid=uid 
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
def delete(ctx, uid):
    """Deleles a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.delete_client(uid=uid)



all = clients