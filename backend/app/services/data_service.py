import json
from pathlib import Path


class DataService:
    def __init__(self):
        self.data_path = Path(__file__).parent.parent / "data"

    def get_surahs(self):
        surah_file = self.data_path / "surah.json"

        with open(surah_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_surah(self, number):
        surahs = self.get_surahs()

        for surah in surahs:
            if surah["number"] == number:
                return surah

        return None