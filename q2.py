class teacher():
    def teach(self):
        print("I am a teacher")

class researcher():
    def research(self):
        print("I am a researcher")

class professor(teacher, researcher):
    def all_skills(self):
        self.teach()
        self.research()
p = professor()
p.all_skills()