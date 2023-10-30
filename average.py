from json import loads
def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    f=loads(open(file_path).read())
    sum=0
    for i in f.values():
        sum+=i
    return sum/len(f)
# test
file_path = 'data.json'
print(average_expenses(file_path))
