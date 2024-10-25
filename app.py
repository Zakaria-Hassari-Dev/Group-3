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

    return render_template('index.html', logs=file_manager.read_file(), search_results=[])

@app.route('/search', methods=['POST'])
def search():
    if 'keyword' in request.form:
        keyword = request.form['keyword']
        search_results = file_manager.search_keyword(keyword)
        return render_template('index.html', logs=file_manager.read_file(), search_results=search_results)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    if 'delete_keyword' in request.form:
        keyword = request.form['delete_keyword']
        file_manager.delete_lines(keyword)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
