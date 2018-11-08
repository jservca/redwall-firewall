from os.path import dirname, basename, isfile
import glob
import importlib
ms = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in ms if isfile(f) and not f.endswith('__init__.py')]
#print(__all__)
#print(ms)
#for f in ms:
#    if isfile(f) and not f.endswith('__init__.py'):
#        importlib.import_module(basename(f)[:-3])
