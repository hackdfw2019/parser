import random
import

import data_types

annotations = [data_types.Annotation("a1", [{}])]
for annotation in annotations:
    fin = open("samples/" + annotation.name)
    for loc_set in annotation.sets:
        fout = open("madlibs/" + annotation.name, "wt")
        