sudo pkill -f uwsgi -9
cd /data/go2
/data/uwsgi-2.0.18/uwsgi --socket go2.sock --module go2.wsgi --chmod-socket=666 &
disown
cd /data/rang
uwsgi --http 0.0.0.0:5000 -w app:app &
disown
