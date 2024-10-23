# app.py

from flask import Flask, render_template, request, redirect, url_for
from file_manager import FileManager

app = Flask(__name__)
file_manager = FileManager('log.txt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'new_entry' in request.form:
            new_entry = request.form['new_entry']
            file_manager.write_to_file(new_entry)
            return redirect(url_for('index'))
        elif 'search' in request.form:
            keyword = request.form['keyword']
            results = file_manager.search_keyword(keyword)
            return render_template('index.html', logs=file_manager.read_file(), results=results)

    return render_template('index.html', logs=file_manager.read_file())

if __name__ == '__main__':
    app.run(debug=True)
