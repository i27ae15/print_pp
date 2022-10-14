from print_pp.logging import PrintSettings, Print, BColors, check_caller_line
import inspect


s = PrintSettings()
s._logs_color = BColors.OKBLUE

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
        Print(self.z)
        

        
    def get_user_attributes(cls):
        boring = dir(type('dummy', (object,), {}))
        return [item
                for item in inspect.getmembers(cls)
                if item[0] not in boring]
        
        
        
        
ClassToTest()
# function_to_test()