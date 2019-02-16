class Annotation:
    def __init__(self, name, sets):
        self.name = name
        self.sets = sets

def is_var_char(c):
    return ord('a') <= ord(c) <= ord('z') or \
           ord('A') <= ord(c) <= ord('Z') or \
           ord('0') <= ord(c) <= ord('9') or \
           ord(c) == ord('-') or ord(c) == ord('_')

def is_whitespace(c):
    return ("" + c).isspace()

def split_var(s):
    result = []
    curr_var = ""
    for c in list(s):
        if is_var_char(c):
            curr_var += c
        elif not is_whitespace(c):
            result.append(curr_var)
            result.append("" + c)
            curr_var = ""
    if len(curr_var) > 0:
        result.append(curr_var)
    return result
