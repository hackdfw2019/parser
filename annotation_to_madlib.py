import random
import pickle
from data_types import split_var

var_chars = "abcdefghijklmnopqrstuvwxyz0123456789__"
med_words = open("dict_med.txt", 'r').readlines()
sho_words = open("dict_sho.txt", 'r').readlines()

def random_words(): # returns a 5-8 character word
    rando = random.randint(0, 11)
    if(rando >= 3):
        return random.choice(med_words).rstrip()
    else:
        return random.choice(sho_words).rstrip() + "_" + random.choice(med_words).rstrip()


def random_var():
    result = ""
    for i in range(0, 8):
        result += random.choice(var_chars)
    return result


def annotations_to_madlibs():
    annotations = pickle.load(open("annotations.pickle", 'rb'))
    for annotation in annotations:
        annotation_to_madlib(annotation)


def annotation_to_madlib(annotation):
    file_lines = []
    fin = open("samples/" + annotation.file_name)
    for line in fin:
        file_lines.append(split_var(line))
    for group in annotation.groups:
        var_name = random_words()
        for loc in group:
            file_lines[loc[0]][loc[1]] = var_name
    result = ""
    for file_line in file_lines:
        for token in file_line:
            result += token
    return result

