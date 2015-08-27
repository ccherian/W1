
import yaml
import json

my_list = range(8)
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.20'
my_list[-1]['model'] = 'cisco'

with open('my_list.yml', 'w') as f:
     f.write(yaml.dump(my_list, default_flow_style=False))

with open('my_list.json', 'w') as g:
     json.dump(my_list, g)

