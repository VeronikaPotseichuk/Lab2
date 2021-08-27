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

j_conv = create_serializer('json') 

obj = {'a':1,'b':3, 'c':[1,2]}

s = j_conv.dump(obj)
print(s)
obj2 = j_conv.load(s)
print(obj2)
if(obj2 == obj):
      print("coool json")
else:
     print("NOOOOOOO json")


p_conv = create_serializer('pickle')

s = p_conv.dump(obj)
print(s)
obj2 = p_conv.load(s)
print(obj2)
if(obj2 == obj):
     print("coool pickle")
else:
     print("NOOOOOOO pickle")
