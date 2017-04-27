import fire
import copy
from domnibus import Domnibus

class DomnibusMeta(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        allowed_methods = Domnibus.allowed_methods()
        cls.list = cls.ls = ['{} <domain>'.format(am) for am in allowed_methods]

        for method in allowed_methods:
            def get_method(method):
                def execute_method(domain, method):

                    try:
                        return Domnibus(domain)[method]
                    except Exception as e:
                        print('\033[91m' + str(e) + '\033[0m')

                return lambda self, domain: execute_method(domain, method)

            setattr(cls, method, get_method(method))

        return super(DomnibusMeta, cls).__init__(name, bases, attrs)


class DomnibusCLI(object):
    __metaclass__ = DomnibusMeta

def cli():
    fire.Fire(DomnibusCLI)

if __name__ == '__main__':
    cli()
