class CourseInfo(object):

    def __init__(self, course_name):
        self.course_name = course_name
        self.psetsDone = []
        self.grade = "No Grade"

    def set_pset(self, pset, score):
        self.psetsDone.append((pset, score))

    def get_pset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def set_grade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def get_grade(self):
        return self.grade


class Edx(object):

    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(CourseInfo(course))

    def set_grade(self, grade, course="6.01x"):
        '''
        grade: integer >= 0 & <= 100
        course: string

        This method sets the grade in the CourseInfo
        object named by `course`.
        If `course` was not part of the initialization,
        then no grade is set, and no
        error is thrown.
        The method does not return a value.
        '''
        #   fill in code to set the grade
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                self.myCourses[i].set_grade(grade)

    def get_grade(self, course="6.02x"):
        '''
        course: string

        This method gets the grade in the the CourseInfo
        object named by `course`.

        returns: the integer grade for `course`.
        If `course` was not part of the initialization,
        returns -1.
        '''
        #   fill in code to get the grade
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                return self.myCourses[i].get_grade()
        return -1

    def set_pset(self, pset, score, course="6.00x"):
        '''
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the CourseInfo object.

        If `course` is not part of the initialization,
        then no pset score is set,
        and no error is thrown.
        '''
        #   fill in code to set the pset
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                self.myCourses[i].set_pset(str(pset), score)

    def get_pset(self, pset, course="6.00x"):
        '''
        pset: a string or a number
        course: string

        returns: The score of the specified `pset`
        of the given `course` using the CourseInfo object.
        If `course` was not part of the initialization,
        returns -1.
        '''
        #   fill in code to get the pset
        for i in range(len(self.myCourses)):
            if self.myCourses[i].courseName == course:
                return self.myCourses[i].get_pset(str(pset))
        return -1


edX = Edx(["6.00x", "6.01x", "6.02x"])
edX.set_pset(1, 100)
edX.set_pset(2, 100, "6.00x")
edX.set_pset(2, 90, "6.00x")

edX.set_grade(100)

for c in ["6.00x", "6.01x", "6.02x"]:
    edX.set_grade(90, c)

for c in edX.myCourses:
    print c.courseName, c.get_grade()


# dir(edX) will print out all the methods for edX's class
dir(edX)[2](90)
