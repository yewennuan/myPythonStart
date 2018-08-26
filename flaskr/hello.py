#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2018/8/26 下午4:46

import click
from flask import current_app
from flask.cli import with_appcontext


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@with_appcontext
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

    print(current_app.config["MAIL_FROM_EMAIL"])

if __name__ == '__main__':
    hello()
