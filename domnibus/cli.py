import fire
import copy
from domnibus import Domnibus

class DomnibusMeta(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        allowed_methods = Domnibus.allowed_methods()
        cls.list = cls.ls = ['{} <domain>'.format(am) for am in allowed_methods]

        for method in allowed_methods:
            setattr(cls, method, (lambda method: lambda self, domain: Domnibus(domain)[method])(method))

        return super(DomnibusMeta, cls).__init__(name, bases, attrs)


class DomnibusCLI(object):
    __metaclass__ = DomnibusMeta

def cli():
    fire.Fire(DomnibusCLI)

if __name__ == '__main__':
    cli()
