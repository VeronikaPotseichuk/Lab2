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

extension = extension[1:]

if extension not in ['json', 'yaml', 'toml', 'pickle']:
     print('Invalid file extension.')
     exit(1)

if extension == args.language:
     print('the same format.')
     exit(1)

with open(path, 'r') as source_fp:
     source_serializer = create_serializer(extension)
     obj = source_serializer.load(source_fp)

new_file_name += '.' + args.language 

with open(new_file_name, 'w') as target_fp:
    target_serializer = create_serializer(args.language)

    target_serializer.dump(obj=obj, fp=target_fp)

print('Done')