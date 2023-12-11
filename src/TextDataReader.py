# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DataReader import DataReader
import yaml

class TextDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                if not line.startswith(" "):
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    subj, score = line.split(":", maxsplit=1)
                    self.students[self.key].append(
                    (subj.strip(), int(score.strip())))
        return self.students

    def read_from_yaml(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)

        for entry in yaml_data:
            self.key = list(entry.keys())[0]
            self.students[self.key] = []
            for subject, score in entry[self.key].items():
                self.students[self.key].append((subject.strip(), int(score)))
        return self.students