import pytest
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


class TestYAMLDataReader:
    @pytest.fixture()
    def yaml_content_and_data(self) -> tuple[str, DataType]:
        yaml_text = "- Иванов Иван Иванович:\n" + \
                    "    математика: 67\n" + \
                    "    литература: 100\n" + \
                    "    программирование: 91\n" + \
                    "- Петров Петр Петрович:\n" + \
                    "    математика: 78\n" + \
                    "    химия: 87\n" + \
                    "    социология: 61\n"
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return yaml_text, data

    @pytest.fixture()
    def yaml_filepath_and_data(self, yaml_content_and_data: tuple[str, DataType], tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(yaml_content_and_data[0], encoding='utf-8')
        return str(p), yaml_content_and_data[1]

    def test_read(self, yaml_filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(yaml_filepath_and_data[0])
        assert file_content == yaml_filepath_and_data[1]
