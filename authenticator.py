import os
import sys
from datetime import datetime
import sqlite3  # SQLite ist bereits in Python eingebaut!

# Speicherort der echten Datenbankdatei im Container
db_pfad = "/data/praktikum.db"

jetzt = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
print(f"[{jetzt}] Verbinde mit SQLite-Datenbank unter {db_pfad}...")

try:
    # Verbindung aufbauen (erstellt die Datei automatisch, falls nicht vorhanden)
    verbindung = sqlite3.connect(db_pfad)
    cursor = verbindung.cursor()
    
    # Tabelle erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS praktikum_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zeitstempel TEXT,
            meldung TEXT
        );
    """)
    
    # Neuen Datensatz schreiben
    cursor.execute(
        "INSERT INTO praktikum_log (zeitstempel, meldung) VALUES (?, ?);",
        (jetzt, "Erfolgreicher Docker-Login und SQLite-Tabelleneintrag!")
    )
    verbindung.commit()
    
    # Daten auslesen, um den Beweis anzutreten
    cursor.execute("SELECT * FROM praktikum_log;")
    eintraege = cursor.fetchall()
    
    print(f"[{jetzt}] ERFOLG: Verbindung steht! Aktuelle Einträge in der DB:")
    for zeile in eintraege:
        print(f"   -> ID {zeile[0]} | Zeit: {zeile[1]} | {zeile[2]}")
        
    cursor.close()
    verbindung.close()
    sys.exit(0)
    
except Exception as fehler:
    print(f"[{jetzt}] FEHLER: {fehler}")
    sys.exit(1)
