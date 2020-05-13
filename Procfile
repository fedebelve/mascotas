web: gunicorn mascotas.wsgi --log-file -
release: DATABASE_URL='postgres://wbrtxcyrqbfbue:a399badc27d8297bedd7d8f75a74ed70d15fa0b33d916e05efa4428ec479c248@ec2-34-198-243-120.compute-1.amazonaws.com:5432/d4f18o0a5noo94' python manage.py test -keepdb
release: python manage.py migrate
