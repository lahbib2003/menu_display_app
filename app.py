from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask import session, flash
import random
from datetime import datetime , timedelta
import calendar
app = Flask(__name__)

app.secret_key = 'supergeheim'  # Für Session
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/')
#def home():
    #return redirect(url_for('login'))

@app.route('/set_duration', methods=['POST'])
def set_duration():
    duration = request.form['duration']
    session['duration'] = int(duration)
    print("test for duration ",duration)
    return redirect(url_for('admin'))    

@app.route('/', methods=['GET', 'POST'])
def index():
    video_filename = None
    duration = session.get('duration', 10)
    weekday = datetime.now().strftime('%A').lower()  # z.B. 'monday'
    files = os.listdir(UPLOAD_FOLDER)

    # Nur Bilder vom aktuellen Wochentag
    image_files = [
        f for f in files
        if f.lower().startswith(weekday) and f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))
    ]

    # Bei POST: neues Video speichern
    if request.method == 'POST':
        file = request.files.get('hint')
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            video_filename = filename
    else:
        # Wenn kein neues Video hochgeladen wurde: Suche erstes Video mit "hint_"
        for f in files:
            if f.lower().startswith("hintergrund") and f.lower().endswith(".mp4"):
                video_filename = f
                break

    return render_template("index.html", video=video_filename, image_files=image_files, duration=duration)
 
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'duration' in request.form:
            duration = request.form['duration']
            session['duration'] = int(duration)
            return redirect(url_for('display'))

        file = request.files.get('file')
        selected_day = request.form.get('day')

        if file and allowed_file(file.filename):
            # Automatischen Wochentag ermitteln, wenn keiner ausgewählt ist
            if not selected_day:
                today = datetime.today().weekday()  # 0 = Montag, 6 = Sonntag
                day_names = ['Monday',  'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
                selected_day = day_names[today]

            original_filename = secure_filename(file.filename)
            filename = f"{selected_day}_{original_filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('admin'))

    current_text = load_display_text()
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
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
    weekday = datetime.now().strftime('%A').lower()  # z.B. 'monday', 'tuesday', etc.

    # Liste alle Dateien im Upload-Ordner
    video_folder = os.listdir(UPLOAD_FOLDER)

    # Filtere Videos, die mit dem heutigen Wochentag beginnen
    video_file = [
        f for f in video_folder
        if f.lower().startswith(weekday) and f.lower().endswith(('mp4', 'mov', 'avi'))
    ]

    if not video_file:
        return f"Kein Video gefunden für {weekday.title()}."

    # Du kannst hier z.B. das erste Video nehmen oder ein zufälliges
    video_file = video_file[0]

    return render_template('video.html', video_file=video_file)

@app.route('/display')
def display():
    duration = session.get('duration', 10)
    weekday = datetime.now().strftime('%A').lower()  # z.B. 'monday'
    #weekday = (datetime.now() + timedelta(days=1)).strftime('%A').lower()
    files = os.listdir(UPLOAD_FOLDER)

    # Nur Bilder vom aktuellen Wochentag
    image_files = [
        f for f in files
        if f.lower().startswith(weekday) and f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))
    ]

    # Falls weniger als 3 Bilder, auffüllen mit leeren Strings
    while len(image_files) < 3:
        image_files.append(None)

    # 3 zufällige Bilder auswählen, wenn mehr vorhanden sind
    selected_images = random.sample(image_files, 3) if len(image_files) >= 3 else image_files

    # Video vom heutigen Tag (optional)
    video_files = [
        f for f in files
        if f.lower().startswith(weekday) and f.lower().endswith(('mp4', 'mov', 'avi'))
    ]
    selected_video = video_files[0] if video_files else None

    current_text = load_display_text()

    return render_template('display.html',
                           image_files=selected_images,
                           duration=duration,
                           video_file=selected_video,
                           display_text=current_text)
@app.route("/delete", methods=["POST"])
def delete_file():
    filename = request.form["filename"]
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect("/admin")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)