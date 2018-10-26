#!/bin/env python

import click
import os
import sys
import re


@click.group()
def cli():
    pass

@cli.command()
@click.option("--username")
def subcli(username):
    print("given username {}".format(username))


if __name__ == "__main__":
    cli()
