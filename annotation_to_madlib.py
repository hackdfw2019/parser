import random
import pickle
import os
from data_types import split_var, Annotation

var_chars = "abcdefghijklmnopqrstuvwxyz0123456789__"
med_words = open(os.path.join(os.path.dirname(__file__), "dict_med.txt"), 'r').readlines()
sho_words = open(os.path.join(os.path.dirname(__file__), "dict_sho.txt"), 'r').readlines()

def random_words():
    rando = random.randint(0, 16)
    if(rando >= 8):
        return random.choice(med_words).rstrip()
    elif(rando >= 6):
        return random.choice(med_words).rstrip().capitalize()
    elif(rando >= 2):
        return random.choice(sho_words).rstrip() + (random.choice(med_words).rstrip()).capitalize()
    else:
        return random.choice(sho_words).rstrip() + "_" + random.choice(med_words).rstrip()


def random_var():
    result = ""
    for i in range(0, 8):
        result += random.choice(var_chars)
    return result


def annotations_to_madlibs():
    annotations = pickle.load(open(os.path.join(os.path.dirname(__file__), "annotations.pickle"), 'rb'))
    for annotation in annotations:
        annotation_to_madlib(annotation)


def annotation_to_madlib(annotation):
    file_lines = []
    fin = open(os.path.join(os.path.dirname(__file__), "samples", annotation.file_name))
    for line in fin:
        file_lines.append(split_var(line))
    for group in annotation.groups:
        var_name = random_words()
        for loc in group:
            file_lines[loc[0]][loc[1]] = var_name
    result = ""
    fout = open("madlibs/" + annotation.file_name, 'w')
    for file_line in file_lines:
        for token in file_line:
            result += token
    fout.write(result)
    return result

def get_candidates(annotation, line, count):
    print(line)
    if line in annotation.reverse:
        reverse = annotation.reverse[line]
        candidates = []
        for i in range(count):
            file_line = split_var(open(os.path.join(os.path.dirname(__file__), "madlibs", annotation.file_name)).readlines()[line])
            for group in reverse:
                var_name = random_words()
                for loc in reverse[group]:
                    file_line[loc] = var_name
                    candidates.append(file_line)
        return candidates
    else:
        return [open(os.path.join(os.path.dirname(__file__), "madlibs", annotation.file_name)).readlines()[line]]
