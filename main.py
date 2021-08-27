import argparse
import os
from converters import *

parser = argparse.ArgumentParser()

parser.add_argument('-p',
                    '--path',
                    metavar='path',
                    action='store',
                    type=str,
                    required=True,
                    help='from file')

parser.add_argument('-l',
                    '--language',
                    metavar='language',
                    action='store',
                    choices=['json', 'yaml', 'pickle', 'toml'],
                    type=str,
                    required=True,
                    help='to language')

args = parser.parse_args()


if not os.path.isabs(args.path):
     path = os.path.join(os.getcwd(), args.path)
     new_file_name, extension = os.path.splitext(args.path)

create_serializer(extension[1:]) 
create_serializer(args.language)