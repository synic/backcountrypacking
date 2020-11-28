import argparse
import functools
import os
import subprocess
import sys

parser = argparse.ArgumentParser(prog='./manage')
subparsers = parser.add_subparsers()
parsers = {}
default_container = ''


def option(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        parser = parsers.get(func.__name__)
        if not parser:
            parser = subparsers.add_parser(func.__name__, help=func.__doc__)
            parser.set_defaults(func=func)
            parsers[func.__name__] = parser

        if args or kwargs:
            parser.add_argument(*args, **kwargs)

        return wrapper

    return decorator


def command(func):
    return option()(func)


def run(cmd):
    print(f' -> {cmd}')
    os.system(f'{cmd}')


def crun(cmd, container=None):
    running = False
    if container is None:
        container = default_container

    try:
        output = subprocess.check_output(
            f'docker inspect --format {{{{.State.Running}}}} '
            f'{container}'.split()
        ).decode('utf8').strip()
        running = output == 'true'
    except subprocess.CalledProcessError:
        pass

    if not running:
        print(
            f' -> ERROR: The "{container}" container does not appear '
            'to be running. Try "docker-compose up -d".'
        )
        return

    run(f'docker exec -it {container} {cmd}')


def run_commands():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    try:
        command = sys.argv[1]
        if command not in ('-h', '--help') and command not in parsers:
            sys.argv.insert(1, 'manage')
    except IndexError:
        pass

    args, extras = parser.parse_known_args()

    if getattr(args, 'func', None):
        args.func(args, extras)
