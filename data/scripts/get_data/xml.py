import lxml.etree as ET



class GetXML:
    def __init__(self, path) -> None:
        self.data = ET.parse(path)