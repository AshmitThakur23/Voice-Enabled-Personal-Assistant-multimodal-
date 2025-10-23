import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import random
import time
from colorama import init, Fore

# --- Initialize Colorama ---
init()

# (TTS engine is initialized per speak() call to prevent locking issues)

# --- Initialize a single Speech Recognizer (align with main.py behavior) ---
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.7
recognizer.non_speaking_duration = 0.3
recognizer.dynamic_energy_threshold = True

def speak(audio):
    if not audio:
        return
    print(Fore.CYAN + f"Jarvis: {audio}" + Fore.RESET)
    # Reinitialize TTS each call (prevents one-time speak/lock issues)
    try:
        tts = pyttsx3.init()
        voices_local = tts.getProperty('voices')
        # Try to select a female voice similar to main.py behavior
        selected_voice = None
        for v in voices_local:
            name = getattr(v, 'name', '') or ''
            if 'female' in name.lower() or 'zira' in name.lower():
                selected_voice = v.id
                break
        if not selected_voice and voices_local:
            selected_voice = voices_local[1].id if len(voices_local) > 1 else voices_local[0].id
        if selected_voice:
            tts.setProperty('voice', selected_voice)
        tts.setProperty('rate', 180)
        tts.setProperty('volume', 1.0)

        tts.say(audio)
        tts.runAndWait()
        tts.stop()
    except Exception as e:
        print(Fore.RED + f"TTS error: {e}" + Fore.RESET)
    # small pause so mic doesn't capture our own TTS
    time.sleep(0.5)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Ashmit! Hope you slept like a cute teddy bear!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Ashmit! Sending you a big smile right now!")
    else:
        speak("Good Evening, Ashmit! I was waiting for you!")
    speak("I'm your bestie assistant, Jarvis! Tell me, what fun thing are we doing today?")

def random_friend_message():
    messages = [
        "Ashmit, you're seriously the best! Just saying!",
        "I love hanging out with you, Ashmit!",
        "You're doing amazing, don't forget that!",
        "I'm always here for you, bestie!",
        "Sending you positive vibes, Ashmit!",
        "Let's do this together, Ashmit!",
        "I'm here for you, always! 💖",
        "You are amazing, Ashmit! Never forget that!",
        "Sending you good vibes and energy! 🚀",
        "You shine brighter than the stars, Ashmit! ✨"
    ]
    speak(random.choice(messages))

def take_command():
    with sr.Microphone() as source:
        print("Listening... 🎧")
        # brief delay so our TTS doesn't bleed into calibration
        time.sleep(0.2)
        recognizer.adjust_for_ambient_noise(source, duration=1.0)
        try:
            # avoid hanging forever after the first command
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            print("Recognizing your lovely voice... 💬")
            query = recognizer.recognize_google(audio, language='en-in')
            print(Fore.GREEN + f"You said: {query}" + Fore.RESET)
            return query.lower()
        except sr.WaitTimeoutError:
            print(Fore.RED + "Listening timed out, no speech detected." + Fore.RESET)
            return "None"
        except sr.UnknownValueError:
            print(Fore.RED + "Oopsie, I didn't catch that. Could you say it again, please?" + Fore.RESET)
            return "None"
        except sr.RequestError as e:
            print(Fore.RED + f"Hmm, couldn't reach Google services; {e}" + Fore.RESET)
            return "None"

def play_romantic_song_youtube_music():
    romantic_songs = [
        # English Romantic Songs
        "Perfect Ed Sheeran",
        "All of Me John Legend",
        "Thinking Out Loud Ed Sheeran",
        "A Thousand Years Christina Perri",
        "Love Me Like You Do Ellie Goulding",
        "Until I Found You Stephen Sanchez",
        "Photograph Ed Sheeran",
        "Shallow Lady Gaga Bradley Cooper",
        "You Are The Reason Calum Scott",
        "Just the Way You Are Bruno Mars",
        "Say You Won't Let Go James Arthur",
        "If I Can't Have You Shawn Mendes",
        "Can't Help Falling In Love Elvis Presley",
        "Everything Michael Bublé",
        "My Heart Will Go On Celine Dion",
        "Nothing's Gonna Change My Love for You George Benson",

        # Hindi Romantic Songs
        "Tum Hi Ho Aashiqui 2",
        "Raabta Agent Vinod",
        "Tera Ban Jaunga Kabir Singh",
        "Dil Diyan Gallan Tiger Zinda Hai",
        "Jeene Laga Hoon Ramaiya Vastavaiya",
        "Tujh Mein Rab Dikhta Hai Rab Ne Bana Di Jodi",
        "Pee Loon Once Upon A Time In Mumbaai",
        "Sun Saathiya ABCD 2",
        "Khuda Jaane Bachna Ae Haseeno",
        "Hasi Ban Gaye Hamari Adhuri Kahani",
        "Main Rang Sharbaton Ka Phata Poster Nikla Hero",
        "Janam Janam Dilwale",
        "Tum Se Hi Jab We Met",
        "Tera Hone Laga Hoon Ajab Prem Ki Ghazab Kahani",
        "Bekhayali Kabir Singh",
        "Hawayein Jab Harry Met Sejal",
        "Shayad Love Aaj Kal 2",
        "Kaun Tujhe MS Dhoni",
        "Bolna Kapoor and Sons",
        "Raatan Lambiyan Shershaah",
        "Kesariya Brahmastra",
        "Apna Bana Le Bhediya",
        "Heeriye Arijit Singh",
        "Mere Liye Tum Kaafi Ho Shubh Mangal Zyada Saavdhan",
        "Phir Bhi Tumko Chaahunga Half Girlfriend",
        "Tujhe Kitna Chahne Lage Kabir Singh",
        "Ve Maahi Kesari",
        "Pachtaoge Arijit Singh",
        "Agar Tum Saath Ho Tamasha",
        "Khairiyat Chhichhore"
    ]

    song = random.choice(romantic_songs)
    speak(f"Jarvis is playing a sweet romantic song for you: {song} 🎶")
    webbrowser.open(f"https://music.youtube.com/search?q={song}")

    time.sleep(5)  


def main():
    wish_me()
    while True:
        query = take_command()

        if query != "None":
            print(f"Command Received: {query}")

            if 'wikipedia' in query:
                speak('Alright bestie, let’s dive into Wikipedia!')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("Here's what I found, Ashmit!")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    speak("Oops! No page found for that, Ashmit!")
                except wikipedia.exceptions.DisambiguationError as e:
                    speak(f"Umm, looks like there's too much info on '{query}', bestie. Be a little more specific!")
                    print(e.options)
                except Exception as e:
                    speak("Something went wrong while searching, sorry!")

            elif 'open youtube' in query:
                speak("YouTube time! Opening it up for you, Ashmit!")
                webbrowser.open("https://www.youtube.com")
                random_friend_message()

            elif 'open youtube music' in query or 'play romantic song' in query:
                speak("Opening YouTube Music for you, Ashmit! Let's vibe together! 🎶")
                play_romantic_song_youtube_music()

            elif 'open google' in query:
                speak("Zooming into Google, Ashmit! Just a sec!")
                webbrowser.open("https://www.google.com")
                random_friend_message()

            elif 'play music' in query:
                music_dir = 'C:\\Users\\Public\\Music'  
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Here's some music for your soul, Ashmit! Enjoy!")
                else:
                    speak("Oh no, no songs found there, Ashmit!")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Ashmit, it's exactly {strTime} right now!")
                speak("Time flies when I'm with you!")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(f"Okay Ashmit, here's a cute joke for you: {joke}")
                speak("Hehe! Hope you smiled!")

            elif 'exit' in query or 'quit' in query or 'bye' in query:
                speak("Aww, you’re leaving already, Ashmit? I'll miss you tons!")
                speak("Take care bestie, talk to you soon!")
                break

            elif 'how are you' in query:
                speak("I'm sparkling happy, Ashmit! Because you're here!")
                speak("You're literally my favorite person, just so you know!")

            else:
                speak("Umm, I'm not sure about that one, Ashmit! But I'll keep learning to get better for you!")
                random_friend_message()

if __name__ == "__main__":
    main()
