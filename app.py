from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Simple task groups
to_do = ['Task 1', 'Task 2', 'Task 3']
doing = ['Task 1', 'Task 2', 'Task 3']
done = ['Task 1', 'Task 2', 'Task 3']

@app.route('/')
def index():
    return render_template('index.html', to_do=to_do, doing=doing, done=done)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')
    if new_task:
        to_do.append(new_task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)