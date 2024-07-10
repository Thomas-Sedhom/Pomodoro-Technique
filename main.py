import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
Pomodoro_duration = 25 * 60
session_type = "Pomodoro"
start_time = None
temp_time = None
tasks = []


@app.route("/")
def index():
    remaining_time = 0
    if start_time:
        elapsed_time = time.time() - start_time
        remaining_time = Pomodoro_duration - elapsed_time
    return render_template("index.html", remaining_time = remaining_time, session_type = session_type)

@app.route("/start")
def start_timer():
    global start_time
    start_time = time.time()
    print(start_time)
    start_time = int(start_time)
    start_time_int = int(start_time)
    return {"startTime": start_time_int} 

@app.route('/stop')
def stop_timer():
    global start_time
    global temp_time
    temp_time = start_time
    print(temp_time)
    start_time = None
    return "timer stopped"

@app.route('/continue')
def continue_timer():
    global start_time
    print(temp_time)
    start_time = temp_time
    return {"startTime": start_time}

@app.route("/add_task", methods=["POST"])
def add_task():
    task_data = request.get_json()
    tasks.append(task_data)
    return jsonify({"message": tasks}), 201

@app.route('/reset')
def reset_timer():
    global current_duration, session_type, start_time
    current_duration = Pomodoro_duration
    start_time = None
    return "timer reset"

@app.route("/get_tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/ajax/click', methods=['POST'])
def handle_click():
    action = request.form.get('action')
    if action == 'start':
        return start_timer()
    elif action == 'stop':
        return stop_timer()
    elif action == 'continue':
        return continue_timer()
    elif action == 'reset':
        return reset_timer()
    return "Invalid action"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  