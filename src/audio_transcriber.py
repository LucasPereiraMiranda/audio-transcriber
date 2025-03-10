import speech_recognition as sr
from pydub import AudioSegment
import os
import sys
import logging

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class AudioTranscriber:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.wav_path = None

    def convert_mp3_to_wav(self) -> str:
        if not self.file_path.lower().endswith(".mp3"):
            raise ValueError("Only MP3 files are supported.")

        self.wav_path = os.path.splitext(self.file_path)[0] + ".wav"
        
        try:
            audio = AudioSegment.from_mp3(self.file_path)
            audio.export(self.wav_path, format="wav")
            logging.info(f"Converted to WAV: {self.wav_path}")
            return self.wav_path
        except Exception as e:
            raise RuntimeError(f"Failed to convert MP3 to WAV: {e}")

    def transcribe_audio(self, language="pt-BR") -> str:
        if not self.wav_path:
            raise ValueError("No WAV file available. Convert MP3 to WAV first.")

        if not os.path.exists(self.wav_path):
            raise FileNotFoundError(f"WAV file not found: {self.wav_path}")

        recognizer = sr.Recognizer()

        try:
            with sr.AudioFile(self.wav_path) as source:
                logging.info("Processing audio...")
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language=language)
                logging.info("Transcription successful.")

                with open("transcription.txt", "w", encoding="utf-8") as file:
                    file.write(text)
                    logging.info("Transcription saved to transcription.txt.")

                return text
        except sr.UnknownValueError:
            raise RuntimeError("Could not understand the audio.")
        except sr.RequestError:
            raise RuntimeError("Error connecting to the speech recognition service.")
