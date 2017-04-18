import fire
from domnibus import Domnibus

def trigger_method(method, domain=None):
    if method == 'list':
        return Domnibus.allowed_methods()
    return Domnibus(domain)[method]

def cli():
    fire.Fire(trigger_method)

if __name__ == '__main__':
    cli()
