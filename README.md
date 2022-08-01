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

## authenticate
   1. login 
   2. logout

## Teacher
 1. class routine
    1. add
    2. update
    3. delete
   
 2. marks all
    1. add mark
    2. update
    3. delete
 
 3. book
    1. add
    2. update
    3. delete

## Student
   1. register
   2. profile update
   3. all marks see
   4. certificate
      1. name
      2. image
      3. add, update, delete
   

## Admin
   1. teacher
   2. student
   3. Notice

   4. Financial data
      1. student
      2. semister
      3. paid
      4. unpaid