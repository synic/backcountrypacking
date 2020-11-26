#!/usr/bin/env python

import os
import subprocess
import sys
import time

import click

web_container = 'bcp-web'
db_container = 'bcp-db'
network = 'bcp'
db_pass = 'bcp'
db_name = 'postgres'
db_uri = f'postgres://postgres:{db_pass}@{db_container}/{db_name}'
port = os.getenv('PORT', '8001')
volume = os.getcwd()
web_image = 'bcp-web-image:latest'
additional_apk_packages = (
    'vim',
    'iputils',
    'postgresql-client',
)
additional_pip_packages = (
    'ipdb',
    'ipython',
)


def check_cmd(cmd, show_output=False):
    return subprocess.call(
        cmd.split(),
        stdout=subprocess.DEVNULL if not show_output else None,
        stderr=subprocess.DEVNULL if not show_output else None,
    ) == 0


def run_cmd(cmd):
    click.echo(click.style(cmd, fg='green'))
    check_cmd(cmd, show_output=True)


def cnt_cmd(container, cmd):
    run_cmd(f'docker exec -it {container} {cmd}')


@click.group()
@click.pass_context
def cli(ctx):
    if len(sys.argv) <= 1:
        click.echo(ctx.get_help())
        ctx.exit()


@cli.command()
def bash():
    cnt_cmd(web_container, 'bash')


@cli.command(context_settings=dict(ignore_unknown_options=True))
@click.argument('manage_args', nargs=-1, type=click.UNPROCESSED)
def manage(manage_args):
    cnt_cmd(web_container, 'django-admin {}'.format(' '.join(manage_args)))


@cli.command()
def build():
    cmd = ['date', '+%Y%m%d%H%M']
    date = subprocess.check_output(cmd).decode('utf8').strip()
    run_cmd(f'docker build --build-arg=DATE={date} --rm -t {web_image} .')


@cli.command()
@click.option('--extras', '-e', is_flag=True)
def start(extras):
    if not check_cmd(f'docker inspect {network}'):
        run_cmd(f'docker network create --driver bridge {network}')

    if not check_cmd(f'docker inspect --type container {db_container}'):
        run_cmd(
            f'docker run -d --network {network} --name {db_container} '
            f'-ePOSTGRES_PASSWORD={db_pass} postgres:12.5'
        )
    else:
        run_cmd(f'docker start {db_container}')

    # wait for db container to start up
    time.sleep(3)

    if not check_cmd(f'docker inspect --type container {web_container}'):
        run_cmd(
            f'docker run -it -d --network {network} --name {web_container} '
            f'-p {port}:8001 -v {volume}:/app/ '
            f'-eDATABASE_URI={db_uri} '
            f'-ePYTHONPATH=/app '
            f'-eBCP_DEV=1 '
            f'{web_image}'
        )
        extras = True
    else:
        run_cmd(f'docker start {web_container}')

    if extras:
        click.echo('Installing extras...')
        time.sleep(2)
        cnt_cmd(web_container, 'apk update')
        cnt_cmd(web_container, 'apk add {}'.format(
            ' '.join(additional_apk_packages)))
        cnt_cmd(web_container, 'pip3 install {}'.format(
            ' '.join(additional_pip_packages)))


if __name__ == '__main__':
    cli()
