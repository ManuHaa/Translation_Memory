# TranslationMemory
engl. version below

Dieses Repository beinhaltet ein Terminal Script Tool basierend auf Python.

## Ordnerstruktur
### database - Datenverwaltung
Die Daten werden in folgenden JSON Files gespeichert:
- generalDB.json: beinhaltet alle registrierten Wörter mit zusätzlichen Daten
- languagesDB.json: beinhaltet alle registrierten Sprachen 
- policiesDB.json: beinhaltet die registrierten User mit deren Berechtigungen für die Verwendung von Sprachen
- registeredUsersDB.json: beinhaltet alle registrierten User mit deren Username und Passwort
- wordsDB.json: beinhaltet die Anzahl von angelegten und üebrsetzten Wörter der User

### obj - Objekte (Instanzen)
Folgende Objekte wurden für die Umsetzung implementiert:
- admin.py: Administrator mit erweiterten Funktionen
- authentication.py: enthält Anmeldeoptionen für die Loginmaske
- colors.py: enthält Farbcodes für den Dialog mit dem Terminal
- translator.py: Übersetzer als Kind vom User mit erweiterten Funktionen
- user.py: Benutzer mit Standardfunktionen

### operator -  Operatoren
Folgende Operatoren wurden für die Umsetzung implementiert:
- adminOperator.py: enthält alle Dialogfunktionen des Admins und erzeugt dessen Instanz
- loginOperator.py: enthält die Loginmaske und verwendet die Instanz der Authentication 
- translatorOperator.py: enthält alle Dialogfunktionen des Übersetzers und erzeugt dessen Instanz
- userOperator.py: enthält alle Dialogfunktionen des Benutzers und erzeugt dessen Instanz

### pattern - Design Patterns
Folgende Pattern wurden in dem Projekt verwendet:
- null_object.py
- singleton.py

### exec.py - Ausführung der Applikation
Die Applikation wird in diesem File definiert und verwendet die oben genannten Operatoren.


## Einsteig

### 1. Applikation starten
Wechseln Sie in folgendes Verzeichnis:
``` /Translation_Memory/app ```

Starten Sie die Applikation:
``` python3 exec.py ```

### 2. Anmelden oder Fortfahren
Die Applikation wird fragen ob sie sich anmelden möchten. Falls das der Fall ist können Sie folgende User verwenden:

- Admin
``` username: admin ```
``` password: 12345 ```

- Übersetzer 1
``` username: translator123 ```
``` password: 123 ```

- Übersetzer 2
``` username: superdupernator```
``` password: sdp2 ```

Falls Sie als Benutzer fortfahren möchten benötigen Sie keine Anmeldung.

### 3. Start
Probieren Sie die Optionen der Benutzer aus:
- Wörter anlegen
- Übersetzungen einpflegen
- Sprachen zuweisen 
- etc ...

Viel Spaß ;)






# Translation_Memory
This repository contains a translation memory script tool written in python. 

## Folder Structure
