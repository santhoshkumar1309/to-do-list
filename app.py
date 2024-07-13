from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)