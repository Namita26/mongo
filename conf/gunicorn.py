"""
All application server level config.
"""


import os


def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

bind = "127.0.0.1:8000"
workers = numCPUs() * 2 + 1 # kept it like this, need to monitor for a day.
backlog = 2048
worker_class ="gevent"
debug = True
daemon = False
pidfile ="/tmp/gunicorn.pid"
logfile ="/tmp/gunicorn.log"
loglevel = 'info'
accesslog = '/tmp/gunicorn-access.log'