# SWP

> `Student Web Portal`. The application develop for university final project purpose.

##### Dependencies

- Python 3.10
- Django 4.1.0
- Postgres  13.0

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop 
on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.


#### Setup

```bash
git clone https://github.com/mbrsagor/swp.git
cd swp
```

###### Then copy code from the ``.env_example`` and create new file `.env` then pasts

-------------------------------------------
```bash
|--> env_example
|--> .env
```

Run the application in your local development server:

```bash
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./mangae.py runserver
```