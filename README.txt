### Installation

```
cd path/to/Jeopardly
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```
cd jeopardlysite
python manage.py migrate
python manage.py runserver
```

Navigate to `localhost:8000/jeopardly`
