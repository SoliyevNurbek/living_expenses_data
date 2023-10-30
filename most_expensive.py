import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f=json.loads(open(file_path).read())
    min1=-956212321252
    for i in f.values():
        if i>min1:
            min1=i
    return min1

# test
file_path = "data.json"
print(most_expensive(file_path))