
import random 
from art import *

class Twamp:

    def __init__(self):
        self.happiness = 100
        self.twampness = 0 
        self.d_dollars = 800 #maybe don't put here
        self.health = 100
        self.hygiene = 0 
        self.name = ""
        self.caffinate = 0 
        self.sleep = 0 
        self.stres = 50 
        self.hours = 1 
        self.maj =""
        #self.schedule = 0 
        
    def set_name(self):
        name = input("Enter a name for your twamp: ")
        self.name = name
        output = "Welcome to William and Mary " + self.name + "!"
        print(output)
        print("You Belong Here!")
        print("""
                 o  
                /|\\ 
                / \\
                   
                    """)


        
    def person_info(self):
        pass 
        
    def meal_plan(self):
        print('Meal Plans Available: All Access, Block 125, Block 100, Commuter 50, Commuter 25')
        print("\n")
        plan = input('Please enter your chosen meal plan: ')
        print("\n")
        print("You chose " + plan + " as your meal plan.")
        print("\n")
        if plan.lower() == 'all access' or 'block 125':
            self.d_dollars = 400

        if plan.lower() == 'block 100':
            self.d_dollars = 500
        if plan.lower() == 'commuter 50' or 'commuter 25':
            self.d_dollars = 560

        print("You spent " + str(self.d_dollars) + " dinning dollars.")
        print("\n")


    def spend(self):
        choice = input("Where do you want to spend your dinning dollars? ")
        print("Cafe or Saddler")
        if self.d_dollars > 0:
            if choice.lower() == "cafe":
                self.d_dollars -= 10 
            elif choice.lower() == "saddler":
                self.d_dollars -= 15
        else:
            self.disaster()
    
    
    def stress(self):
        print("Calculating Stress Level....")
        print("\n")
        choices = ["study", "procrastinate", "hang out" ]
        choice = random.choice(choices)
        hours = random.randint(1, 5)
        self.hours = hours 
        print("You decide to " + choice + " for " + str(self.hours) + " hours.")
        print("\n")
        
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
        print("\n")
        for hour in range(self.hours):
            self.happiness -= 1 
            self.stres += 1 
            self.sleep -= 1 
            self.caffinate += 1 

        

    def club(self):
        pass

    def greek_life(self):
        pass

    def major(self):
        self.maj = input('Majors Include: STEM or Not STEM: ')
        print("\n")
        print('Choose Your Fate Wisely: ' + self.maj)
        print("\n")
        if self.maj.lower() == 'stem':
            self.stres += 20
            print("That's a good choice!")
            print("\n")
            print("""
                *******
                *      *
                * o  o *
                *   v  *
                * \\_/ *
                ******
                """)
            print("\n")
        
        if self.maj.lower() == 'not stem':
            self.stres -= 20 
            print("\n")
            print("""
                *******
                *      *
                * o  o *
                *  ^   *
                * / \  *
                ******
                """)
            print("\n")

    def exams(self):
        c_num = input('Enter Number of Classes Enrolled In: ')
        print("\n")
        self.schedule = c_num
        grades = []
        if self.hours > 2:
            for i in range(int(self.schedule)):
                grade = random.randint(0,100)
                grade += (self.hours *5)
                grades.append(grade)
        else:
            for i in range(int(self.schedule)):
                grade = random.randint(0,100)
                grades.append(grade)
        
        
        for i in grades:
            print('This is your exam grades for your class: ' + str(i) +"%.")
            print("\n")
            if i < 50 and self.maj == "stem":
                print("That's an A with a curve!")
                print("\n")
                print("You must be in discrete structures!")
                print("\n")
                print("""
                 o  
                \|/
                / \\
                   
                    """)



    def disaster(self):
        if self.d_dollars == 0:
            print('You have starved')
        

if __name__ == '__main__':

    #exampls of twamps 
    tprint("Twamp Simulator")
    myra = Twamp()
    myra.set_name()
    myra.meal_plan()
    myra.major()
    myra.stress()
    myra.swem()
    myra.exams()