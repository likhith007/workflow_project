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

# Large chunk of repetitive code
def repetitive_code_example():
    for i in range(10):
        print("Iteration:", i)
        # ...
        # Many lines of repetitive code here
        # ...
        print("End of iteration:", i)

# Poorly organized and long function
def poorly_organized_function():
    var1 = 1
    var2 = 2
    var3 = 3

    if var1 > var2:
        # Many lines of code here
        # ...
        # ...
        # ...

    elif var2 < var3:
        # Many lines of code here
        # ...
        # ...
        # ...

    else:
        # Many lines of code here
        # ...
        # ...
        # ...

    # More lines of code...

# Overuse of global variables
global_variable = 0

def function_with_global_variable():
    global global_variable
    global_variable += 1

def another_function_with_global_variable():
    global global_variable
    global_variable -= 1

# Long function with excessive branching
def function_with_excessive_branching(param):
    if param == 1:
        # Many lines of code here
        # ...
        # ...
        # ...

    elif param == 2:
        # Many lines of code here
        # ...
        # ...
        # ...

    elif param == 3:
        # Many lines of code here
        # ...
        # ...
        # ...

    else:
        # Many lines of code here
        # ...
        # ...
        # ...

# Poorly named variables and unclear logic
def poorly_named_variables():
    x = 5
    y = 3

    z = (x + y) * (x - y) + (x * y)

    if z > 20:
        return True
    else:
        return False

# Many lines of commented-out code
# ...
# ...
# ...
# ...
# ...
# ...
# ...

# Inefficient algorithm or operation
def inefficient_algorithm(n):
    result = 0
    for i in range(n):
        result += i
    return result

# Poorly formatted code
def poorly_formatted_code(): return True if 5 > 3 else False

# Excessive nesting
