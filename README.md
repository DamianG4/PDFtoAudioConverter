# PDF to Audio

Skrypt w języku Python wykorzystujący sztuczną inteligencję do zamiany dokumentów PDF na audiobooki w formacie MP3 przy użyciu Google Cloud Text-to-Speech API.

## Aplikacja online
Wersja live: [LINK](https://react-weather-app-kappa-navy.vercel.app)

## Funkcje
- **Ekstrakcja tekstu:** automatyczne odczytywanie treści z wielostronicowych plików PDF za pomocą biblioteki `pypdf`.
- **Konwersja mowy (TTS):** integracja z zaawansowanymi modelami Google dla uzyskania naturalnego brzmienia.
- **Zapis audio:** generowanie plików MP3 z obsługą odpowiedzi binarnych (Base64) z API.
- **Bezpieczeństwo:** pełna separacja kluczy API od kodu źródłowego przy użyciu zmiennych środowiskowych.

## Technologie
- Python 3.x
- Google Cloud Text-to-Speech API
- pypdf
- python-dotenv
- Requests
- Git / GitHub

## Instalacja i uruchomienie

1. Sklonuj repozytorium na swoj dysk:

   ```git clone https://github.com/DamianG4/PDFtoAudioConverter```

2. Wejdz do folderu projektu:

   ```cd PDFtoAudio```

3. Zainstaluj wymagane biblioteki:

   ```pip install -r requirements.txt```

4. Skonfiguruj klucz API:
   - Stworz plik .env w glownym folderze projektu.
   - Dodaj w nim linijke:

    ```GOOGLE_CLOUD_API_KEY=TWOJ_KLUCZ_API```

5. Przygotuj plik PDF:
   - Umieść plik PDF, który chcesz przekonwertować, w głównym folderze projektu.
   - Zmień jego nazwę na sample.pdf

6. Uruchom skrypt:

   ```python main.py```
   
