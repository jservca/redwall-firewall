from flask import Flask, request, jsonify
import importlib
import simplejson as json
#from modules import redgate


app = Flask(__name__)

modules = {
	'dns': 'dnsmasq',
	'interfaces': 'interfaces2',
	'firewall': 'simple-firewall'
}

@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/')
def root():
    return 'Unauthorized Access'

@app.route('/<path:path>', methods=['GET', 'POST'])
def route(path):
    parts = path.split("/")
    mname = parts[0]
    routing = {}
    module = importlib.import_module('modules.' + modules[mname], package=None)
    routing[mname]  = module.Main()
    if len(parts) > 1:
        return jsonify(routing[mname].request(parts[1]))
    else:
        return jsonify(routing[mname].request())
