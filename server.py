import xmlrpclib
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

SERVER_IP = 'localhost'
SERVER_PORT = '8080'
API_KEY = 'some_key'
API_SECRET = 'sshhhh'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/do_api_call/<module>/<command>')
def do_api_call(module, command):
    proxy = xmlrpclib.ServerProxy("http://{}:{}/api/{}/{}/{}").format(SERVER_IP, SERVER_PORT, API_KEY, API_SECRET, module)
    proxy_module = getattr(proxy, module)
    module_command = getattr(proxy_module, command)
    module_command()
    return Response('done')


if __name__ == '__main__':
    app.run(port=8000)