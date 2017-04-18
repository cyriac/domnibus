import fire
from domnibus import Domnibus

def trigger_method(method, domain=None):
    if method in ['list', 'ls']:
        value = ["{} <domain>".format(r) for r in Domnibus.allowed_methods()]
    else:
        value = Domnibus(domain)[method]
    return value

def cli():
    fire.Fire(trigger_method)

if __name__ == '__main__':
    cli()
