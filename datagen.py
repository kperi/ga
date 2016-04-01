#/usr/bin/env python3
import random
from gen_overlaps import generate_overlaps
random.seed(42)

from config import NUM_EXAMS, NUM_SLOTS, NUM_STUDENTS
print("config:", NUM_EXAMS, NUM_SLOTS, NUM_STUDENTS)


def generate():
    exams = [ "exam_%s" % s for s in range(NUM_EXAMS)]

    students = ["student_%s" %s for s in range(NUM_STUDENTS)]


    student_exams = {}
    for student in students:
        num_exams =  random.randint( 3, 6)
        sample = list( set( random.sample( exams ,  num_exams) ) )
        student_exams[student] = sample

    with open("students_exams.txt", "w") as f:
        for key in student_exams.keys():
            exams = ",".join( student_exams[key] )
            #print( key, exams)
            f.write( "%s\t%s\n" % (key,exams))



def load_data(data_file):
    students_exams = defaultdict()

    with open(data_file, "r") as f:
        lines = f.readlines()

        for line in lines:
            student, exams = line.strip().split("\t")
            students_exams[student] = exams.split(",")

    return students_exams


def calculate_overlaps():
    STUDENTS_EXAMS_LOOKUP = load_data("students_exams.txt")

if __name__ == '__main__':
    print("generating data")
    generate()
    print("generating overlaps")
    generate_overlaps()
