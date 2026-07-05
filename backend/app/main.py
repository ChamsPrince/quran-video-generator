from services.data_service import DataService


def main():
    data_service = DataService()

    surah = data_service.get_surah(114)

    print("=" * 40)
    print("SURAH DETAIL")
    print("=" * 40)

    print(f"Number      : {surah['number']}")
    print(f"Arabic      : {surah['name_ar']}")
    print(f"Latin       : {surah['name_en']}")
    print(f"Meaning     : {surah['translation_id']}")
    print(f"Revelation  : {surah['revelation']}")
    print(f"Ayah Count  : {surah['ayah_count']}")


if __name__ == "__main__":
    main()