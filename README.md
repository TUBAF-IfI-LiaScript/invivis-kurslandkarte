# invivis Kurslandkarte

_Autoren: Sebastian Zug, Ines Aubeln & Claude Code (Opus 5.5)_

Gemeinsamer Kern der Kurslandkarten im Projekt **invivis**: eine interaktive Übersicht für Studierende über Termine, Begriffe, Zusammenhänge und didaktische Fäden eines Kurses – dazu eine Startseite und auf Wunsch Orientierungsfolien in den LiaScript-Materialien. Jeder Kurs liefert nur seine Daten; Prüfung, Darstellung und Verbesserungen leben hier an einer Stelle.

Genutzt von:

| Kurs | Karte | Besonderheit |
| :--- | :---- | :----------- |
| Erhebung, Analyse und Visualisierung digitaler Daten (EAVD) | [Karte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) | strenge Freigabe (`vorschau="keine"`) |
| Digitale Systeme / Eingebettete Systeme | [Karte](https://tubaf-ifi-liascript.github.io/VL_EingebetteteSysteme/kurslandkarte/) | Seiten aus der Repo-Wurzel |
| Robotik (VL, Ü, P) | [Karte](https://tubaf-ifi-liascript.github.io/VL_SoftwareprojektRobotik/kurslandkarte/) | drei Termintypen, Orientierungsfolien (`folien=True`) |

## Ansichten

* **Vorlesungen / Termine:** Wochenraster nach Blöcken; Spalten für die Termintypen, die im Kurs vorkommen (VL, Ü, P). Jede Kachel: Leitfrage bzw. Ziel im Projekt, Begriffe als Chips, angewandte Begriffe („wendet an“), Anwendungen, Links auf Folien und PDF. Standard auf dem Handy.
* **Metrokarte:** didaktische Fäden als Linien über die Zeit.
* **Zeitleiste:** alle Begriffe nach Themengebiet mit Pfeilen für ihre Beziehungen.

„Sie sind hier“ folgt dem Datum. Begriffe erscheinen nach ihrer Freigabe; `vorschau="ausblick"` zeigt vorbereitete Begriffe auf Wunsch blass, `vorschau="keine"` lässt sie gar nicht erst in die Seite.

Direktlinks: `…/kurslandkarte/#termin=<key>`, `#begriff=<id>`, `#ansicht=liste|metro|zeit` (kombinierbar mit `&`).

**Druckfassungen:** Mit `pdf_ordner="docs/pdf"` verlinken Kacheln und Startseite das PDF jedes Termins (Name = Materialdatei, bei `README.md` der Ordnername). `python3 kurslandkarte/erzeuge.py --pdf` erzeugt vorher mit dem LiaScript-Exporter `liaex` jedes fehlende oder veraltete PDF. Gebaut und verlinkt werden die PDFs der freigegebenen Termine, alternativ die in `pdf_termine` genannten. Die PDFs werden mit eingecheckt.

## Termine und Datum

Die Karte ordnet Termine nach **Kalenderwochen** (Rasterzeile „KW 44 · 26.–30.10.“). Was am einzelnen Termin steht, hängt vom Kurs ab:

* **Standard:** Das Datum eines Termins ist irgendein Tag seiner Woche (meist der Montag). Angezeigt wird nur die Woche („KW 44 · 26.–30.10.“), damit kein Montag als Termin missverstanden wird.
* **`"tagesgenau": True`** im `KURS`-Wörterbuch: Das Datum ist der echte Tag. Mit `"uhrzeiten": {"Mi": "11:30–13:00", "Do": "16:15–17:45"}` erscheint die Uhrzeit dazu („Mi 28.10. · 11:30–13:00“). Ein Termin über mehrere Tage nimmt eine Liste (`["2026-11-25", "2026-11-26"]` → „Mi 25.11. 11:30–13:00 + Do 26.11. 16:15–17:45“; in der Blocktabelle der Folien nur die Tage); steht nur die Woche fest, genügt `"2027-W21"` („KW 21 · Tag folgt“).

Der Kern prüft, dass Wochen und Tage chronologisch sind. Startseite, Kacheln, Wochenleiste und Orientierungsfolien („Nächster Halt“) zeigen dieselbe Angabe.

## Gestaltung

Karte und Startseite folgen der Lia-Designsprache (Entwurf: Ines Aubeln): IBM Plex, LiaScript-Marke im Fuß, eine Form je Art von Klick-Element. Farbe hat auf der ganzen Seite genau eine Bedeutung: Fäden der Metrokarte tragen die Linienfarben mit Nummernfeld (F1–F6), damit sie auch bei Farbsehschwäche unterscheidbar bleiben. Themengebiete sind farblos.

## Dateien

| Datei | Inhalt |
| :---- | :----- |
| `kern.py` | Prüfung der Daten, Erzeugung von `kurslandkarte.json`, Karte, Startseite und Orientierungsfolien |
| `vorlage.html` | Karte; `%%…%%` füllt `kern.py` |
| `startseite.html` | Startseite des Kurses („Diese Woche“, Kurslandkarte, Lernziele, Organisation, Kontakt) |
| `uebernehmen.py` | kopiert den Kern nach `<kurs>/kurslandkarte/invivis/` |
| `VERSION` | Version des Kerns; steht in jeder erzeugten Seite |
| `NOTICE-Carbon.txt` | Lizenzhinweis für das eingebettete Carbon-Icon (Apache 2.0) |

## Einen Kurs anbinden oder aktualisieren

```bash
python3 uebernehmen.py ../VL_Robotik/VL_SoftwareprojektRobotik   # Kern in den Kurs kopieren
cd ../VL_Robotik/VL_SoftwareprojektRobotik && python3 kurslandkarte/erzeuge.py
```

Die Kursdatei `kurslandkarte/erzeuge.py` enthält nur Daten und ruft `kern.erzeuge(...)` auf. Datenformate und Parameter stehen im Kopf von `kern.py`. Verbesserungen immer hier machen, `VERSION` erhöhen und an alle Kurse verteilen – Änderungen in `kurslandkarte/invivis/` eines Kurses werden beim nächsten Übernehmen überschrieben.

## Kursspezifisches

Alles Kursspezifische steht im `KURS`-Wörterbuch der Kursdatei: Titel, Links (LiaScript, Pages, Repository), Wortwahl (`einheit` „Vorlesung“/„Termin“, `liste`, `frage_label` „Leitfrage“/„Ziel im Projekt“, Freigabetexte), Statusbeschriftungen, Startansicht, Lernziele, Organisation, Kontakt, Lizenz. Farben kommen aus einer gemeinsamen Palette: Blöcke `ph1`–`ph4` (hell und dunkel). Farbe bedeutet in der Karte nur „Faden“ (F1–F6); Themengebiete werden über ihre Zeile und Beschriftung unterschieden, ihr Feld `farbe` wird nicht mehr dargestellt.
