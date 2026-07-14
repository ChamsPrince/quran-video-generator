from services.quran_service import QuranService


def main():
    quran_service = QuranService()

    surah = quran_service.get_surah(114)

    print(surah)


if __name__ == "__main__":
    main()