from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask import session, flash ,jsonify

import random
from datetime import datetime , timedelta
import calendar
app = Flask(__name__)
import json  # Ganz oben ergänzen

import uuid
MENU_FILE = "static/menus.json"  # Neue globale Variable
app.secret_key = 'supergeheim'  # Für Session
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SCHEDULE_FILE = "static/menu_schedule.json" 
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
    weekday = datetime.now().strftime('%A')  # z.B. 'Monday'

    # Lade Zuweisungen
    assignments = []
    if os.path.exists('assignments.json'):
        with open('assignments.json', 'r', encoding='utf-8') as f:
            assignments = json.load(f)

    # Lade Menü-Daten
    menus = []
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []

    # Finde Menüs für den heutigen Wochentag
    assigned_menus = []
    for a in assignments:
        if a['day'].lower() == weekday.lower():
            # Menü-ID aus assignment
            menu_id = a['menu']['id']
            # Menü-Objekt aus Menü-Datei finden
            matching_menu = next((m for m in menus if m['id'] == menu_id), None)
            if matching_menu:
                assigned_menus.append(matching_menu)

    image_extensions = ['jpg', 'jpeg', 'png', 'gif']

    image_files = [
        menu['filename'] for menu in assigned_menus
        if menu['filename'].split('.')[-1].lower() in image_extensions
    ]

    # Bei POST: Video hochladen
    if request.method == 'POST':
        file = request.files.get('hint')
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            video_filename = filename
    else:
        # Wenn kein neues Video hochgeladen wurde: Suche erstes Video mit "hintergrund"
        files = os.listdir(UPLOAD_FOLDER)
        for f in files:
            if f.lower().startswith("hintergrund") and f.lower().endswith(".mp4"):
                video_filename = f
                break
      # Extrahiere nur benötigte Felder
    assigned_slides = [{
    'filename': m['filename'],
    'name': m['name'],
    'description': m['description']
    }  for m in assigned_menus]

    return render_template("index.html", video=video_filename, image_files=image_files, duration=duration,assigned_slides=assigned_slides)
ASSIGNMENTS_FILE = 'assignments.json'
#to delete the uploaded menus  
@app.route('/delete_menu', methods=['POST'])
def delete_menu():
    menu_id = request.form.get('menu_id')  # <<<<<< angepasst

    if not menu_id:
        return jsonify({"error": "menu_id missing"}), 400

    print("test von menu id ,", menu_id)

    # Menüs laden
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        menus = json.load(f)

    # Finde das zu löschende Menü
    menu_to_delete = next((m for m in menus if m['id'] == menu_id), None)
    if not menu_to_delete:
        flash("Menü nicht gefunden.")
        return redirect(url_for('admin'))  # oder wo deine Admin-Seite ist

    
    
  

    # Neue Menüliste speichern
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        json.dump(menus, f, ensure_ascii=False, indent=2)

    # Zuweisungen laden und filtern
    if os.path.exists(ASSIGNMENTS_FILE):
        with open(ASSIGNMENTS_FILE, 'r', encoding='utf-8') as f:
            assignments = json.load(f)
        
        assignments = [a for a in assignments if a['menu_id'] != menu_id]
        
        # Neue Zuweisungen speichern
        with open(ASSIGNMENTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(assignments, f, ensure_ascii=False, indent=2)

    flash("Menü und zugehörige Zuweisungen wurden gelöscht.")
    return redirect(url_for('admin'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = load_config()
    header_text = config.get('header_text', "Hungrig? Schau, was wir haben")
    ticker_enabled = True
    if os.path.exists('settings.json'):
        with open('settings.json', 'r', encoding='utf-8') as f:
            try:
                settings = json.load(f)
                ticker_enabled = settings.get('ticker_enabled', True)
            except json.JSONDecodeError:
                ticker_enabled = True
    if os.path.exists(ASSIGNMENTS_FILE):
        with open(ASSIGNMENTS_FILE, 'r', encoding='utf-8') as f:
            assigned_menus = json.load(f)
    else:
        assigned_menus = []

    if request.method == 'POST':
        if 'duration' in request.form:
            duration = request.form['duration']
            session['duration'] = int(duration)
            return redirect(url_for('display'))

        file = request.files.get('file')
        selected_day = request.form.get('day')

        if file and allowed_file(file.filename):
            if not selected_day:
                today = datetime.today().weekday()
                day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                selected_day = day_names[today]

            original_filename = secure_filename(file.filename)
            filename = f"{selected_day}_{original_filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('admin'))
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []
    else:
        menus = []
    # Neue Gruppierung für die Template-Ausgabe
    media_files = os.listdir(app.config['UPLOAD_FOLDER'])
    grouped_files = {}

    for file in media_files:
        if "_" in file:
            day = file.split('_')[0]
        else:
            day = "Unbekannt"

        if day not in grouped_files:
            grouped_files[day] = []
        grouped_files[day].append(file)

    return render_template('admin.html', media_files=media_files,ticker_enabled=ticker_enabled, grouped_files=grouped_files,  menus=menus,assigned_menus=assigned_menus)


@app.route('/upload_menu', methods=['POST'])
def upload_menu():
    if 'menu_image' not in request.files:
        flash('Kein Bild ausgewählt.')
        return redirect(url_for('admin'))

    image = request.files['menu_image']
    name = request.form.get('menu_name')
    description = request.form.get('menu_description')

    if not image or image.filename == '':
        flash('Ungültige Bilddatei.')
        return redirect(url_for('admin'))

    if not allowed_file(image.filename):
        flash('Dateityp nicht erlaubt.')
        return redirect(url_for('admin'))

    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    # Menü-Eintrag vorbereiten
    new_entry = {
        'id': str(uuid.uuid4()),  # Generiere eine einzigartige ID für jedes Menü
        'filename': filename,
        'name': name,
        'description': description
    }

    # Bestehende Menüs laden oder neues Array starten
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []
    else:
        menus = []

    menus.append(new_entry)

    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        json.dump(menus, f, ensure_ascii=False, indent=2)

    flash('Menübild erfolgreich hochgeladen.')
    return redirect(url_for('admin'))
TEXT_FILE = 'data.json'
@app.route('/save_text', methods=['POST'])
def save_text():
    # Daten aus dem Formular holen
    ken = request.form.get('ken')
    barbie = request.form.get('barbie')

    # Validierung: Sicherstellen, dass beide Felder ausgefüllt sind
    if not ken or not barbie:
        return jsonify({'error': 'Ken und Barbie müssen ausgefüllt sein'}), 400

    # Neue Daten als einzelner Eintrag in einer Liste
    new_entry = [{'ken': ken, 'barbie': barbie}]

    # Speichere die neuen Daten und überschreibe die JSON-Datei
    with open(TEXT_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)

    return jsonify({'message': 'Daten gespeichert'}), 200

@app.route('/load', methods=['GET'])
def load_text():
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, 'r', encoding='utf-8') as f:
            try:
                texts = json.load(f)
                return jsonify(texts), 200
            except json.JSONDecodeError:
                return jsonify({'error': 'Fehler beim Laden der Daten'}), 500
    else:
        return jsonify([]), 200
    
@app.route('/assign_menu', methods=['POST'])
def assign_menu():
    menu_id = request.form.get('menu_id')
    date = request.form.get('date')  # <-- Datum statt Wochentag

    # Lade bestehende Menüs
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []
    else:
        menus = []
    
    # Menü anhand der ID suchen
    selected_menu = next((menu for menu in menus if menu['id'] == menu_id), None)

    if selected_menu:
        # ✅ Tag aus Menü entfernen (optional, da Zuweisung jetzt extern ist)
        selected_menu.pop('day', None)

        # ✅ Überschreibe das Menü in der Menüliste
        for i, menu in enumerate(menus):
            if menu['id'] == menu_id:
                menus[i] = selected_menu
                break

        # ✅ Speichere das aktualisierte Menü zurück in menus.json
        with open(MENU_FILE, 'w', encoding='utf-8') as f:
            json.dump(menus, f, ensure_ascii=False, indent=2)

        # ✅ Speichere die Zuweisung in assignments.json (optional)
        assignment = {
            'menu_id': menu_id,
            'date': date,
            'menu': selected_menu
        }

        if os.path.exists('assignments.json'):
            with open('assignments.json', 'r', encoding='utf-8') as f:
                try:
                    assignments = json.load(f)
                except json.JSONDecodeError:
                    assignments = []
        else:
            assignments = []

        assignments.append(assignment)

        with open('assignments.json', 'w', encoding='utf-8') as f:
            json.dump(assignments, f, ensure_ascii=False, indent=2)

        flash(f'Menü {selected_menu["name"]} erfolgreich dem {date} zugewiesen!')
    else:
        flash('Menü nicht gefunden!')

    return redirect(url_for('admin'))

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
    video_filename = None
    duration = session.get('duration', 10)
    weekday = datetime.now().strftime('%A')  # z.B. 'Monday'
   
    # Lade Zuweisungen
    assignments = []
    if os.path.exists('assignments.json'):
        with open('assignments.json', 'r', encoding='utf-8') as f:
            assignments = json.load(f)

    # Lade Menü-Daten
    menus = []
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []

    # Finde Menüs für den heutigen Wochentag
    assigned_menus = []
    for a in assignments:
        if a['day'].lower() == weekday.lower():
            # Menü-ID aus assignment
            menu_id = a['menu']['id']
            # Menü-Objekt aus Menü-Datei finden
            matching_menu = next((m for m in menus if m['id'] == menu_id), None)
            if matching_menu:
                assigned_menus.append(matching_menu)

    # Nur gültige Videodateien extrahieren
    video_files = [
        menu['filename'] for menu in assigned_menus
        if menu['filename'].lower().endswith(('mp4', 'mov', 'avi'))
    ]

    selected_video = random.choice(video_files) if video_files else None

    return render_template('video.html', video_file=selected_video)

from datetime import datetime
import os, json, random

@app.route('/display')
def display():
    duration = session.get('duration', 10)
    weekday = datetime.now().strftime('%A').lower()

    # Lade Zuweisungen
    assignments = []
    if os.path.exists('assignments.json'):
        with open('assignments.json', 'r', encoding='utf-8') as f:
            assignments = json.load(f)

    # Lade Menü-Daten
    menus = []
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []

    # Finde Menüs, die für heute zugewiesen wurden
    assigned_menus = []
    for a in assignments:
        if a['day'].lower() == weekday:
            menu_id = a['menu']['id']
            matching_menu = next((m for m in menus if m['id'] == menu_id), None)
            if matching_menu:
                assigned_menus.append(matching_menu)

    # Nur Bilddateien verwenden (keine Videos)
    allowed_image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = [
        menu['filename']
        for menu in assigned_menus
        if menu['filename'].lower().endswith(allowed_image_extensions)
    ]

    # Falls weniger als 3 Bilder, auffüllen mit None
    while len(image_files) < 3:
        image_files.append(None)

    # 3 zufällige Bilder auswählen
    selected_images = random.sample(image_files, 3) if len(image_files) >= 3 else image_files

    current_text = load_display_text()
    assigned_slides = [{
    'filename': m['filename'],
    'name': m['name'],
    'description': m['description']
    }  for m in assigned_menus]
    return render_template('display.html',
                           image_files=selected_images,
                           duration=duration,
                           video_file=None,  # oder entferne es ganz
                           display_text=current_text,assigned_slides=assigned_slides)

@app.route("/test", methods=["GET", "POST"])
def index_test():
    video_filename = None
    duration = session.get('duration', 10)
    today = datetime.now().strftime('%Y-%m-%d')  # Aktuelles Datum im Format YYYY-MM-DD
    config = load_config()
    header_text = config.get('header_text', "Hungrig? Schau, was wir haben")
    # Lade Zuweisungen
    assignments = []
    if os.path.exists('assignments.json'):
        with open('assignments.json', 'r', encoding='utf-8') as f:
            try:
                assignments = json.load(f)
            except json.JSONDecodeError:
                assignments = []

    # Lade Menü-Daten
    menus = []
    if os.path.exists(MENU_FILE):
        with open(MENU_FILE, 'r', encoding='utf-8') as f:
            try:
                menus = json.load(f)
            except json.JSONDecodeError:
                menus = []

    # Finde Menüs, die HEUTE zugewiesen sind
    assigned_menus = []
    for a in assignments:
        if a.get('date') == today:
            menu_id = a['menu']['id']
            matching_menu = next((m for m in menus if m['id'] == menu_id), None)
            if matching_menu:
                assigned_menus.append(matching_menu)

    # Lade Ken/Barbie-Daten
    ken_barbie_data = []
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, 'r', encoding='utf-8') as f:
            try:
                ken_barbie_data = json.load(f)
            except json.JSONDecodeError:
                ken_barbie_data = []

    # Nur Bild-Dateien extrahieren
    image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    image_files = [
        menu['filename'] for menu in assigned_menus
        if menu['filename'].split('.')[-1].lower() in image_extensions
    ]

    # Datei-Upload (Video)
    if request.method == 'POST':
        file = request.files.get('hint')
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            video_filename = filename
    else:
        # Suche nach hintergrund-video
        files = os.listdir(UPLOAD_FOLDER)
        for f in files:
            if f.lower().startswith("hintergrund") and f.lower().endswith(".mp4"):
                video_filename = f
                break

    # Reduzierte Datenstruktur für das Template
    assigned_slides = [{
        'filename': m['filename'],
        'name': m['name'],
        'description': m['description']
    } for m in assigned_menus]

    # Ken & Barbie Namen setzen
    ken_name = ken_barbie_data[0]['ken'] if ken_barbie_data else "Ken"
    barbie_name = ken_barbie_data[0]['barbie'] if ken_barbie_data else "Barbie"
    ticker_enabled = True
    if os.path.exists('settings.json'):
        with open('settings.json', 'r', encoding='utf-8') as f:
            try:
                settings = json.load(f)
                ticker_enabled = settings.get('ticker_enabled', True)
            except json.JSONDecodeError:
                ticker_enabled = True

    return render_template(
        "test.html",
        assigned_slides=assigned_slides,
        video=video_filename,
        image_files=image_files,
        ken_name=ken_name,
        barbie_name=barbie_name,
        ticker_enabled=ticker_enabled,header_text=header_text
    )

@app.route("/delete", methods=["POST"])
def delete_file():
    filename = request.form["filename"]
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect("/admin")
@app.route('/delete_menus', methods=['POST'])
def delete_menus():
    menu_id = request.form.get('menu_id')  # <<<<<< angepasst

    if not menu_id:
        return jsonify({"error": "menu_id missing"}), 400

    print("test von menu id ,", menu_id)

    # Menüs laden
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        menus = json.load(f)

    # Finde das zu löschende Menü
    menu_to_delete = next((m for m in menus if m['id'] == menu_id), None)
    if not menu_to_delete:
        flash("Menü nicht gefunden.")
        return redirect(url_for('admin'))  # oder wo deine Admin-Seite ist

    # Bild löschen
    image_path = os.path.join(UPLOAD_FOLDER, menu_to_delete['filename'])
    if os.path.exists(image_path):
        os.remove(image_path)

    # Menü aus Liste entfernen
    menus = [m for m in menus if m['id'] != menu_id]

    # Neue Menüliste speichern
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        json.dump(menus, f, ensure_ascii=False, indent=2)

    # Zuweisungen laden und filtern
    if os.path.exists(ASSIGNMENTS_FILE):
        with open(ASSIGNMENTS_FILE, 'r', encoding='utf-8') as f:
            assignments = json.load(f)
        
        assignments = [a for a in assignments if a['menu_id'] != menu_id]
        
        # Neue Zuweisungen speichern
        with open(ASSIGNMENTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(assignments, f, ensure_ascii=False, indent=2)

    flash("Menü und zugehörige Zuweisungen wurden gelöscht.")
    return redirect(url_for('admin'))
@app.route('/toggle_ticker', methods=['POST'])
def toggle_ticker():
    enabled = request.form.get('ticker_enabled') == 'on'

    # Speichern in settings.json
    with open('settings.json', 'w', encoding='utf-8') as f:
        json.dump({'ticker_enabled': enabled}, f, ensure_ascii=False, indent=2)

    flash('Ticker-Einstellung aktualisiert!')
    return redirect(url_for('admin'))
#header config 


CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

@app.route('/update_header', methods=['POST'])
def update_header():
    new_header = request.form.get('header_text')
    config = load_config()
    config['header_text'] = new_header
    save_config(config)
    flash('Header-Text wurde aktualisiert!')
    return redirect(url_for('admin'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)