import requests
import base64
import os
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

PDF_FILE_PATH = "sample.pdf"
OUTPUT_AUDIO_FILE = "audio.mp3"

API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY")

if not API_KEY:
    raise ValueError("Brak klucza API.")

URL = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"


def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text.replace('\n', ' ') + " "
        return extracted_text.strip()
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{pdf_path}'.")
        return None
    except Exception as e:
        print(f"Wystąpił błąd podczas czytania PDF: {e}")
        return None


def convert_text_to_speech(text, output_file):
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    text_to_process = text[:5000]

    data = {
        "input": {
            "text": text_to_process
        },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-Journey-F"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    }

    print("Łączenie z API Google Cloud Text-to-Speech...")
    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        audio_content = response.json().get("audioContent")
        with open(output_file, "wb") as out:
            out.write(base64.b64decode(audio_content))
        print(f"Sukces! Twój audiobook został zapisany jako: {output_file}")
    else:
        print(f"Błąd API (Kod {response.status_code}):")
        print(response.text)


if __name__ == "__main__":
    print(f"Ekstrahowanie tekstu z pliku {PDF_FILE_PATH}...")
    pdf_text = extract_text_from_pdf(PDF_FILE_PATH)

    if pdf_text:
        convert_text_to_speech(pdf_text, OUTPUT_AUDIO_FILE)
    else:
        print("Proces przerwany. Brak tekstu do przetworzenia.")