wsgi_app =  "fps.wsgi:application"

loglevel = "info"

workers = 2

bind = "0.0.0.0:7000"

reload = True

accesslog = errorlog = "/var/log/gunicorn/devfps.log"

capture_output = True

pidfile = "/var/run/gunicorn/gunicornfps.pid"

daemon = True