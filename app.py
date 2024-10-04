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
        user_input = request.form['user_input']
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_input)
        
        # API 응답 구조 출력
        print(response)  # 응답 내용을 출력하여 구조 확인

        # response.text 대신 적절한 필드 사용
        if hasattr(response, 'text'):
            response_text = response.text  # 기존 코드를 유지하되, 예외처리 추가
        else:
            response_text = "응답에 'text' 필드가 없습니다."

    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)