# Django Livello Tre

Progetto didattico Django che copre: ModelForm, Form personalizzati,
autenticazione nativa, password reset, crispy-forms con Bootstrap 5.

## Requisiti

- Python 3.10+
- Django 5.x

## Installazione

```bash
git clone https://github.com/tuouser/django_livello_tre.git
cd django_livello_tre
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # poi modifica la SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## App incluse

- `blog`: editor post con ModelForm
- `contact`: form di contatto con persistenza su DB
- `forms_app`: registrazione utente, form di contatto non persistente