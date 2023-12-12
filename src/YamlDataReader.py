import yaml

from src.DataReader import DataReader
from src.Types import DataType


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)

        for entry in yaml_data:
            self.key = list(entry.keys())[0]
            self.students[self.key] = []
            for subject, score in entry[self.key].items():
                self.students[self.key].append((subject.strip(), int(score)))
        return self.students

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}
