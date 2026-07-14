import requests

class QuranService:
    """
    Service responsible for retrieving Quran text.
    """

    BASE_URL = "https://api.alquran.cloud/v1"

    def get_surah(self, surah_number: int):
        url = f"{self.BASE_URL}/surah/{surah_number}"

        response = requests.get(url)

        return response.json()

    def get_ayahs(self, surah_number: int, start_ayah: int, end_ayah: int):
        pass