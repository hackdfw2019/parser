class Annotation:
    def __init__(self, name, sets):
        self.name = name
        self.sets = sets

def is_var_char(c):
    return ord('a') <= ord(c) <= ord('z') or \
           ord('A') <= ord(c) <= ord('Z') or \
           ord('0') <= ord(c) <= ord('9') or \
           ord(c) == ord('_')

def split_var(s):
    result = []
    curr_var = ""
    for c in list(s):
        if is_var_char(c):
            curr_var += c
        elif str(c).isspace():
            if len(curr_var) > 0:
                result.append(curr_var)
            curr_var = ""
        else:
            if len(curr_var) > 0:
                result.append(curr_var)
            curr_var = ""
            result.append(str(c))
    if len(curr_var) > 0:
        result.append(curr_var)
    return result
