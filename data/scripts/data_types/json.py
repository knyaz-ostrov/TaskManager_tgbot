import json



class JSON:
    def __init__(self, file_path: str) -> None:
        self.__get_data(file_path)

    def __get_data(self, file_path: str) -> None:
        with open(file_path) as file:
            self.data = json.load(file)

    def get_item(self, category: str, item_key: str) -> str:
        item = self.data[category][item_key]
        return item