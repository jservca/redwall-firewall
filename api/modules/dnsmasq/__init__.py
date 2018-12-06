import os
from modules import redgate

class Main():
    def __init__(self):
        self.tpls = redgate.templates()

    def request(self, args=False):
        if not args:
            return {'module': 'DNSMasq'}
        else:
            return self.load_template()

    def load_template(self):
        vals = {
            'listen_port':           53, 
            'domain_needed':  'domain-needed', 
            'bogus_priv':     'bogus-priv', 
            'interfaces':     ['enp1s0', 'enp1s8']
        }
        return self.tpls.render('dnsmasq/dnsmasq.conf.tpl', vals)

