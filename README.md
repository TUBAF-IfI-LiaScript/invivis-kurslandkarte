# invivis Kurslandkarte

_Autoren: Sebastian Zug & Claude Code (Opus 5.5)_

Gemeinsamer Kern der Kurslandkarten im Projekt **invivis**: eine interaktive Übersicht für Studierende über Termine, Begriffe, Zusammenhänge und didaktische Fäden eines Kurses – dazu eine Startseite und auf Wunsch Orientierungsfolien in den LiaScript-Materialien. Jeder Kurs liefert nur seine Daten; Prüfung, Darstellung und Verbesserungen leben hier an einer Stelle.

Genutzt von:

| Kurs | Karte | Besonderheit |
| :--- | :---- | :----------- |
| Erhebung, Analyse und Visualisierung digitaler Daten (EAVD) | [Karte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) | strenge Freigabe (`vorschau="keine"`), PDF-Links |
| Digitale Systeme / Eingebettete Systeme | [Karte](https://tubaf-ifi-liascript.github.io/VL_EingebetteteSysteme/kurslandkarte/) | Seiten aus der Repo-Wurzel |
| Robotik (VL, Ü, P) | [Karte](https://tubaf-ifi-liascript.github.io/VL_SoftwareprojektRobotik/kurslandkarte/) | drei Termintypen, Orientierungsfolien (`folien=True`) |

## Ansichten

* **Vorlesungen / Termine:** Wochenraster nach Blöcken; Spalten für die Termintypen, die im Kurs vorkommen (VL, Ü, P). Jede Kachel: Leitfrage bzw. Ziel im Projekt, Begriffe als Chips, angewandte Begriffe („wendet an“), Anwendungen, Links auf Folien und PDF. Standard auf dem Handy.
* **Metrokarte:** didaktische Fäden als Linien über die Zeit.
* **Zeitleiste:** alle Begriffe nach Themengebiet mit Pfeilen für ihre Beziehungen.

„Sie sind hier“ folgt dem Datum. Begriffe erscheinen nach ihrer Freigabe; `vorschau="ausblick"` zeigt vorbereitete Begriffe auf Wunsch blass, `vorschau="keine"` lässt sie gar nicht erst in die Seite.

Direktlinks: `…/kurslandkarte/#termin=<key>`, `#begriff=<id>`, `#ansicht=liste|metro|zeit` (kombinierbar mit `&`).

## Dateien

| Datei | Inhalt |
| :---- | :----- |
| `kern.py` | Prüfung der Daten, Erzeugung von `kurslandkarte.json`, Karte, Startseite und Orientierungsfolien |
| `vorlage.html` | Karte; `%%…%%` füllt `kern.py` |
| `startseite.html` | Startseite des Kurses („Diese Woche“, Kurslandkarte, Lernziele, Organisation, Kontakt) |
| `uebernehmen.py` | kopiert den Kern nach `<kurs>/kurslandkarte/invivis/` |
| `VERSION` | Version des Kerns; steht in jeder erzeugten Seite |

## Einen Kurs anbinden oder aktualisieren

```bash
python3 uebernehmen.py ../VL_Robotik/VL_SoftwareprojektRobotik   # Kern in den Kurs kopieren
cd ../VL_Robotik/VL_SoftwareprojektRobotik && python3 kurslandkarte/erzeuge.py
```

Die Kursdatei `kurslandkarte/erzeuge.py` enthält nur Daten und ruft `kern.erzeuge(...)` auf. Datenformate und Parameter stehen im Kopf von `kern.py`. Verbesserungen immer hier machen, `VERSION` erhöhen und an alle Kurse verteilen – Änderungen in `kurslandkarte/invivis/` eines Kurses werden beim nächsten Übernehmen überschrieben.

## Kursspezifisches

Alles Kursspezifische steht im `KURS`-Wörterbuch der Kursdatei: Titel, Links (LiaScript, Pages, Repository), Wortwahl (`einheit` „Vorlesung“/„Termin“, `liste`, `frage_label` „Leitfrage“/„Ziel im Projekt“, Freigabetexte), Statusbeschriftungen, Startansicht, Lernziele, Organisation, Kontakt, Lizenz. Farben kommen aus einer gemeinsamen Palette: Blöcke `ph1`–`ph4`, Themengebiete `c1`–`c7` (jeweils hell und dunkel).
