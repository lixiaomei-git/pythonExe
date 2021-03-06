class LoggedMappingMixin:
    __slots__ = ()
    def __getitem__(self, key):
        print('Getting ',str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ',str(key))
        return super().__delitem__(key)

class SetOnceMappingMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key),' already set')
        return super().__setitem__(key, value)

class StringKeyMappingMixin:
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


