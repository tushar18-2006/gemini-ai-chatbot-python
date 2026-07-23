import tkinter as tk
from tkinter import scrolledtext
from google import genai

# ==========================
# PASTE YOUR GEMINI API KEY HERE
# ==========================
API_KEY = "AQ.Ab8RN6JicubkfelTdTiOvto0cihYFN2fzQ1FTCKGSBRIPfjtTA"

# Create Gemini Client
client = genai.Client(api_key=API_KEY)


def send_message():
    user_message = entry.get()

    if user_message.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_message + "\n")

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=user_message
        )

        ai_reply = response.text

    except Exception as e:
        ai_reply = "Error: " + str(e)

    chat_box.insert(tk.END, "Gemini: " + ai_reply + "\n\n")

    entry.delete(0, tk.END)


# ------------------------------
# GUI
# ------------------------------

window = tk.Tk()
window.title("Gemini AI Chatbot")
window.geometry("700x600")

chat_box = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=80,
    height=30,
    font=("Arial", 11)
)
chat_box.pack(padx=10, pady=10)

entry = tk.Entry(
    window,
    width=70,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(
    window,
    text="Send",
    command=send_message,
    width=12
)
send_button.pack(side=tk.LEFT)

window.mainloop()