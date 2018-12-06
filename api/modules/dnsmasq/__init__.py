import os
import redgate

class Main():
    def __init__(self):
        self.tpls = redgate.templates()

    def request(self, args=False):
        return {'module': 'DNSMasq'}

    def load_template(self):
        vals = {
            'listen_port':           53, 
            'domain_needed':  'domain-needed', 
            'bogus_priv':     'bogus-priv', 
            'interfaces':     ['enp1s0', 'enp1s8']
        }
        self.tpls.render('dnsmasq/dnsmasq.conf.tpl', vals)

