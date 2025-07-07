
🧾 Menu Display System – README
Ein einfaches, visuelles Anzeige-System zur Darstellung von Menüs (z. B. für Kantinen), mit Bildrotation, Beschreibung und flexibler Steuerung.

📁 Repository erstellen
Falls du dein Projekt noch nicht als Git-Repository eingerichtet hast:

bash
Kopieren
Bearbeiten
# Im Projektordner
git init
git add .
git commit -m "Initial commit"
Wenn du es mit GitHub verbinden willst:

bash
Kopieren
Bearbeiten
git remote add origin https://github.com/DEIN_USERNAME/menu-display-system.git
git push -u origin main
🧰 Voraussetzungen
Python 3.9+

pip

Optional: virtualenv oder venv

🛠️ Lokale Entwicklungsumgebung einrichten
bash
Kopieren
Bearbeiten
# Projektverzeichnis betreten
cd menu-display-system

# Virtuelle Umgebung erstellen
python -m venv venv

# Aktivieren (Linux/macOS)
source venv/bin/activate

# Aktivieren (Windows)
venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
Falls du kein requirements.txt hast, hier ein Beispiel:

txt
Kopieren
Bearbeiten
Flask==2.3.2
▶️ Anwendung starten
bash
Kopieren
Bearbeiten
# Aktiviere ggf. deine Umgebung (s.o.)

# Anwendung starten
python app.py
Die App läuft dann unter:
  http://localhost:5000

📂 Projektstruktur

menu-display-system/
├── static/
│   └── uploads/           # Hier liegen deine Menübilder
├── templates/
│   └── test.html # HTML-Vorlage für die Anzeige
  └── admin.html  # HTML-Vorlage für die Admin seite

├── app.py                 # Flask Backend
├── requirements.txt       # Abhängigkeiten
├── README.md              # Diese Datei


menu display
git clone Bitte Link Aus github Kopieren 



--  sudo apt update
sudo apt install unzip
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
chmod +x ngrok
./ngrok config add-authtoken DEIN_TOKEN_HIER
ngrok auth ::   WHINQSTDABOX3MIKQLAPMLSCAI5M6TWP
zweiten  2voSEI2CxJ72ZAQyd6I6Y9Pstdw_6EeVKf9TGgwvsHdXneEBb
