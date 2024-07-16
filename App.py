from flask import Flask, request, jsonify, render_template
import openai



#API Code
api_key = "CODE from OpenAI"
openai.api_key = api_key

app = Flask(__name__)

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.form['prompt']
    response = get_openai_response(prompt)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
