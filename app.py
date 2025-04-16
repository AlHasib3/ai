import os
from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv

# .env ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করা
load_dotenv()

app = Flask(__name__)

# OpenAI API কী সেট করা
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # ব্যবহারকারীর ইনপুট নেওয়া
    user_message = request.form.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # GPT-4.1-এর জন্য
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150,
            temperature=0.7,
        )
        chat_response = response.choices[0].message['content'].strip()
    except Exception as e:
        chat_response = f"ত্রুটি ঘটেছে: {str(e)}"
    return jsonify({"response": chat_response})

if __name__ == "__main__":
    app.run(debug=True)
