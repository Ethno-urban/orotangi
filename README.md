Orotangi
========

Your Thoughts, Everywhere 


Installation
------------

```bash
virtualenv orotangi
cd $_
git clone http://github.com/foxmask/orotangi
pip install -r requirements.txt
cd orotangi
./manage.py migrate
./manage.py runserver localhost:8001
./manage.py createsuperuser
```

Data Sample
-----------

* to add some books go to http://localhost:8001/api/orotangi/books/

