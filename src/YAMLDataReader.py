from typing import Dict, List, Tuple
from DataReader import DataReader
import yaml


class YAMLDataReader(DataReader):
    def read(self, path: str) -> Dict[str, List[Tuple[str, int]]]:
        data = {}
        with open(path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
            for entry in yaml_data:
                if isinstance(entry, dict):
                    for name, subjects in entry.items():
                        scores = [(subj, score)
                                  for subj, score in subjects.items()]
                        data[name] = scores
        return data
