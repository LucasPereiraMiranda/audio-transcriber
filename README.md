<h1 align="center"> Audio Transcriber </h1>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/LucasPereiraMiranda/audio-transcriber">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/LucasPereiraMiranda/audio-transcriber">
  
  <a href="https://github.com/LucasPereiraMiranda/audio-transcriber/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/LucasPereiraMiranda/audio-transcriber">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/audio-transcriber/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/LucasPereiraMiranda/audio-transcriber">
  </a>

  <a href="https://github.com/LucasPereiraMiranda/audio-transcriber/issues">
    <img alt="GitHub license" src="https://img.shields.io/github/license/LucasPereiraMiranda/audio-transcriber">
  </a>
</p>

## 💻 Objectives

A helper tool for transcribing speech to text using Speech Recognition.
For analysis, we can input an MP3 file and receive the transcribed text in the target language.

### Execution preview:

<div align="center">
  <img src=".github/img/execution-preview.png" alt="Execution preview">
</div>

## 🚀 Techs

The analysis is being performed with the following technologies:

- [Python3](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

## :boom: How to run the application?


- With python3 & virtualenv already installed, we can activate the virtual environment by running:

```shell
  python3 -m venv venv
  source venv/bin/activate
```

- We can install requirements.txt dependencies:

```shell
  pip install -r requirements.txt
```

- After defining the contents of the lists in the `audio.mp3` file and selecting the target language, as mentioned above:

<div align="center">
  <img src=".github/img/definitions.png" alt="Definitions">
</div>


 we can run:

```shell
  python src/handle.py
```

- After this, we will receive the transcription in the `transcription.txt` file at the root directory, as mentioned above:


<div align="center">
  <img src=".github/img/transcription-file-preview.png" alt="Definitions">
</div>

### License

[MIT](https://choosealicense.com/licenses/mit/)
