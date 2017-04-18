class DomnibusMethodError(Exception):
    pass

class Domnibus(object):
    FUNC_PREFIX = '_get_value_for_'
    def __init__(self, domain):
        self.domain = domain
        self._data = {}
        self.allowed_methods = set()

        # Discover and attach supported functions
        for func in dir(self):
            if func.startswith(self.FUNC_PREFIX) and callable(getattr(self, func)):
                func_name = func.lstrip(self.FUNC_PREFIX)
                self.allowed_methods.add(func_name)

    def __getitem__(self, method):
        return self._get_and_save_data(method)

    def __getattr__(self, method):
        if method in self.allowed_methods:
            attr = self[method]
        else:
            attr = super(Domnibus, self).__getattr__(method)
        return attr

    def _get_and_save_data(self, key):
        if key in self.allowed_methods:

            if key not in self._data:
                self._data[key] = getattr(self, '{}{}'.format(self.FUNC_PREFIX, key))()
            return self._data[key]

        else:
            raise DomnibusMethodError("Method '{}' not implemented".format(key))

    def _get_value_for_whois(self):
        import whois
        return whois.whois(self.domain)

    def _get_value_for_ssl(self):
        import ssl, socket

        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=self.domain)
        s.connect((self.domain, 443))
        return s.getpeercert()


# from domnibus import Domnibus; d=Domnibus('google.com')
