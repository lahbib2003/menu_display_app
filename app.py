from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import os

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # ändere das!

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

USERNAME = 'admin'
PASSWORD = 'passwort123'

@app.route('/')
def display():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('display.html', files=files)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('admin.html', files=files)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return "Login fehlgeschlagen"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Keine Datei'
    file = request.files['file']
    if file.filename == '':
        return 'Keine Datei ausgewählt'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return redirect(url_for('admin'))

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')