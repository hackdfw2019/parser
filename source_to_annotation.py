import re
import sys
from data_types import Annotation, split_var, is_var_char

RESERVED = ["abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while"]

def validate(token):
    if token in RESERVED:
        return False
    for char in token:
        if not is_var_char(char):
            return False
    return True


def source_to_annotation(input_file_name):
    # open the file, and read the lines into an array of strings
    lines = open(input_file_name).readlines()
    results = []

    i = 0
    while i < len(lines):
        line = split_var(lines[i])
        for j, token in enumerate(line):
            if j > 0 and (line[j] == '/' and line[j - 1] == '/'):
                break
            if validate(token):
                results.append({str(token): (i, j)})
        i += 1

    return Annotation(input_file_name, results)
