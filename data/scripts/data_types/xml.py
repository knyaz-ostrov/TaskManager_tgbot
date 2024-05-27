import lxml.etree as ET



class XML:
    def __init__(self, file_path: str) -> None:
        self.__get_data(file_path)

    def __get_data(self, file_path: str) -> None:
        self.data = ET.parse(file_path)

    def get_item(self, category: str, filter_value: str) -> str:
        path = f'.//{category}[@id=""]'
        path = path.replace('""', f'"{filter_value}"')
        item = self.data.xpath(path)[0].text
        return item