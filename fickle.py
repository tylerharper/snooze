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
    def add_function(self, func, name, options):
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
    
        
        return self.function_dict[function_name]['function'](*(sys.argv[2:])) 
            
        if function_name not in self.function_dict:
           raise FunctionDoesNotExist("%s is not a valid action" % function_name) 
        
        if function_option not in self.function_dict[function_name]['options']:
           raise FunctionDoesNotExist("%s is not a valid option for %s")
        
         
