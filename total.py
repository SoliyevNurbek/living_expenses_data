import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f=json.loads(open(file_path).read())
    sum=0
    for i in f.values():
        sum+=i
    return sum

# test
file_path = "data.json"
print(total_expenses(file_path))
