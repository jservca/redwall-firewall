from flask import Flask, request, jsonify
import importlib
import simplejson as json


app = Flask(__name__)

modules = {
	'dns': 'dnsmasq',
	'interfaces': 'interfaces2',
	'firewall': 'simple-firewall'
}


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
    return jsonify(routing[mname].request())
