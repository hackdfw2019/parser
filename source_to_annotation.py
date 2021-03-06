#!/usr/sbin/python

import re
import sys
from data_types import Annotation, split_var, is_var_char
import pickle
import os

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
    lines = open(os.path.join(os.path.dirname(__file__), 'samples', input_file_name)).readlines()
    results = {}

    i = 0
    while i < len(lines):
        line = split_var(lines[i])
        for j, token in enumerate(line):
            if j > 0 and (line[j] == '/' and line[j - 1] == '/'):
                break
            if validate(token):
                if token in results:
                    results[token].append((i, j))
                else:
                    results[token] = [(i, j)]
        i += 1

    groups = list(results.values())
    reverse_index = {}
    for var, group in enumerate(groups):
        for location in group:
            line = location[0]
            col = location[1]
            if line in reverse_index:
                if var in reverse_index[line]:
                    reverse_index[line][var].append(col)
                else:
                    reverse_index[line][var] = [col]
            else:
                reverse_index[line] = {}
                reverse_index[line][var] = [col]
    return Annotation(input_file_name, groups, reverse_index)


def generate_annotations():
    file_names = os.listdir('samples/')
    annotations = []
    for file_name in file_names:
        annotations.append(source_to_annotation(file_name))
    pickle.dump(annotations, open(os.path.join(os.path.dirname(__file__), "annotations.pickle"), 'wb'))
