from json import loads
def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    f=loads(open(file_path).read())
    return f
file_path='data.json'
print(get_data(file_path))

