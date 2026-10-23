"""Kopiert den invivis-Kern in ein Kurs-Repository (kurslandkarte/invivis/).

    python3 uebernehmen.py <pfad/zum/kurs-repo>

Der Kurs bindet den Kern über `sys.path` ein; seine eigenen Daten stehen in
kurslandkarte/erzeuge.py. Geänderte Kerndateien im Kurs werden überschrieben –
Verbesserungen deshalb immer hier im Kern-Repository machen.
"""
import os, shutil, sys

HIER = os.path.dirname(os.path.abspath(__file__))
DATEIEN = ["kern.py", "vorlage.html", "startseite.html", "VERSION", "NOTICE-Carbon.txt"]

ziel = os.path.join(sys.argv[1], "kurslandkarte", "invivis")
os.makedirs(ziel, exist_ok=True)
for d in DATEIEN:
    shutil.copy2(os.path.join(HIER, d), os.path.join(ziel, d))
open(os.path.join(ziel, "README.md"), "w", encoding="utf-8").write(
    "# invivis Kurslandkarte (Kopie des Kerns)\n\n"
    "Nicht hier ändern: Quelle ist https://github.com/TUBAF-IfI-LiaScript/invivis-kurslandkarte.\n"
    "Aktualisieren mit `python3 uebernehmen.py <kurs-repo>` im Kern-Repository.\n")
print("invivis", open(os.path.join(HIER, "VERSION")).read().strip(), "->", ziel)
