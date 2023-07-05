# Unused parameters in functions
def function_with_unused_parameters(param1, param2):
    return param1

def another_function_with_unused_parameters(param1, param2):
    return param2

# Worst declaration of classes
class BadlyNamedClass:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0

    def bad_method(self, unused_param):
        return self.var1 + self.var2

class AnotherBadlyNamedClass:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0

    def another_bad_method(self, unused_param):
        return self.var1 - self.var2

# Other code smells
def function_with_long_name_and_many_lines_of_code():
    variable_with_a_very_long_name = 1
    another_variable_with_a_very_long_name = 2

    result = variable_with_a_very_long_name + another_variable_with_a_very_long_name
    if result > 10:
        return True
    else:
        return False

def function_with_duplicate_code():
    variable1 = 1
    variable2 = 2

    result1 = variable1 + variable2
    result2 = variable1 + variable2

    return result1, result2
