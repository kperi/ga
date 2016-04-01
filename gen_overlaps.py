from collections import defaultdict
import itertools
import importlib

import config
importlib.reload(config)
from config import NUM_EXAMS, NUM_SLOTS, NUM_STUDENTS
print("config:", NUM_EXAMS, NUM_SLOTS, NUM_STUDENTS)

def load_data(data_file):
    students_exams = defaultdict()

    with open(data_file, "r") as f:
        lines = f.readlines()

        for line in lines:
            student, exams = line.strip().split("\t")
            students_exams[student] = exams.split(",")

    return students_exams


def generate_overlaps():

    STUDENTS_EXAMS_LOOKUP = load_data("students_exams.txt")


    EXAMS = [ 'exam_%s' % e for e in range(NUM_EXAMS)]
    CP_EXAMS =  itertools.product( EXAMS, EXAMS)
    L =  list( filter( lambda key: key[0] < key[1], CP_EXAMS) )


    LOOKUP = defaultdict( defaultdict )



    for item in L:
        ex1 = item[0]
        ex2 = item[1]
        if ex1>ex2: ex2,ex1 = ex1, ex2
        LOOKUP[ex1][ex2] = 0



    for idx, student in enumerate(STUDENTS_EXAMS_LOOKUP):
        S_EXAMS =  STUDENTS_EXAMS_LOOKUP[student]
        cross_prod =  list( filter( lambda key: key[0]>key[1], itertools.product( S_EXAMS, S_EXAMS )) )
        for ex1, ex2 in cross_prod:
            if ex1>ex2: ex2,ex1 = ex1, ex2
            LOOKUP[ex1][ex2] +=1



    s = 0
    with open("overlaps.txt", "w") as f:
        for ex1 in LOOKUP.keys():
            for ex2 in LOOKUP[ex1].keys():
                val = LOOKUP[ex1][ex2]
                f.write( "%s\t%s\t%s\n" %  (ex1, ex2,val))
                s+= val


    exam1 = 'exam_1'
    exam2 = 'exam_19'
    check = 0
    for idx, student in enumerate(STUDENTS_EXAMS_LOOKUP):
        exams = STUDENTS_EXAMS_LOOKUP[student]
        if exam1 in exams and exam2 in exams:
            check+=1


    print("check is", check)
    assert( check == LOOKUP[exam1][exam2] )
