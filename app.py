from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask import session, flash
import random

app = Flask(__name__)

app.secret_key = 'supergeheim'  # Für Session
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('admin'))
    current_text = load_display_text()
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('admin.html', media_files=media_files)


def load_display_text():
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "Willkommen!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'admin123':  # ← hier Passwort setzen
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Falsches Passwort!')
    return render_template('login.html')
TEXT_FILE = "static/display_text.txt"

@app.route("/set_text", methods=["POST"])
def set_text():
    text = request.form["display_text"]
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    return redirect("/admin")


@app.route('/display')
def display():
    files = os.listdir(UPLOAD_FOLDER)
    image_files = [f for f in files if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    return render_template('display.html', image_files=image_files)
@app.route("/delete", methods=["POST"])
def delete_file():
    filename = request.form["filename"]
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect("/admin")


if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
