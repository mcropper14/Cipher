

import random 

class Twamp:

    def __init__(self):
        self.happiness = 100
        self.twampness = 0 
        self.d_dollars = 0
        self.health = 100

        self.hygiene = 0 
        self.name = ""
        self.caffinate = 0 
        self.sleep = 0 
        self.stres = 50 
        self.hours = 1 
        


        self.stress = 0 
        self.hygiene = 0
        self.schedule = 0

    def set_name(self):
        name = input("Enter a name for your twamp: ")
        self.name = name
        output = "Welcome to William and Mary " + self.name
        print(output) #return output 

        

    def person_info(self):
        pass 
    
    def meal_plan(self):
        print('Meal Plans Available: All Access, Block 125, Block 100, Commuter 50, Commuter 25')
        plan = input()
        print('Please enter your chosen meal plan: ' + plan)

        if plan.lower() == 'all access' or 'block 125':
            self.d_dollars = 400
        if plan.lower() == 'block 100':
            self.d_dollars = 500
        if plan.lower() == 'commuter 50' or 'commuter 25':
            self.d_dollars = 560

    def display(self):
        pass

    
        
        
    def stress(self):
        print("Calculating Stress Level....")
        choices = ["study", "procrastinate", "hang out" ]
        choice = random.choice(choices)
        hours = random.randint(1, 5)
        self.hours = hours 
        print("You decide to " + choice + " for " + str(self.hours) + " hours.")
        
        if choice == "study":
            self.happiness -= self.hours * 10 
            self.twampness += 10 
            self.health -= self.hours 
            self.caffinate += self.hours * 100 
            self.sleep -= self.hours 
            self.hygiene -= 10 
            self.stres += self.hours * 10
        elif choice == "procrastinate":
            self.happiness -= 10
            self.twampness -= 10 
            self.health -= self.hours 
            self.sleep += self.hours 
            self.stres += self.hours * 5 
        else:
            self.happiness += self.hours * 10 
            self.hygiene += 10 
            self.sleep += 7 
            self.stres -= self.hours * 5
        
        return self.stres
    
    def swem(self):
        print("Going to Swem to study for " + str(self.hours) + " hours.")
        for hour in range(self.hours):
            self.happiness -= 1 
            self.stres += 1 
            self.sleep -= 1 
            self.caffinate += 1 

        

    def club(self):
        pass

    def greek_life(self):
        pass

    def orientation(self, days, socialize):
        pass

    def major(self):
        print('Majors Include: STEM or Not STEM')
        maj = input()
        print('Choose Your Fate Wisely: ' + maj)
        if maj.lower() == 'stem':
            self.stress += 20
        if maj.lower() == 'not stem':
            self.stress -= 20 

    def classes(self):
        c_num = input()
        print('Enter Number of Classes Enrolled In: ' + c_num)
        self.schedule = c_num
    
    def exams(self):
        grades = []
        for i in range(self.schedule):
            grades.append(randint(0, 100))
        print('These are your exam grades for your ' + self.schedule + 'classes: ' + grades)

    def disaster(self, disaster):
        if self.d_dollars == 0:
            print('You have starved')
        pass



if __name__ == '__main__':

    myra = Twamp()
    myra.set_name()
    myra.stress()
    myra.swem()