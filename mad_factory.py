import sys
import os
import random
import pickle
from annotation_to_madlib import get_candidates
from data_types import Annotation

class MadFactory:
    def __init__(self):
        # pick a template
        template_name = random.choice(os.listdir('madlibs/'))
        self.madlib = open('madlibs/' + template_name, 'r').readlines()
        annotations = pickle.load(open(os.path.join(os.path.dirname(__file__), "annotations.pickle"), 'rb'))
        for annotation in annotations:
            if annotation.file_name == template_name:
                self.annotation = annotation
                print("successfully broken: " + str(self.annotation.reverse))
                break

    def get_next_block(self, count=50):
        current_line = 0
        while current_line < len(self.madlib):
            yield get_candidates(self.annotation, current_line, count)
            current_line += 1
