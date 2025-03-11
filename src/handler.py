import os
import logging
import sys
from audio_transcriber import AudioTranscriber

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def handle_audio_transcription(file_path: str, language: str = "pt-BR") -> str | None:
    try:
        transcriber = AudioTranscriber(file_path)
        wav_path = transcriber.convert_mp3_to_wav()

        if not wav_path or not os.path.exists(wav_path):
            logging.error("WAV file was not created successfully.")
            return None

        transcription = transcriber.transcribe_audio(language=language)
        logging.info("Transcription completed successfully.")
        return transcription

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except ValueError as e:
        logging.error(f"Invalid file format: {e}")
    except RuntimeError as e:
        logging.error(f"Processing error: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")

    return None


if __name__ == "__main__":
    mp3_file_path = "./audio.mp3"
    language = "en-US"
    transcription = handle_audio_transcription(mp3_file_path, language)

    if transcription:
        logging.info(f"Transcription output:\n{transcription}")
    else:
        logging.warning("Transcription failed.")
