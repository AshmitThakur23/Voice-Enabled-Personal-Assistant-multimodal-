# Voice‑Enabled Personal Assistant (Multimodal) 🗣️🤖✨

[![Repo](https://img.shields.io/badge/GitHub-AshmitThakur23%2FVoice--Enabled--Personal--Assistant--multimodal---181717?logo=github)](https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-)
![Made with Python](https://img.shields.io/badge/Made%20with-Python%20100%25-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#-license)

A production‑minded, multimodal AI assistant with three integrated modules:
- 💬 Gemini API Chatbot for intelligent conversations
- 🌦️ Voice Weather Assistant using Gemini + OpenWeather for live updates
- 🧠 “Jarvis” Personal Assistant to play music, open apps, and fetch info via voice commands

Designed with reliability, extensibility, and recruiter‑friendly clarity in mind. Perfect to demonstrate LLM integration, voice pipelines, API composition, and systems design.

---

## ✨ Highlights

- Multimodal interface: seamless text + voice workflows
- Robust voice I/O: wake‑word style usage, TTS, and configurable mic input
- Real‑time weather: Gemini reasoning + OpenWeather data fusion
- Action engine: play music, open apps, search web, fetch knowledge
- Extensible command registry: add new skills in minutes
- Clean architecture: modular separation of concerns for maintainability

---

## 🗺️ Table of Contents

- [Demo](#-demo)
- [Architecture](#-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Quality, Testing, and Reliability](#-quality-testing-and-reliability)
- [Roadmap](#-roadmap)
- [FAQ / Troubleshooting](#-faq--troubleshooting)
- [Why This Project (for Recruiters/Reviewers)](#-why-this-project-for-recruitersreviewers)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎥 Demo

Note: GitHub sometimes doesn’t play videos inline in README due to HTML sanitization/CSP. If a player doesn’t appear, use the “Download the video” links below each section.

### 1) First Chatbot (Text Q&A)
<video src="https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/first%20chatbot.mp4" controls width="720"></video>

[Download the video](https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/first%20chatbot.mp4)

---

### 2) Both Chatbots (Combined)
<video src="https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/attached%20both%20chatbot.mp4" controls width="720"></video>

[Download the video](https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/attached%20both%20chatbot.mp4)

---

### 3) Jarvis Personal Assistance (Play music / Open apps / Fetch info)
<video src="https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/jarvis%20personal%20assistance.mp4" controls width="720"></video>

[Download the video](https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-/raw/main/jarvis%20personal%20assistance.mp4)

## 🧱 Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                            User Interface                          │
│                      (Text CLI / Voice Input)                      │
└───────────────▲───────────────────────┬─────────────────────────────┘
                │                       │
                │                       │
        Speech Capture              Text Input
         + STT (ASR)                    │
                │                       │
                └───────────────┬───────┘
                                ▼
                      Intent Router / Orchestrator
                    (Command registry + skill router)
                  /            |               \
                 /             |                \
                ▼              ▼                 ▼
        Gemini Chat       Weather Skill     Jarvis Assistant
       (google-genai)   (OpenWeather + LLM) (Apps, Music, Web)
                 \             |                /
                  \            |               /
                   └──────────▼──────────────┘
                               │
                         Response Builder
                          + TTS (pyttsx3)
                               ▼
                          Spoken Output
```

Design goals:
- Decoupled skills for easy additions
- Network‑safe (timeouts, retries)
- Observable (structured logs)
- Configurable via environment

---

## ✅ Features

- Gemini‑powered chat and reasoning
- Live weather with OpenWeather (city/coordinates configurable)
- Voice commands for:
  - “What’s the weather in London?”
  - “Play lo‑fi beats”
  - “Open Chrome/VS Code/Calculator”
  - “Search Wikipedia for Alan Turing”
- Offline TTS via `pyttsx3` (works without cloud TTS)
- Cross‑platform Python (Windows/macOS/Linux)
- Error‑tolerant: input validation, API fallback, timeouts

---

## 🧰 Tech Stack

- Language: Python (100%)
- LLM: Google Gemini (via `google-generativeai`)
- Weather: OpenWeather REST API
- Voice I/O: `SpeechRecognition`, `PyAudio`, `pyttsx3` (TTS)
- Utilities: `requests`, `platform`, `subprocess`, `playsound`/`pydub` (optional)
- CLI/UX: standard Python CLI with rich logging

---

## 🚀 Quick Start

1) Prerequisites
- Python 3.9+ recommended
- A working microphone and speakers
- API keys:
  - Gemini: https://ai.google.dev/
  - OpenWeather: https://openweathermap.org/api
- System packages:
  - PortAudio (for PyAudio)
    - macOS: `brew install portaudio`
    - Ubuntu/Debian: `sudo apt-get install portaudio19-dev`
    - Windows: install PyAudio wheel if needed (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

2) Clone
```bash
git clone https://github.com/AshmitThakur23/Voice-Enabled-Personal-Assistant-multimodal-.git
cd Voice-Enabled-Personal-Assistant-multimodal-
```

3) Create virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

4) Install dependencies
```bash
# If requirements.txt exists:
pip install -r requirements.txt

# Otherwise, install common deps used by this project:
pip install google-generativeai SpeechRecognition PyAudio pyttsx3 requests python-dotenv playsound
```

5) Configure environment
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_key_here
OPENWEATHER_API_KEY=your_openweather_key_here
OPENWEATHER_UNITS=metric   # or imperial
DEFAULT_CITY=London
VOICE_RATE=180             # optional, pyttsx3 rate
VOICE_VOLUME=1.0           # 0.0–1.0
```

6) Run modules
```bash
# 1) Gemini Chatbot (text)
python chatbot.py

# 2) Voice Weather Assistant
python weather_voice.py

# 3) Jarvis Personal Assistant
python jarvis.py
```

Note: If your entry point scripts live in a subfolder (e.g., `src/`), adjust the paths accordingly:
```bash
python src/chatbot.py
python src/weather_voice.py
python src/jarvis.py
```

---

## ⚙️ Configuration

- Environment variables (via `.env` or shell):
  - `GEMINI_API_KEY`: Google Gemini key
  - `OPENWEATHER_API_KEY`: OpenWeather key
  - `OPENWEATHER_UNITS`: `metric` or `imperial`
  - `DEFAULT_CITY`: default fallback city for weather
  - `VOICE_RATE`, `VOICE_VOLUME`: TTS preferences
- Microphone device index:
  - If multiple mics, allow a `MIC_DEVICE_INDEX` env var and pass into your STT initializer.

Example Python snippet for TTS:
```python
import pyttsx3

def speak(text: str, rate: int = 180, volume: float = 1.0):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.say(text)
    engine.runAndWait()
```

Example for OpenWeather:
```python
import os, requests

def get_weather(city: str):
    key = os.getenv("OPENWEATHER_API_KEY")
    units = os.getenv("OPENWEATHER_UNITS", "metric")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={units}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()
```

---

## 🧑‍💻 Usage

- Voice Weather
  - “What’s the weather right now?”
  - “Weather in New York”
  - “Do I need an umbrella today?”

- Jarvis Commands
  - “Play lo‑fi beats”
  - “Open Chrome”
  - “Search Wikipedia for ‘Generative AI’”
  - “What’s the time?”

- Chatbot
  - Free‑form prompts via CLI
  - Example:
    ```
    You: Summarize the latest AI research trends in 3 bullets.
    Bot: ...
    ```

---

## 🗂️ Project Structure

This is a reference layout. Align it with how your repository is organized.

```
.
├── chatbot.py                 # Gemini text chatbot
├── weather_voice.py           # Voice + weather module (Gemini + OpenWeather)
├── jarvis.py                  # Personal assistant (apps, music, info)
├── utils/                     # Shared helpers: audio, TTS, STT, prompts, logging
├── requirements.txt           # Python dependencies (if present)
├── README.md                  # This file
└── .env.example               # Example environment configuration (optional)
```

---

## 🧪 Quality, Testing, and Reliability

- Network safety:
  - Timeouts on all HTTP requests (e.g., 10s)
  - Retry with exponential backoff for transient failures (HTTP 429/5xx)
- Input validation:
  - Sanitize voice/text inputs before executing any system commands
- Logging & Observability:
  - Structured logs with module, severity, and timestamps
- Tests (suggested):
  - Unit tests for parsers, intent router, weather formatter
  - Mock LLM + HTTP with fixtures
  - Device‑independent tests for command registry

Example pytest skeleton:
```python
def test_intent_router_weather():
    text = "What's the weather in Delhi?"
    intent, args = route(text)
    assert intent == "weather"
    assert "Delhi" in args.values()
```

---

## 🧭 Roadmap

- Wake word detection for hands‑free activation
- Streaming STT and low‑latency TTS
- Multilingual support (ASR + TTS)
- Skills marketplace: plug‑and‑play commands
- Dockerized local dev and deployment
- Desktop tray app / minimal GUI

---

## ❓ FAQ / Troubleshooting

- PyAudio install fails
  - macOS: `brew install portaudio && pip install pyaudio`
  - Ubuntu/Debian: `sudo apt-get install portaudio19-dev && pip install pyaudio`
  - Windows: install a matching wheel from Gohlke

- Mic not detected / wrong device
  - Enumerate devices via `pyaudio.PyAudio().get_device_info_by_index(i)`
  - Set `MIC_DEVICE_INDEX` and pass it to your recognizer

- TTS is too fast/slow or quiet
  - Adjust `VOICE_RATE` and `VOICE_VOLUME` in `.env`

- OpenWeather errors (401/404)
  - Verify `OPENWEATHER_API_KEY`, city name, and units

- Gemini rate limit
  - Implement retry/backoff and modest request cadence

---

## 💼 Why This Project 

- Real‑world systems thinking: multimodal pipeline with clear boundaries
- LLM + external API composition: Gemini reasoning grounded with OpenWeather data
- Platform awareness: audio device handling across OSes
- Safety & reliability: timeouts, retries, and input validation
- Extensible design: command registry + modular skills
- Developer experience: clean CLI, env‑driven config, clear docs

If you’d like a quick walkthrough, start with:
1) `jarvis.py` – command registry and action execution
2) `weather_voice.py` – STT/TTS loop + weather integration
3) `chatbot.py` – Gemini prompt handling and response rendering

---

## 🤝 Contributing

Contributions are welcome!
- Open an issue to discuss major changes
- Keep PRs focused and well‑tested
- Follow conventional commit messages if possible

Recommended setup:
```bash
pip install -r requirements.txt
pip install pytest black isort
black . && isort .
pytest -q
```

---

## 📝 License

Copyright (c) 2026 Ashmit Thakur. All rights reserved.

This repository is provided for educational and reference purposes only.

PERMITTED:

* You may view and download the code for personal learning.
* You may fork this repository on GitHub.
* You may submit issues, suggestions, and pull requests.

RESTRICTIONS:

* You may NOT use this code in any personal, academic, or commercial project.
* You may NOT publish, distribute, or re-upload this code (in whole or in part).
* You may NOT use this code to build or showcase your own applications.
* You may NOT claim this code as your own work.

ATTRIBUTION:
If you are explicitly permitted to share any part of this code, you must give clear credit at the beginning:

"Original code by Ashmit Thakur (2026)"

NO LICENSE:
Only the permissions listed above are allowed. Any other use is strictly prohibited.

ENFORCEMENT:
If you violate these terms, the copyright holder may take appropriate legal action.


---

## 🙏 Acknowledgments

- Google Gemini (google‑generativeai)
- OpenWeather
- Python SpeechRecognition, PyAudio, pyttsx3
- The open‑source community ❤️

---
