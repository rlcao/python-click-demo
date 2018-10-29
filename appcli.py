#!/bin/env python

import click
import os
import sys
import re


@click.group()
@click.option("--username")
@click.option("--password")
def cli(username,password):
    ctx = click.get_current_context()
    print('cli -> {}'.format(ctx.params))
    print('usernmae -> {}'.format(username))
    ctx.obj['username'] = username
    pass

@cli.command()
@click.pass_context
def subcli(ctx):
    #ctx = click.get_current_context()
    parent = ctx.parent
    print("{}".format(parent.params))
    print("given username {}".format(parent.params['username']))
    print("from obj username -> {}".format(ctx.obj['username']))


if __name__ == "__main__":
    cli(obj={})
