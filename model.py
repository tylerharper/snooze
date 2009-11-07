"""

Restful Api Framework Tada - raft

"""

from raft_exceptions import RaftError

class Model(object):
    def __init__(self, domain, uri='', secure=False):
        self.domain = domain
        self.uri = uri
        self.secure = secure
        self.kwargs = {}

    def __getattr__(self, name):

        try:
            return object.__getattr__(self, name)
        except AttributeError:
            return Model(self.domain, self.uri + '/' +  name)

    def __call__(self, *args, **kwargs):
        try:
            return object.__call__(self, *args, **kwargs)
        except TypeError:
            kwargs = kwargs
            pos = self.uri.rindex('/',0,-1) # should always find a slash since __getattr__ is called first
            return Model(self.domain, self.uri[:pos + 1] + args[0])

    def __str__(self):
        return str(self.domain) +  str(self.uri) 

    def add_prefix(self, prefix):
        """
        
        Action - Adds a prefix to a the beginning of the current uri

        Returns - new instance of Model, but it also add the prefix to
        the current Model's uri.  This allows for a call that has 

           raft.add_prefix('somthing.somthingelse') 
                           or 
           raft.add_prefix('something.somethingelse').another.part
        """
        num_slash = prefix.count('/') 
        num_dot = prefix.count('.')
        if num_dot > 0 and num_slash > 0:
            raise RaftError('There should be either slashes or dots not' +
                            ' both in a prefix. Prefix is %s' % prefix)
        else:
            trans_prefix = prefix.replace('.', '/')
            if trans_prefix[0] != '/':
                trans_prefix = '/' + trans_prefix
            if trans_prefix[-1] == '/':
                trans_prefix = trans_prefix[:-1]
        
            self.uri = trans_prefix + self.uri
        
        return Model(self.domain, self.uri)
