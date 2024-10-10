from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Simple response logic
    if user_input:
        response = f"You said: {user_input}"
    else:
        response = "Please say something!"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
