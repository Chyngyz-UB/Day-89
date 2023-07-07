from flask import Flask, render_template, request, jsonify
from threading import Timer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Store the user's text
user_text = ""
timer = None
timer_duration = 2

def reset_timer():
    global user_text
    user_text = ""
    print("Text cleared.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-typing', methods=['POST'])
def start_typing():
    global timer

    # Reset the timer if it's already running
    if timer:
        timer.cancel()

    # Start a new timer
    timer = Timer(timer_duration, reset_timer)
    timer.start()

    return jsonify({'message': 'Timer started.'})

@app.route('/save-text', methods=['POST'])
def save_text():
    global user_text

    text = request.form.get('text')
    user_text += text

    return jsonify({'message': 'Text saved.'})

@app.route('/get-text', methods=['GET'])
def get_text():
    return jsonify({'text': user_text})

if __name__ == '__main__':
    app.run(debug=True)
