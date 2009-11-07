import urllib
import urllib2
from raft_exceptions import RaftError

class Transport(object):
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
        self.url = beg + model.domain + model.uri
        self.response = ''
        self.encoded_args = urllib.urlencode(model.kwargs)
        
    def send_response(self, method):
        if method.lower() == 'post':
            req = urllib2.Request(self.url, self.encoded_args)
            self.response = urllib2.urlopen(req).read()
        elif method.lower() == 'get':
            url = self.url + '?' + self.encoded_args
            req = urllib2.Request(self.url)
            self.response = urllib2.urlopen(req).read()   
        else:
            raise RaftError('%s is an unknown method we use either get or post requests' % method)

        return self.response
    
