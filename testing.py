from print_pp.logging import PrintSettings, Print, BColors, check_caller_line
x = 'hello world'
y = 456
j = 'second hello'

t = 5


@check_caller_line(show_file=True)
def function_number(number: int):
    return number



print(function_number(5))


# print(p.value_one)
# l.testing()


# parent = Parent()
# child = Child()
# # parent.valueA = 15

# print(child.valueA)

# child.Calculate()

# def function_to_test():
#     y = 123
#     Print(y)
    
# class ClassToTest:
#     def __init__(self):
#         self.z = 987
#         Print(self.z)
        
        
# function_to_test()
# ClassToTest()