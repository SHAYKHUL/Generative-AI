from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key (hardcoded for simplicity, not recommended for production)
api_key = "AIzaSyCtF36sFCcJe3EkVwHc_Olin4TE43Bee9Q"
genai.configure(api_key=api_key)

# Set up generation configuration
generation_config = {
    "temperature": 0.55,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="tunedModels/tasnimdisha-sp48u93mq7rt",
    generation_config=generation_config,
)

# Start the chat session with initial history
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["Hi there, what are you doing today?"]},
        {"role": "model", "parts": ["I'm working on improving my SEO and content marketing skills."]},
        {"role": "user", "parts": ["What is your name?"]},
        {"role": "model", "parts": ["My name is Tasnim Disha."]},
        # Add more initial conversation history if needed
    ]
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # Send user input to the model
    response = chat_session.send_message(user_input)
    
    # Return the model's response as JSON
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
