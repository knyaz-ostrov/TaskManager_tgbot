import json



class GetJSON:
    def __init__(self, path) -> None:
        data = None
        with open(path, 'r') as file:
            data = json.load(file)
        self.data = data