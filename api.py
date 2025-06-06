from flask import Flask, request, jsonify
from ollama import chat
from ollama import ChatResponse

app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def chat_endpoint():
    try:
        prompt = request.args.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt não fornecido'}), 400

        response: ChatResponse = chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
            ],
        )
        
        return jsonify({
            'response': response.message.content
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
