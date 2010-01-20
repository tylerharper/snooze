import urllib
import urllib2
from snooze_exceptions import SnoozeError

class RESTfulRequest(object):
    """
    This sends the request out to server and returns the raw response.
    No formatting here.
    """
    def __init__(self, model):
        self.model = model
        if model.secure:
            beg = 'https://'
        else:
            beg = 'http://'
       
        pop_values = [] 
        for x in model.kwargs:
            if model.kwargs[x] is None:
                pop_values.append(x)

        for x in pop_values:
            model.kwargs.pop(x)

        self.url = beg + model.domain + model.uri
        self.headers = model.headers
        self.response = ''
        self.encoded_args = urllib.urlencode(model.kwargs)
        
    def send_request(self, method):
        if method.upper() == 'POST':
            req = urllib2.Request(self.url, self.encoded_args, self.headers)
            self.response = urllib2.urlopen(req).read()
        elif method.upper() == 'GET':
            url = self.url + '?' + self.encoded_args
            req = urllib2.Request(self.url, None, self.headers)
            self.response = urllib2.urlopen(req).read()
        else:
            raise SnoozeError('%s is an unknown method. we use either get or post requests' % method)

        return self.response
    
