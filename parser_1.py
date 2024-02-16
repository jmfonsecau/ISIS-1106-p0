import re

def tokenize(input_text):
    return re.findall(r'\(|\)|[^()\s]+', input_text)

def is_valid_program(tokens):
    defined_vars = set()

    defined_functions = {}

    def is_variable_defined(variable):
        return variable in defined_vars

    def is_function_valid(function_name, parameters):
        if function_name not in defined_functions:
            return False
        expected_params = defined_functions[function_name]
        if len(expected_params) != len(parameters):
            return False
        for param in parameters:
            if not is_variable_defined(param) and not param.isdigit():
                return False
        return True

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.lower() == 'defvar':
            if i + 3 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 3] == ')':
                return False
            defined_vars.add(tokens[i + 1])
            i += 3

        elif token.lower() == 'defun':
            if i + 5 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 3] == '(' or tokens[i + 4] == ')' or tokens[i + 5] == ')':
                return False
            function_name = tokens[i + 1]
            params = tokens[i + 3].split()
            defined_functions[function_name] = params
            i += 6

        elif token.lower() == 'if':
            if i + 6 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 6] == ')' or tokens[i + 3] == '(' or tokens[i + 4] == '(':
                return False
            i += 7

        elif token.lower() == 'repeat':
            if i + 5 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 5] == ')' or tokens[i + 3] == '(':
                return False
            i += 6

        elif token.lower() == '(':
            block_count = 1
            i += 1
            while block_count > 0 and i < len(tokens):
                if tokens[i] == '(':
                    block_count += 1
                elif tokens[i] == ')':
                    block_count -= 1
                i += 1
            if block_count > 0:
                return False

        elif token.lower() == 'run-dirs':
            if i + 3 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 3] == ')':
                return False
            i += 4

        elif token.lower() == 'defun':
            if i + 5 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 3] == '(' or tokens[i + 4] == ')' or tokens[i + 5] == ')':
                return False
            i += 6

        elif token.lower() == 'if':
            if i + 6 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 6] == ')' or tokens[i + 3] == '(' or tokens[i + 4] == '(':
                return False
            i += 7

        elif token.lower() == 'repeat':
            if i + 5 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 5] == ')' or tokens[i + 3] == '(':
                return False
            i += 6

        elif token.lower() == '(':
            block_count = 1
            i += 1
            while block_count > 0 and i < len(tokens):
                if tokens[i] == '(':
                    block_count += 1
                elif tokens[i] == ')':
                    block_count -= 1
                i += 1
            if block_count > 0:
                return False

        elif token.lower() == 'run-dirs':
            if i + 3 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 3] == ')':
                return False
            i += 4

        else:
            if i + 2 >= len(tokens) or tokens[i + 1] == '(' or tokens[i + 2] == ')':
                return False
            if not is_variable_defined(token) and not is_function_valid(token, tokens[i + 2:]):
                return False
            i += 3

    return True

def main():
    with open("instrucciones.txt", "r") as file:
        input_text = file.read()

    tokens = tokenize(input_text)

    if is_valid_program(tokens):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
