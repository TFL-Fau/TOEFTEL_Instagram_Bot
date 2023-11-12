from flask import Flask, render_template, request, redirect, url_for, flash, Response, stream_with_context
import bot_functions
import time
import datetime


app = Flask(__name__)
app.secret_key = 'some_secret_key'

bot_instance = bot_functions

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/run-bot", methods=['POST'])
def run_bot():
    if request.method == 'POST':
        username = request.form['accountname']
        password = request.form['password']
        hashtags = request.form['hashtags'].split(',')
        commentname = request.form.get('commentname', ' ')
        methods = request.form.getlist('methods')
        
        bot_instance.start_bot(hashtags, username, password, methods, commentname)
        
        flash('Bot-Aufgaben abgeschlossen!')
        return redirect(url_for('index'))

@app.route('/status')
def status():
    last_index = -1

    def generate():
        nonlocal last_index
        while True:
            messages = bot_instance.get_messages()
            if not messages:
                time.sleep(1)
                continue

            current_last_index = len(messages) - 1
            if last_index != current_last_index:
                for idx in range(last_index + 1, current_last_index + 1):
                    yield f"data: {{\"message\": \"{datetime.datetime.now().strftime('%H:%M:%S')}: {messages[idx]}\"}}\n\n"
                last_index = current_last_index

            time.sleep(5)

    return Response(stream_with_context(generate()), content_type='text/event-stream')

       

if __name__ == "__main__":
    app.run(debug=True, threaded=True,host="0.0.0.0")
