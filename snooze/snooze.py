"""

A restful api generator for the lazy

"""

from snooze_exceptions import SnoozeError
from transport import RESTfulRequest
import re

class Snooze(object):
    def __init__(self, domain, uri='', secure=False):
        
        if domain[-1] == '/':
            domain = domain[:-1]
        self.domain = domain
        
        self.uri = uri
        self.secure = secure
        self.kwargs = {}
        self.headers = {}

    def __getattr__(self, name):

        try:
            return object.__getattr__(self, name)
        except AttributeError:
            name = name.replace('_','.')
            return Snooze(self.domain, str(self.uri) + '/' +  str(name), self.secure)

    def __call__(self, _method_='POST', **kwargs):
        self.kwargs = kwargs
        try:
            return object.__call__(self, **kwargs)
        except TypeError:
            return RESTfulRequest(self).send_request(_method_)

    def __getitem__(self, key):
        pos = self.uri.rindex('/',0,-1) # should always find a slash since __getattr__ is called first
        return Snooze(self.domain, self.uri[:pos + 1] + key)

    def __str__(self):
        return str(self.domain) +  str(self.uri) 

if __name__ == '__main__':
    s = Snooze('github.com/api/v2', secure=False)
    s.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5"
    print s.format['json'].user.show.username['knobe'](_method_ = 'GET')
