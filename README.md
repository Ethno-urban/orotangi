Orotangi
========

Your Thoughts, Everywhere 


Installation
------------

```bash
python3.6 -m venv orotangi
cd $_
git clone http://github.com/foxmask/orotangi
pip install -r requirements.txt
cd orotangi
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver localhost:8001 &
```

Data Sample
-----------

after logged in from http://localhost:8001/

* to add some books go to http://localhost:8001/api/orotangi/books/

