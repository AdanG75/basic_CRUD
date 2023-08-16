import click
import csv
from typing import List

from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client: Client):
        print(client.to_dict(), type(client.to_dict()))
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self) -> List[dict]:
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_cient: Client):
        was_client_found = False
        client_list = self.list_clients()

        for index, client in enumerate(client_list):
            if client['uid'] == updated_cient.uid:
                client_list[index] = updated_cient.to_dict()

                was_client_found = True
                break

        if was_client_found:
            self._save_to_disk(client_list)

        else:
            click.echo("Client not found")

    def delete_client(self, uid: str):
        was_client_found = False
        client_list = self.list_clients()

        for index, client in enumerate(client_list):
            if client['uid'] == uid:
                client_list.pop(index)

                was_client_found = True
                break

        if was_client_found:
            self._save_to_disk(client_list)

        else:
            click.echo("Client not found")

    def _save_to_disk(self, client_list: List[Client]):
        with open(self.table_name, mode="w") as f:
                writer = csv.DictWriter(f, fieldnames=Client.schema())
                writer.writerows(client_list)
            

            

    
