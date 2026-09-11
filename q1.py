class father:
    def skill_father(self):
        print(f"Father's skill is gardening")

class mother:
    def skill_mother(self):
        print(f"Mother's skill is cooking")

class son(father, mother):
    def skill_son(self):
        self.skill_father()
        self.skill_mother()

son1 = son()
son1.skill_son()




            
