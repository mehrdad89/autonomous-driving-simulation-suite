from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    report_files = os.listdir('reports')
    return render_template('index.html', reports=report_files)

@app.route('/report/<filename>')
def report(filename):
    path = f'reports/{filename}'
    return send_file(path)

if __name__ == "__main__":
    app.run(debug=True)
