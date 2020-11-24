class Student:
    def __init__(self, student_number, name, major):
        self.student_number = student_number
        self.name = name
        self.major = major

class UnderGraduateSt(Student):
    def __init__(self, student_number, name, major, club):
        Student.__init__(self, student_number, name, major)
        self.club = club

    def __call__(self):
        return self.student_number, self.name, self.major, self.club

class GraduateSt(Student):
    def __init__(self, student_number, name, major, professor):
        Student.__init__(self, student_number, name, major)
        self.professor = professor

    def __call__(self):
        return self.student_number, self.name, self.major, self.professor

st1 = UnderGraduateSt("홍길동", 2018001, "영어학과", "공연동아리")
st2 = GraduateSt("이순신", 2019002, "영어학과", "신사임당")

print(st1())
print(st2())