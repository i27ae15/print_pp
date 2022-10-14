from print_pp.logging import PrintSettings, Print, BColors, check_caller_line
import inspect




x = 'hello world'
y = 456
j = 'second helloa'

t = 5


@check_caller_line(show_file=True)
def function_number(number: int):
    return number


def function_to_test():
    y = 123
    Print(y)
    
    
class ClassToTest:
    here = 'j'
    def __init__(self):
        self.z = 987
        self.p = 987
        # Print(self.z)
        
        # callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        callers_local_vars = inspect.getmembers(self)
        
        
        print(callers_local_vars)
        
        
    def get_user_attributes(cls):
        boring = dir(type('dummy', (object,), {}))
        return [item
                for item in inspect.getmembers(cls)
                if item[0] not in boring]
        
        
        
        
ClassToTest()
# function_to_test()