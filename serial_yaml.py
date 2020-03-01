import yaml
dict_file = [{'sports':['soccer', 'football', 'basketball', 'hockey', 'baseball','cricket','table tennis']}, 
{'countries': ['pakistan','USA','India', 'China','Germany', 'France','Spain']}]

with open('store_yaml_file.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)