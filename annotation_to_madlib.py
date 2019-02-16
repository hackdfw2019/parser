import random
from data_types import split_var

var_chars = "abcdefghijklmnopqrstuvwxyz0123456789_____"

def random_var():
    result = ""
    for i in range(0, 8):
        result += random.choice(var_chars)
    return result

def annotation_to_madlib(annotation):
    file_lines = []
    fin = open("samples/" + annotation.name)
    for line in fin:
        file_lines.append(split_var(line))
    for group in annotation.groups:
        var_name = random_var()
        for loc in group:
            file_lines[loc[0]][loc[1]] = var_name
    fout = open("madlibs/" + annotation.name, "wt")
    for file_line in file_lines:
        for token in file_line:
            fout.write(token + " ")
        fout.write("\n")
