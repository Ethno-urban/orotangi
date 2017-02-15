Orotangi
========

Your thoughts everywhere 


Installation
------------

```bash
virtualenv orotangi
cd $_
git clone http://github.com/foxmask/orotangi
pip install -r requirements.txt
cd orotangi
./manage.py migrate
./manage.py runserver localhost:8000
./manage.py createsuperuser
```

Data Sample
-----------

to add some tags go to http://localhost:8000/api/orotangi/tags/
to add some books go to http://localhost:8000/api/orotangi/books/

