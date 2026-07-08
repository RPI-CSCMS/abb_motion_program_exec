import argparse
import os
from .project_setup import project_setup

def func_example(args):
    print("example test {}".format(args.example))

parser = argparse.ArgumentParser(description="abb_motion_program_exec help")
subparsers = parser.add_subparsers(dest="command",required=True)

# project setup command
setup_parser = subparsers.add_parser("setup", help="Set up a new project for use with abb_motion_program_exec")
setup_parser.add_argument("project", help="Name of project to configure")
setup_parser.add_argument("-e","--egm", action="store_true", help="Use Externally Guided Motion")
setup_parser.add_argument("-d","--dir", metavar="directory", action="store", help="Directory of project if not in default location")
setup_parser.add_argument("-i","--inplace", action="store_true", help="Use this option if script is run within project directory. If used, the project name and argument -d are ignored; however, a project name must still be given")
setup_parser.set_defaults(func=project_setup)

# copy example project
#setup_parser = subparsers.add_parser("example", help="Run an example from the abb_motion_program_exec repository")
#setup_parser.add_argument("example", help="Name of example to run")
#setup_parser.add_argument("-a","--address", action="store", default="127.0.0.1", help="Set the ip address of the target other than default (default: 127.0.0.1)")
#setup_parser.add_argument("-p","--port", action="store", default="80", help="Set the port of the target other than default (default: 80). This may alternatively be set by the -a option")
#setup_parser.set_defaults(func=func_example)

args = parser.parse_args()
args.func(args)


