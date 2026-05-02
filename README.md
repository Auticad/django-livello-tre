# Django Livello Tre — Blog, Forms e Registrazione Utenti
 
Progetto Django che consolida i concetti intermedi del framework:
modelli con `ModelForm`, form personalizzati con validazione custom,
registrazione utenti tramite `UserCreationForm`, e gestione
sicura della configurazione con `python-decouple`.
 
---
 
## App e funzionalità
 
Il progetto è organizzato in tre app distinte, ognuna focalizzata su un concetto specifico.
 
### `blog`
 
Semplice editor di post del blog. Dimostra l'uso di `ModelForm` legato
al modello `BlogPost`, con campi `title`, `content` e `draft`.
La view gestisce correttamente i branch GET/POST e il salvataggio del form.
 
### `contact`
 
Form di contatto collegato al modello `ContactMessage` tramite `ModelForm`.
I messaggi vengono persistiti nel database. I campi coprono nome,
email, oggetto e testo del messaggio.
 
### `forms_app`
 
App più ricca, con due form indipendenti:
 
- `RegisterForm` — estende `UserCreationForm` di Django per la registrazione
  di nuovi utenti con username, email e password.
- `ContactForm` — form generico (non legato a un modello) con validazione
  custom sul campo `content`: blocca parole vietate tramite `clean_content()`.
Le view includono `HomeTemplateView` (CBV con `TemplateView`) e due FBV
per la registrazione e il contatto.
 
---
 
## Stack tecnologico
 
| Componente | Tecnologia |
|---|---|
| Backend | Python 3.11, Django 5.2 |
| Database | SQLite (sviluppo) |
| Frontend | HTML5, Bootstrap 5 |
| Form | django-crispy-forms + crispy-bootstrap5 |
| Configurazione | python-decouple |
| Autenticazione | django.contrib.auth |
 
---
 
## Struttura del progetto
 
```
django-livello-tre/
├── blog/               # Editor di post con ModelForm
├── contact/            # Form di contatto con salvataggio su DB
├── forms_app/          # Registrazione utenti e form con validazione custom
├── django_livello_tre/ # Configurazione Django (settings, urls, wsgi, asgi)
├── templates/          # Template base e registrazione
├── manage.py
├── requirements.txt
├── .env.example        # Template variabili d'ambiente
└── .gitignore
```
 
---
 
## Installazione locale
 
### Prerequisiti
 
- Python 3.10 o superiore
- pip
### Passaggi
 
```bash
# 1. Clona il repository
git clone https://github.com/Auticad/django-livello-tre.git
cd django-livello-tre
 
# 2. Crea e attiva un ambiente virtuale
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
 
# 3. Installa le dipendenze
pip install -r requirements.txt
 
# 4. Crea il file .env copiando l'esempio
cp .env.example .env
# Poi modifica .env e inserisci una SECRET_KEY valida
 
# 5. Applica le migrazioni
python manage.py migrate
 
# 6. Avvia il server di sviluppo
python manage.py runserver
```
 
L'applicazione sarà disponibile su `http://127.0.0.1:8000/`.
 
---
 
## Variabili d'ambiente
 
Il progetto utilizza `python-decouple` per separare la configurazione
dal codice. Il file `.env` non viene mai committato. Usa `.env.example`
come punto di partenza:
 
```ini
SECRET_KEY=cambia-questa-chiave-con-una-sicura
DEBUG=True
```
 
Per generare una `SECRET_KEY` casuale:
 
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
 
---
 
## Concetti dimostrati
 
Il progetto copre in modo progressivo i seguenti argomenti:
 
- `ModelForm` e salvataggio diretto da form a database
- Form non legato a un modello con validazione custom (`clean_<field>`)
- `UserCreationForm` per la registrazione utenti
- Class-based view (`TemplateView`) affiancata a function-based view
- Separazione della configurazione con `python-decouple` e file `.env`
- Template bootstrap con `crispy-forms`
- Struttura multi-app con namespace di template separati
---
 
## Note
 
Progetto didattico a scopo di apprendimento.
Non destinato al deployment in produzione nella configurazione attuale.
Le aree di possibile estensione includono: autenticazione completa
con login/logout, API REST con Django REST Framework,
e test automatizzati con `pytest-django`.
 
---
 
## Licenza
 
Distribuito senza licenza esplicita. Uso libero a scopo didattico e di studio.
