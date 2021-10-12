import argparse
import os
from VeronikaPotseichukSerializer import *
import configparser  

parser = argparse.ArgumentParser()


parser.add_argument('-c',
                    '--config',
                    metavar='config',
                    action='store',
                    type=str,
                    required=False,
                    help='config file')

parser.add_argument('-p',
                    '--path',
                    metavar='path',
                    action='store',
                    type=str,
                    required=False,
                    help='from file')

parser.add_argument('-l',
                    '--language',
                    metavar='language',
                    action='store',
                    choices=['json', 'yaml', 'pickle', 'toml'],
                    type=str,
                    required=False,
                    help='to language')

args = parser.parse_args()



if args.config is not None:
     if not os.path.isfile(args.config):
          print("Config file {} not exist".format(args.config))
          exit(1)
     try:
          config = configparser.ConfigParser()
          config.read(args.config)     
          file_path = config['target_file']['file']
          language = config['target_language']['language']
          
          if language not in ['json', 'yaml', 'toml', 'pickle']:
               print('Invalid language.')
               exit(1)

     except:   
          print("Error parce config file!")
          exit(1)

elif args.path is not None and args.language is not None:
     file_path = args.path
     language = args.language
else:
     print("Error arguments")
     exit(1)

if not os.path.isabs(file_path):
     path = os.path.join(os.getcwd(), file_path)
     new_file_name, extension = os.path.splitext(file_path)

extension = extension[1:]

if extension not in ['json', 'yaml', 'toml', 'pickle']:
     print('Invalid file extension.')
     exit(1)

if extension == language:
     print('the same format.')
     exit(1)

with open(path, 'r') as source_fp:
     source_serializer = create_serializer(extension)
     obj = source_serializer.load(source_fp)

new_file_name += '.' + language 

with open(new_file_name, 'w') as target_fp:
    target_serializer = create_serializer(language)

    target_serializer.dump(obj=obj, fp=target_fp)

print('Done')