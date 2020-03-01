import yaml
with open('categories.yaml') as file1:
    cat = yaml.full_load(file1)
    
    for item, doc in cat.items():
        print(item, ":", doc)