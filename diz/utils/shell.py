import os


def current():
    """
    Get current shell name and path
    :return: shell name, shell path
    """
    shell = os.environ.get('SHELL', '')
    return shell.split('/')[-1], shell

