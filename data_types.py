class Annotation:
    def __init__(self, file_name, groups, reverse):
        self.file_name = file_name
        self.groups = groups  # a list of lists
        self.reverse = reverse


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
        else:
            if len(curr_var) > 0:
                if curr_var == "import" or curr_var == "package":
                    return ""
                else:
                    result.append(curr_var)
            curr_var = ""
            result.append(str(c))
    if len(curr_var) > 0:
        result.append(curr_var)
    return result
