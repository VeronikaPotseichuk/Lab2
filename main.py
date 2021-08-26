import argparse
import os

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

print(args.path)
print(args.language)