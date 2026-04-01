# Jarvis – AI Voice Assistant 🤖

**Jarvis** is a personal AI assistant built in Python that listens to your voice, responds intelligently, performs web searches, plays media, and interacts using Google's Generative AI. This project combines **speech recognition, text-to-speech, web automation, YouTube & image search, and AI-based chat** into a single, powerful assistant.

---

## 🚀 Features

- **Voice Activation:** Say `"Jarvis"` to activate the assistant.
- **Voice Recognition:** Uses `speech_recognition` to understand natural language commands.
- **Text-to-Speech:** Responds using `pyttsx3` for a natural voice assistant experience.
- **Web Automation:** Automatically opens websites like Google, YouTube, Pinterest, Facebook, Amazon, and more.
- **YouTube & Media Control:** Search and play YouTube videos or music directly by voice.
- **Image Search:** Search for images on Google using voice commands.
- **AI Chat Assistant:** Uses Google Generative AI (`gemini-1.5-flash`) to answer questions intelligently.
- **Extensible Commands:** Easily add new voice commands and actions.

---

## 📂 Project Structure

```
Jarvis/
│
├── jarvis.py                 # Main script
├── names_of_audio.py         # Stores URLs for media commands
├── youtube_api               # File containing YouTube API key
├── api_key                   # File containing Google API key
├── search_engine_id          # File containing Google Custom Search Engine ID
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iamHammadA/Jarvis.git
   cd Jarvis
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys:**  
   Create the following files in the project root and add your credentials:
   - `youtube_api` → Your YouTube Data API key
   - `api_key` → Your Google Custom Search API key
   - `search_engine_id` → Your Google Custom Search Engine ID

4. **Hardware requirement:**  
   Ensure your microphone is connected and working.

---

## 💻 Usage

1. **Run the assistant:**
   ```bash
   python jarvis.py
   ```

2. **Activate Jarvis:**  
   Say `"Jarvis"` to start giving commands.

3. **Example voice commands:**

   | Command Type     | Example Phrases                              |
   |------------------|----------------------------------------------|
   | Open websites    | `"open Google"`, `"open YouTube"`, `"open Facebook"` |
   | Play media       | `"play Yah Dunya"`, `"play Jhol"`            |
   | Search images    | `"search for a sunset"`                      |
   | AI chat          | Ask any question after activation – Jarvis will answer using Google Generative AI |

---

## 🔧 How It Works

### 🎤 Speech Recognition
- Listens continuously via the microphone.
- Detects the keyword `"Jarvis"` to activate command mode.

### 🧠 Command Parsing
- Uses Python string matching and `numpy.char.lower` to detect and categorize commands.

### 🌐 Web & Media Actions
- Opens URLs in your default browser using the `webbrowser` module.
- Plays YouTube videos or searches images using YouTube API & Google Custom Search API.

### 🤖 AI Responses
- Integrates with `google.generativeai` (Gemini 1.5 Flash) for natural language understanding.
- Outputs responses via text-to-speech using `pyttsx3`.

---

## ⚡ Dependencies

Add these to your `requirements.txt`:

```txt
pyttsx3
speechrecognition
requests
beautifulsoup4
pytube
mediapipe
opencv-python
google-generativeai
numpy
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🎨 Customization

- **Add new websites/commands:** Extend the command logic in `jarvis.py`.
- **Add media URLs:** Update `names_of_audio.py` with new pre-defined media links.
- **Adjust sensitivity:** Modify `recognizer.adjust_for_ambient_noise(source)` to fine-tune speech recognition.
- **Change wake word:** Update the activation keyword detection logic as needed.

---

## 🖼️ Screenshots / Demo

> *(Optional: Add screenshots or GIFs of Jarvis in action to showcase your project)*

Example placeholder:
```
[![Jarvis Demo](https://via.placeholder.com/600x400?text=Jarvis+In+Action)](https://your-demo-link)
```

---

## ⚖️ License

This project is open-source. You are free to modify, reuse, or improve it for personal or educational projects.

```
MIT License

Copyright (c) 2026 Hammad

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## 📫 Contact

- **GitHub:** [iamHammadA](https://github.com/iamHammadA)
- **Instagram:** [@iamHammadA](https://instagram.com/iamHammadA)

---

> ✅ **Pro Tip:** Save this file as `README.md` in your project root, then commit and push to GitHub:
>
> ```bash
   git add README.md
   git commit -m "Add detailed professional README"
   git push origin main
   ```

---

*Built with ❤️ by Hammad | Empowering voice-first AI interactions* 🎙️✨r