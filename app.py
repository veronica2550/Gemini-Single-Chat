from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("중세시대 배경에서 의사의 삶에 대해 5줄로 작성해줘.")

# print(response.text)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        user_input = request.form['user_input']  # 사용자가 입력한 텍스트
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_input)
        response_text = response.text  # API 응답

    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True)