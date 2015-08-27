
import yaml
import json

from pprint import pprint

with open('my_list.yml') as f:
        new_yaml_list = yaml.load(f)

pprint(new_yaml_list)

with open('my_list.json') as g:
        new_json_list = json.load(g)

pprint(new_json_list)

