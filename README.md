Jarvis – AI Voice Assistant 🤖
Jarvis is a personal AI assistant built in Python that listens to your voice, responds intelligently, performs web searches, plays media, and interacts using Google's Generative AI. This project combines speech recognition, text-to-speech, web automation, YouTube & image search, and AI-based chat into a single, powerful assistant.
🚀 Features
Voice Activation: Say "Jarvis" to activate the assistant.
Voice Recognition: Uses speech_recognition to understand natural language commands.
Text-to-Speech: Responds using pyttsx3 for a natural voice assistant experience.
Web Automation: Automatically opens websites like Google, YouTube, Pinterest, Facebook, Amazon, and more.
YouTube & Media Control: Search and play YouTube videos or music directly by voice.
Image Search: Search for images on Google using voice commands.
AI Chat Assistant: Uses Google Generative AI (gemini-1.5-flash) to answer questions intelligently.
Extensible Commands: Easily add new voice commands and actions.
📂 Project Structure
123456789
🛠️ Installation
Clone the repository:
bash
12
Install dependencies:
bash
1
Configure API keys:
Create the following files in the project root and add your credentials:
youtube_api → Your YouTube Data API key
api_key → Your Google Custom Search API key
search_engine_id → Your Google Custom Search Engine ID
Hardware requirement:
Ensure your microphone is connected and working.
💻 Usage
Run the assistant:
bash
1
Activate Jarvis:
Say "Jarvis" to start giving commands.
Example voice commands:
Command Type
Example Phrases
Open websites
"open Google", "open YouTube", "open Facebook"
Play media
"play Yah Dunya", "play Jhol"
Search images
"search for a sunset"
AI chat
Ask any question after activation – Jarvis will answer using Google Generative AI
🔧 How It Works
🎤 Speech Recognition
Listens continuously via the microphone.
Detects the keyword "Jarvis" to activate command mode.
🧠 Command Parsing
Uses Python string matching and numpy.char.lower to detect and categorize commands.
🌐 Web & Media Actions
Opens URLs in your default browser using the webbrowser module.
Plays YouTube videos or searches images using YouTube API & Google Custom Search API.
🤖 AI Responses
Integrates with google.generativeai (Gemini 1.5 Flash) for natural language understanding.
Outputs responses via text-to-speech using pyttsx3.
⚡ Dependencies
Add these to your requirements.txt:
txt
123456789
Install all at once:
bash
1
🎨 Customization
Add new websites/commands: Extend the command logic in jarvis.py.
Add media URLs: Update names_of_audio.py with new pre-defined media links.
Adjust sensitivity: Modify recognizer.adjust_for_ambient_noise(source) to fine-tune speech recognition.
Change wake word: Update the activation keyword detection logic as needed.
🖼️ Screenshots / Demo
(Optional: Add screenshots or GIFs of Jarvis in action to showcase your project)
Example placeholder:
1
⚖️ License
This project is open-source. You are free to modify, reuse, or improve it for personal or educational projects.
12345
📫 Contact
GitHub: iamHammadA
Instagram: @iamHammadA
✅ Pro Tip: Save this file as README.md in your project root, then commit and push to GitHub:
bash
123
Built with ❤️ by Hammad | Empowering voice-first AI interactions 🎙️✨
write in a format that i can copy paste

Thinking completed
markdown
123456789101112131415161718192021
Jarvis/
│
├── jarvis.py # Main script
├── names_of_audio.py # Stores URLs for media commands
├── youtube_api # File containing YouTube API key
├── api_key # File containing Google API key
├── search_engine_id # File containing Google Custom Search Engine ID
├── requirements.txt # Python dependencies
└── README.md # Project documentation
123456789
Install dependencies:
bash
1
Configure API keys:
Create the following files in the project root and add your credentials:
youtube_api → Your YouTube Data API key
api_key → Your Google Custom Search API key
search_engine_id → Your Google Custom Search Engine ID
Hardware requirement:
Ensure your microphone is connected and working.
💻 Usage
Run the assistant:
bash
1
Activate Jarvis:
Say "Jarvis" to start giving commands.
Example voice commands:
Command Type
Example Phrases
Open websites
"open Google", "open YouTube", "open Facebook"
Play media
"play Yah Dunya", "play Jhol"
Search images
"search for a sunset"
AI chat
Ask any question after activation – Jarvis will answer using Google Generative AI
🔧 How It Works
🎤 Speech Recognition
Listens continuously via the microphone.
Detects the keyword "Jarvis" to activate command mode.
🧠 Command Parsing
Uses Python string matching and numpy.char.lower to detect and categorize commands.
🌐 Web & Media Actions
Opens URLs in your default browser using the webbrowser module.
Plays YouTube videos or searches images using YouTube API & Google Custom Search API.
🤖 AI Responses
Integrates with google.generativeai (Gemini 1.5 Flash) for natural language understanding.
Outputs responses via text-to-speech using pyttsx3.
⚡ Dependencies
Add these to your requirements.txt:
txt
123456789
Install all at once:
bash
1
🎨 Customization
Add new websites/commands: Extend the command logic in jarvis.py.
Add media URLs: Update names_of_audio.py with new pre-defined media links.
Adjust sensitivity: Modify recognizer.adjust_for_ambient_noise(source) to fine-tune speech recognition.
Change wake word: Update the activation keyword detection logic as needed.
🖼️ Screenshots / Demo
(Optional: Add screenshots or GIFs of Jarvis in action to showcase your project)
Example placeholder:
1
⚖️ License
This project is open-source. You are free to modify, reuse, or improve it for personal or educational projects.
12345
📫 Contact
GitHub: iamHammadA
Instagram: @iamHammadA
✅ Pro Tip: Save this file as README.md in your project root, then commit and push to GitHub:
bash
123
Built with ❤️ by Hammad | Empowering voice-first AI interactions 🎙️✨
```
