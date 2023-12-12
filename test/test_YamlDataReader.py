import pytest

from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:

    @pytest.fixture()
    def yaml_file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = """
        - student1:
            math: 90
            english: 85
        - student2:
            math: 75
            history: 92
        """
        data = {
            "student1": [("math", 90), ("english", 85)],
            "student2": [("math", 75), ("history", 92)]
        }
        return yaml_content, data

    @pytest.fixture()
    def filepath_and_data(self, yaml_file_and_data_content: tuple[str, DataType], tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(yaml_file_and_data_content[0], encoding='utf-8')
        return str(p), yaml_file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        yaml_reader = YamlDataReader()
        file_content = yaml_reader.read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
