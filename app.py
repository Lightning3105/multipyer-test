import sys
import os
import logging
import shlex
import gunicorn.app.wsgiapp

host = '172.30.122.202' #os.environ.get('OPENSHIFT_DIY_IP', '127.0.0.1')
port = os.environ.get('OPENSHIFT_DIY_PORT', '8080')
print("===STARTING===")
print(os.environ)

# This line
cmd = 'gunicorn -b %s:%d -k "flask_sockets.worker" flaskapp:app' % (host, int(port))
sys.argv = shlex.split(cmd)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%b %d %H:%M:%S]')
os.chdir(os.path.abspath(os.path.dirname(__file__)))
gunicorn.app.wsgiapp.run()
