import yaml

with open('fruits.yaml') as file:
    fruits_yaml = yaml.load(file, Loader = yaml.FullLoader)
    sort_file = yaml.dump(fruits_yaml, sort_keys = True)
    print(sort_file)