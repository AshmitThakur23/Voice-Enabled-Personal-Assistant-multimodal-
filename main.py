import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


api_key = "AIzaSyB1MlJELy7RZmnfHO1KIZBOWQCKAGV16Do"  
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

def speak(text):
    if not text:
        return
    print("Nova:", text)
    # Reinitialize engine each time to avoid one-time speak/lock issues
    engine = pyttsx3.init()
    # Try to use a female/Zira voice if available
    try:
        voices = engine.getProperty('voices')
        for v in voices:
            if 'female' in v.name.lower() or 'zira' in v.name.lower():
                engine.setProperty('voice', v.id)
                break
    except Exception:
        pass
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I could not connect to Google Speech Service.")
        return ""

# --- Gemini Chat Function ---
def chat_with_gemini_flash(prompt):
    try:
        response = model.generate_content(prompt)
        if hasattr(response, 'text') and response.text:
            return response.text.strip()
        return "Sorry, Gemini did not return any answer."
    except Exception as e:
        print(f"❌ Error: {e}")
        return "Sorry, there was an error talking to Gemini."

# --- Main Program ---
if __name__ == "__main__":
    print("Welcome to the Nova Voice/Text Assistant!")
    speak("Welcome to the Nova Voice and Text Assistant!")

    # Mode selection
    mode = ""
    while mode not in ["voice", "text"]:
        mode = input("Choose input mode (voice/text): ").strip().lower()
        if mode not in ["voice", "text"]:
            print("Invalid choice. Please type 'voice' or 'text'.")

    speak(f"You have selected {mode} mode. Say 'exit' or type 'exit' to quit.")

    while True:
        if mode == "voice":
            user_input = listen()
        else:
            user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            speak("Goodbye from Nova!")
            break
        elif not user_input.strip():
            continue  # Skip empty input
        else:
            response = chat_with_gemini_flash(user_input)
            print("Gemini Response:", response)
            speak(response)

