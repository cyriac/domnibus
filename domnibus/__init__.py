from .exceptions import *
from .operations import *
import collections

class Domnibus(DomnibusOperationMixin):
    FUNC_PREFIX = '_get_value_for_'

    def __init__(self, domain):
        self.domain = domain
        self._data = {}

    def __getitem__(self, method):
        return self._get_and_save_data(method)

    def __getattr__(self, method):
        if method in self.allowed_methods():
            attr = self[method]
        else:
            attr = super(Domnibus, self).__getattr__(method)
        return attr

    @classmethod
    def allowed_methods(cls):
        allowed_methods = set()

        for func in dir(cls):
            if func.startswith(cls.FUNC_PREFIX) and isinstance(getattr(cls, func), collections.Callable):
                func_name = func.lstrip(cls.FUNC_PREFIX)
                allowed_methods.add(func_name)

        return allowed_methods

    def _get_and_save_data(self, key):
        if key in self.allowed_methods():

            if key not in self._data:
                value, store = getattr(self, '{}{}'.format(self.FUNC_PREFIX, key))()
                if store:
                    self._data[key] = value
            else:
                value = self._data[key]

            return value

        else:
            raise DomnibusMethodError("Method '{}' not implemented".format(key))

