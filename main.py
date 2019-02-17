import re
import sys
import os
from source_to_annotation import generate_annotations
from annotation_to_madlib import annotations_to_madlibs

def cleanse(s):
    for x in re.findall(r'("[^\n]*"(?!\\))|(//[^\n]*$|/(?!\\)\*[\s\S]*?\*(?!\\)/)',s,8):s=s.replace(x[1],'')
    return s


for filename in os.listdir('samples/'):
    text = cleanse(open('samples/' + filename, 'r').read())
    to_write = open('samples/' + filename, 'w')
    to_write.write(text)

generate_annotations()
annotations_to_madlibs()

for filename in os.listdir('madlibs/'):
    texts = open('madlibs/' + filename, 'r').readlines()
    result = []
    for text in texts:
        if not (not text or text.isspace()):
            result.append(text)
    result_string = ''.join(result)
    to_write = open('madlibs/' + filename, 'w')
    to_write.write(result_string)
