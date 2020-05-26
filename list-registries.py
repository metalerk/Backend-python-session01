#!/usr/bin/env python

import click
from mysqlmodel import get_registries, get_tables
from stdout import print_registries

@click.command()
@click.argument('table', required=False)
def list_registries(table):
    if table:
        registries = get_registries(table)
        print_registries(registries, 'Table: {}'.format(table))
    else:
        tables = get_tables()
        print_registries(tables, 'Available tables: ')

if __name__ == "__main__":
    list_registries()