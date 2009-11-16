"""

This will allow you to add a function 
to be called from the command line

"""
import sys


class FunctionDoesNotExist(Exception):
    """Called if the function you added does not exist"""
    pass
    

class Fickle(object):
    def __init__(self):
        self.function_dict = {}
    def add_function(self, func, name=None, options=[]):
        if name is None:
            name = func.func_name

        self.function_dict[name] = {'function': func, 'options' : options}
    
    def run_fickle(self):
        function_name = sys.argv[1]
        function_option = ''
        function_option_value = ''

        if len(sys.argv) == 3:
            function_option = ''
            function_option_value = sys.argv[2]
        elif len(sys.argv) > 3:    
            function_option = sys.argv[2]
            function_option_value = sys.argv[3]
    
        
        return_value = None
        try:
            return_value = self.function_dict[function_name]['function'](*(sys.argv[2:])) 
        except KeyError:
            print 'No such action: %s' % function_name
        except TypeError, error:
            #TODO Figure out how to get the correct number of args
            print 'Not the correct number of options'
        
        return return_value
        if function_option not in self.function_dict[function_name]['options']:
           raise FunctionDoesNotExist("%s is not a valid option for %s")
        
         
