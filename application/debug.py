#!/usr/bin/env python
import os, sys, ptvsd, pydevd
from pydevd_file_utils import setup_client_server_paths
from configurations.management import execute_from_command_line  #

# use debug.py to run the development server with remote debugging enabled

if __name__ == "__main__":

    # only attach to ptvsd in the main thread, allows using runserver without --noreload flag
    # https://github.com/Microsoft/PTVS/issues/1057
    if os.environ.get('IDE_REMOTE_DEBUG') == 'vscode':
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)

    if os.environ.get('IDE_REMOTE_DEBUG') == 'eclipse':
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            MY_PATHS_FROM_ECLIPSE_TO_PYTHON = [
                (os.environ.get('ECLIPSE_LOCAL_PATH'), os.environ.get('ECLIPSE_REMOTE_PATH')),
            ]
            setup_client_server_paths(MY_PATHS_FROM_ECLIPSE_TO_PYTHON)
            pydevd.settrace('host.docker.internal')
    execute_from_command_line(sys.argv)

