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

@app.route('/set_duration', methods=['POST'])
def set_duration():
    duration = request.form['duration']
    session['duration'] = int(duration)
    print("test for duration ",duration)
    return redirect(url_for('admin'))    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Falls der Benutzer nicht eingeloggt ist, auf die Login-Seite umleiten
    
    if request.method == 'POST':
        # Wenn das Formular zur Dauer eingestellt wird
        if 'duration' in request.form:
            duration = request.form['duration']
            session['duration'] = int(duration)
            return redirect(url_for('display'))  # Nach dem Speichern der Dauer auf die Display-Seite weiterleiten
        
        # Wenn eine Datei hochgeladen wird
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('admin'))  # Nach dem Hochladen der Datei wieder auf die Admin-Seite weiterleiten

    # Laden des aktuellen Texts und der Mediendateien für die Anzeige auf der Admin-Seite
    current_text = load_display_text()  # Funktion, um den Text für die Anzeige zu laden
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])  # Liste der Mediendateien im Upload-Ordner
    return render_template('admin.html', media_files=media_files, current_text=current_text)


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
@app.route('/video')
def video():
    # Liste alle Dateien im Upload-Ordner
    video_folder = os.listdir(UPLOAD_FOLDER)

    # Suche nach .mp4, .mov, .avi Videos
    video_file = [f for f in video_folder if f.lower().endswith(('mp4', 'mov', 'avi'))]
 
    if not video_file:
        return "Kein Video gefunden."

    # Wenn du ein zufälliges Video wählen willst, kannst du es so tun:
    # import random
    # video_file = random.choice(video_file)  # Wählt zufällig ein Video aus der Liste

    # Falls du einfach das erste Video verwenden willst:
    video_file = video_file[0]

    return render_template('video.html', video_file=video_file)
@app.route('/display')
def display():
    duration = session.get('duration', 10)
    files = os.listdir(UPLOAD_FOLDER)
    image_files = [f for f in files if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    video_files = [f for f in files if f.lower().endswith(('mp4', 'mov', 'avi'))]
    selected_video = video_files[0] if video_files else None
    current_text = load_display_text()
    return render_template('display.html', image_files=image_files, duration=duration ,video_file=selected_video, display_text=current_text)
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
