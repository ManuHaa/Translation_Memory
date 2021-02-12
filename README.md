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


# ----------------------------------------------------------------------------------------  
#
This repository contains a translation memory script tool written in python. 

## Folder Structure
### database - data storage
The application data is stored in following files:
- generalDB.json: contains all registered words with additional data
- languagesDB.json: contains all registered languages
- policiesDB.json: contains the registered users with their entitlements
- registeredUsersDB.json: contains all registered users with their username and password
- wordsDB.json: contains the number of added and translated words of each user

### obj - objects (intsances)
Following objects wehre implemented for the application:
- admin.py: admin with his functionality
- authentication.py: contains login functionality
- colors.py: contains color codes for the terminal dialogs
- translator.py: child class of user with own functionality
- user.py: user with base default functionality

### operator -  operators
Following operators where implemented for the application:
- adminOperator.py: contains dialog functionality of the admin object and creates its instance
- loginOperator.py: contains login mask and uses the authentication instance
- translatorOperator.py: contains dialog functionality of the translator object and creates its instance
- userOperator.py: contains dialog functionality of the user object and creates its instance

### pattern - Design Patterns
Following design patterns where used in this project:
- null_object.py
- singleton.py

### exec.py - Execution of application
The application gets started here and uses all aforementioned parts.


## Getting started

### 1. start the application
navigate to the following directory:
``` /Translation_Memory/app ```

start the application:
``` python3 exec.py ```

### 2. login or continue
For using the admin or translator functionalities you can sign in with following accounts:

- admin
``` username: admin ```
``` password: 12345 ```

- translator 1
``` username: translator123 ```
``` password: 123 ```

- translator 2
``` username: superdupernator```
``` password: sdp2 ```

You don't need to sign in for the user functionalities, just continue.

### 3. start
try the diverse optionalities of all users:
- create words
- add translations
- assign languages 
- etc ...

have fun ;)

