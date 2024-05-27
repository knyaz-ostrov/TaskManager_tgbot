import lxml.etree as ET



class GetXML:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.__get_data()

    def __get_data(self):
        self.data = ET.parse(self.file_path)

    def get_item(self, item_path) -> str:
        item = self.data.xpath(item_path)[0].text
        return item