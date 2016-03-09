import sys

class _capivara(object):

    def __init__(self, arg):
        super(_capivara, self).__init__()
        self.arg = arg

    def __call__(self, func):
        return True


def get_DOM(page=None):
    if not page:
        raise TypeError(('get_DOM() expected string type, '
            'but got type {0}.').format(type(page)))

    return _capivara(page)
