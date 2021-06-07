accesslog = "-"
access_log_format = (
    '%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)
bind = "0.0.0.0:6565"
capture_output = True
chdir = "/app"
errorlog = "-"
keepalive = 60
worker_class = "gevent"
worker_tmp_dir = "/dev/shm"
workers = 1