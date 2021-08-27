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

t_conv = create_serializer('toml') 

obj = {'a':1,'b':3, 'c':[1,2]}

s = t_conv.dump(obj)
print(s)
obj2 = t_conv.load(s)
print(obj2)
if(obj2 == obj):
     print("coool toml")
else:
     print("NOOOOOOO toml")

