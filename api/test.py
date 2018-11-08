import importlib
mname = 'firewall'

routing = {}
module = importlib.import_module('modules.' + mname, package=None)
routing[mname]  = module.Main()
print(routing[mname].list())

