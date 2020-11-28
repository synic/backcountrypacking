import argparse
import functools
import os
import subprocess
import sys

parser = argparse.ArgumentParser(prog='./manage')
subparsers = parser.add_subparsers()
parsers = {}
default_container = ''
default_command = None


class Color(object):
    debug = '\033[96m'
    info = '\033[92m'
    warning = '\033[93m'
    error = '\033[91m'
    endc = '\033[0m'


class Option(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class File(object):
    def __init__(self, fn):
        if fn.lower().endswith('.sql'):
            self.fmt = 'sql'
        elif fn.lower().endswith('.json'):
            self.fmt = 'json'
        else:
            raise ValueError('Invalid file import extension')
        self.fn = fn

    def __str__(self):
        return self.fn


def file(fn):
    return File(fn) if fn else None


def command(options=(), passthrough=False, default=False):
    def decorator(func):
        global default_command

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        name = func.__name__.replace('_', '-')
        parser = subparsers.add_parser(name, help=func.__doc__)
        parser.set_defaults(func=func)

        for option in options:
            parser.add_argument(*option.args, **option.kwargs)

        wrapper.passthrough = passthrough
        wrapper.command_name = name

        if default:
            if default_command:
                raise ValueError('There can only be one default command.')
            default_command = wrapper

        parsers[name] = wrapper
        return wrapper

    return decorator


option = Option


def run(cmd):
    logcmd(cmd)
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
        error(
            f'The "{container}" container does not appear '
            'to be running. Try "docker-compose up -d".'
        )
        return

    run(f'docker exec -it {container} {cmd}')


def log(msg, color=Color.endc):
    print(f'{color}{msg}{Color.endc}')


def logcmd(msg):
    log(f' -> {msg}', Color.debug)


def info(msg):
    log(msg, Color.info)


def warning(msg):
    log(msg, Color.warning)


def error(msg):
    log(f'ERROR: {msg}', Color.error)


def main(prog='./manage'):
    parser.prog = prog
    default = default_command.command_name if default_command else None
    args = sys.argv[1:]
    command = None

    try:
        command = parsers[args[0]].command_name
        if command == default:
            args = args[1:]
    except (KeyError, IndexError):
        command = default

    if command and len(args):
        if parsers[command].passthrough:
            parsers[command](args)
            sys.exit(0)

    if not args:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args(args)

    if getattr(args, 'func', None):
        args.func(args)
