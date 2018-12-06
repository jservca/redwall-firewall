import  yaml
import jinja2
#from jinja2 import Environment, PackageLoader, select_autoescape

#http://jinja.pocoo.org/docs/2.10/api/#basics

class config():

    def __new__(self):
        with open("/opt/redgate/api/config.yml", 'r') as cfgfile:
            self.cfg = yaml.load(cfgfile)
        return self.cfg

# Global access to sqlitedb
class reddb():

    def load(self, q):
        return ""

class templates():

        def __init__(self):
                    self.cfg = config()
                    self.env = jinja2.Environment(
                                loader=jinja2.FileSystemLoader( 
                                    self.cfg['application']['templates_dir']
                                )
                            )


        def render(self, tpl, values = None):
            #print(self.cfg['application']['templates_dir'] + tpl)
            template = self.env.get_template(tpl)
            return template.render(**values)



