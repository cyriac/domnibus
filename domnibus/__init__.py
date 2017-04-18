from .exceptions import *
from .operations import *

class Domnibus(DomnibusOperationMixin):
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
                value, store = getattr(self, '{}{}'.format(self.FUNC_PREFIX, key))()
                if store:
                    self._data[key] = value
            else:
                value = self._data[key]

            return value

        else:
            raise DomnibusMethodError("Method '{}' not implemented".format(key))

