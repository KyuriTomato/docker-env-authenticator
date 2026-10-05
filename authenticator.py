import os
from datetime import datetime

# 1. Wir holen uns die Variablen aus der Umgebung (Environment)
# Wenn Docker uns nichts mitgibt, setzen wir ein "Nicht definiert" als Standardwert
db_host = os.getenv("DB_HOST", "Nicht definiert")
db_user = os.getenv("DB_USER", "Nicht definiert")
db_password = os.getenv("DB_PASSWORD", "Nicht definiert")

# 2. Aktuelle Uhrzeit für das Protokoll holen
jetzt = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

print(f"[{jetzt}] Starte Verbindungsaufbau zu Host: {db_host}...")

# 3. Die Sicherheitsprüfung (Authentifizierung)
# Wir legen fest: Der Login ist nur erfolgreich, wenn der User "admin" und das Passwort "administhebest" ist
if db_user == "admin" and db_password == "administhebest":
    print(f"[{jetzt}] ✅ ZUGRIFF ERLAUBT: Erfolgreich als '{db_user}' an '{db_host}' angemeldet.")
else:
    print(f"[{jetzt}] ❌ ZUGRIFF VERWEIGERT: Falsche Zugangsdaten für Benutzer '{db_user}'.")

