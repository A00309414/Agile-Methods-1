from flask import Flask, render_template

app = Flask(__name__)

# Simple task groups
to_do = ['Task 1', 'Task 2', 'Task 3']
doing = ['Task 1', 'Task 2', 'Task 3']
done = ['Task 1', 'Task 2', 'Task 3']

@app.route('/')
def index():
    return render_template('index.html', to_do=to_do, doing=doing, done=done)

if __name__ == ('__main__'):
    app.run(debug=True)