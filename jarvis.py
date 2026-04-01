import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
from numpy.core.defchararray import lower
import pytube
import cv2
import mediapipe as mp
import winsound
import math



from tensorflow.python.ops.gen_array_ops import lower_bound
import requests
from bs4 import BeautifulSoup

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()
r = sr.Recognizer()

# Function to recognize speech from the microphone
def recognize_speech_from_mic():
    # Ensure the microphone is properly accessed and managed
    with (sr.Microphone() as source):
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Ready to recognize speech. Speak into the microphone.")

        while True:
            try:
                print("Listening...")
                audio_data = recognizer.listen(source, timeout=2)  # Adjust timeout as needed
                text = recognizer.recognize_google(audio_data)
                print(f"you said {text}")


                if "jarvis" in text.lower():
                    print("'jarvis' detected. Activating...")
                    engine.say("You called?")
                    engine.runAndWait()

                    # Listen for the next command after activation
                    print("Listening for command...")
                    engine.runAndWait()
                    engine.say("""Please tell your choice : "
                                                       1. Image
                                                       2. Video
                                                       3. Website""")
                try:
                    print("Listening..." )
                    rate = engine.getProperty('rate')
                    engine.setProperty('rate', rate - 10)
                    a = 0
                    if a == 0:
                        pyttsx3.speak("I am listening")
                        a += 1
                except sr.Microphone:
                    pass
                try:
                        text1 = recognizer.recognize_google(audio_data)
                        a = text1.lower()
                        if 'video' in a:
                            pyttsx3.speak("Please tell the name of the video or song you want to listen")
                            engine.runAndWait()
                            audio = recognizer.listen(source)
                            text2 = recognizer.recognize_google(audio)
                            text3 = text2.lower()
                            API_KEY = open('youtube_api').read()

                            search_query = text3


                            url = 'https://www.googleapis.com/youtube/v3/search'
                            params = {
                                'q' : search_query,
                                'key' : API_KEY,
                                'part' : "snippet",
                                'SearchType' : 'video',
                                'maxresult' : 1
                            }
                        elif 'website' in a:
                                pyttsx3.speak("Please tell the name of the website you want to open")
                                audio = recognizer.listen(source)
                                text2 = recognizer.recognize_google(audio)
                                engine.runAndWait()
                                text3 = text2.lower()
                                API_KEY = open('api_key').read()
                                SEARCH_ENGINE_ID = open('search_engine_id').read()

                                search_query = text3


                                url = 'https://www.googleapis.com/customsearch/v1'
                                params = {
                                    'q' : search_query,
                                    'key' : API_KEY,
                                    'cx' : SEARCH_ENGINE_ID,
                                }

                                response = requests.get(url, params=params)
                                data = response.json()
                                print(data)

                                if 'items' in data:
                                    wb.open(data['items'][0]['link'])

                        elif 'image' in a:
                                    pyttsx3.speak("Please tell the name of the image you want to search")
                                    audio = recognizer.listen(source)
                                    text2 = recognizer.recognize_google(audio)
                                    engine.runAndWait()
                                    text3 = text2.lower()
                                    API_KEY = open('api_key').read()
                                    SEARCH_ENGINE_ID = open('search_engine_id').read()

                                    search_query = text3


                                    url = 'https://www.googleapis.com/customsearch/v1'
                                    params = {
                                        'q' : search_query,
                                        'key' : API_KEY,
                                        'cx' : SEARCH_ENGINE_ID,
                                        'SearchType' : 'image'
                                    }

                                    response = requests.get(url, params=params)
                                    data = response.json()
                                    print(data)
                                    a = 0

                                    for items in data:
                                        if a == 0:
                                            wb.open(data['items'][0]['link'])
                                            a +=1
                                    response = requests.get(url, params=params)
                                    data = response.json()
                                    if 'items' in data and len(data['items']) > 0:
                                        video_id = data['items'][0]['id']['videoId']
                                        wb.open(f"https://www.youtube.com/watch?v={video_id}")
                                    else:
                                        print('No video found.')
                        else:
                            engine = pyttsx3.init()
                            # Ensure the API key is set in the environment variable
                            api_key = "GEMINI_API KEY"  # Replace with your actual API key
                            if not api_key:
                                raise ValueError("API key not found in environment variables.")

                            genai.configure(api_key=api_key)

                            # Create the model configuration
                            generation_config = {
                                "temperature": 1,
                                "top_p": 0.95,
                                "top_k": 40,
                                "max_output_tokens": 8192,
                                "response_mime_type": "text/plain",
                            }

                            # Initialize the generative model
                            model = genai.GenerativeModel(
                                model_name="gemini-1.5-flash",
                                generation_config=generation_config,
                            )

                            # Start a chat session
                            chat_session = model.start_chat(
                                history=[]
                            )

                            # Send a message and receive a response
                            response = chat_session.send_message(text1)
                            with open("file.txt", "w") as f:
                                b = f.write(response.text)
                            with open("file.txt", "r") as f:
                                c = f.read()
                            cou = c.replace("*", "")
                            with open("file.txt", "r") as f:
                                c = f.read()
                            new = cou.replace("#", "")

                            rate = engine.getProperty('rate')
                            engine.setProperty('rate', rate - 12.5)

                            print(new)
                            pyttsx3.speak(new)

                except sr.UnknownValueError:
                    print("Sorry, could not understand the audio.")
                except sr.RequestError as e:
                    print(f"Sorry, there was an error with the request: {e}")
                except sr.WaitTimeoutError:
                    print("Listening timed out while waiting for phrase to start.")
                except:
                    pass
            except:
                pass

# Main execution
if __name__ == "__main__":
    try:
        recognize_speech_from_mic()
    except KeyboardInterrupt:
        print("Stopped.")
