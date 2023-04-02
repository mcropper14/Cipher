
import random 
from art import *
import time 



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

    def get_status(self):
        print("Attributes: ")
        print("\n " + " Your name is: " + self.name)
        print("\n " + " Your major is " + self.maj)
        print("\n " + " Your happiness level is: " + str(self.happiness))
        print("\n " + " Your twampness level is: " + str(self.twampness))
        print("\n " + " You have: " + str(self.d_dollars) + " dinning dollars.")
        print("\n " + " Your health is: " + str(self.health))
        print("\n " + " Your hygiene is: " + str(self.hygiene))
        print("\n " + " Your level of caffeine consumption: " + str(self.caffinate))
        print("\n " + " Your hours of sleep: " + str(self.sleep))
        print("\n " + " Your stress level is: " + str(self.stres))

       

    def get_calc(self):
        total = 100
        for i in range(total):
            progress = (i + 1) / total * 100
            print('[' + '#' * int(progress // 10) + '-' * (10 - int(progress // 10)) + '] ' + str(int(progress)) + '%', end='\r')
            time.sleep(0.1)
        print('\nDone!')
        
        
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
        choice = input("Where do you want to spend your dinning dollars: Cafe or Saddler ")
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
        self.get_calc()
        choices = ["study", "procrastinate", "hang out" ]
        choice = random.choice(choices)
        hours = random.randint(1, 5)
        self.hours = hours 
        print("You decide to " + choice + " for " + str(self.hours) + " hours.")
        print("\n")
        
        if choice == "study":
            print("You decided to ")
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
        if self.hours > 3:
            print("That's ackward, you got kicked out of swem at midnight.")
            print("Have fun in the 24 hour study room!")
        for hour in range(self.hours):
            self.happiness -= 1 
            self.stres += 1 
            self.sleep -= 1 
            self.caffinate += 1 

        

    def club(self):
        num = int(input("How many clubs do you want to join? "))
        print("\n")
        print("You joined " + str(num) +" clubs.")
        print("\n")
        for i in range(num):
            self.stres += i
            self.happiness += 1

        print("Your new stress level is " + str(self.stres))
        print("\n")
        print("Your new happiness level is " +str(self.happiness))
        print("\n")

        

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
        #poss_diss_list = [insta_hack, forgot_hw, dorm_fire]
        poss_diss = ['your instgram was hacked', 'The dorm fire alarm went off when there was actually a fire', 'You forgot there was a test']
        diss = random.choice(poss_diss)
        print(diss)
        if diss == poss_diss[0]:
            poss_stole = ['your inside jokes','your dog pictures','your unflattering pictures','pictures of the homework you send to your friend. It\'s okay, you probably failed anyways.','pictures about your embarassing hobby']
            print('the hacker stole ' + random.choice(poss_stole))
            self.happiness -= 20
            print('You are slowly losing you lust for life. Your happiness is now',self.happiness)
      
        elif diss == poss_diss[1]:
           poss_lost = ['your computer','your textbook','your hopes and dreams']
           print('Your dorm caught on fire. You lost ' + random.choice(poss_lost))
           self.happiness -= 10
           print('You are slowly losing you lust for life. Your happiness is now',self.happiness)
      
        elif diss == poss_diss[2]:
           print('This is what you get for skipping class to sleep in')
           self.stres += 10
           print('You are stressed and dropping out seems like a better idea everyday. You are slowly losing your youthful optimism. Your stress is now',self.stres)
    


    def death(self): 
        if self.d_dollars <= 0:
            print('You have starved')
            print("\n")
            print(" \\  /")
            print("o----")
            print(" /  \\")
        else:
            print("You have died.")
            print("\n " + "Game Over!")

    def housing_crisis(self):
        print("You got kicked out of GGV for setting the fire alarm off!")
        

    #classes 
    #timer, notifiys you to go to class 
    #miss class, happiness goes up, grade range goes down 



    #get status 
    #set name 
    #meal plan
    #spend 
    #stress 
    #swem 
    #club 
    #major 
    #exams 
    #disaster 

    #options: get status, set name, meal plan, major
    #random: spend, stress, swem, club, exams, disaster


    def main_game(self):
        setup = True 
        while setup:
            options = ["Set Name", "Get Status", "Meal Plan", "Set Major", "Quit Setup" ]
            for option in options:
                print(" \n "+ option)
            print(" \n ")
            pick = input("Pick a option: ")
            if pick.lower() == "get status":
                self.get_status()
            elif pick.lower() == "set name":
                self.set_name()
            elif pick.lower() == "meal plan":
                self.meal_plan()
            elif pick.lower() == "set major":
                self.major()
            elif pick.lower() == "quit setup":
                setup = False 
            else:
                print("Not a valid option")

    def random_game(self):
        ran_choices = random.randint(2,10)
        for i in range(ran_choices):
            choices = ["spend", "stress", "swem", "club", "exams", "disaster", "death"]
            choice = random.choice(choices)
            print("\n ")
            if choice == choices[0]:
                self.spend()
            elif choice == choices[1]:
                self.stress()
            elif choice == choices[2]:
                self.swem()
            elif choice == choices[3]:
                self.club()
            elif choice == choices[4]:
                self.exams()
            elif choice == choices[5]:
                self.disaster()
            

                
      




if __name__ == '__main__':

    #exampls of twamps 
    print("\n ")
    print("\n ")
    tprint("TWAMP Simulator")
    print("\n ")
    print("\n ")



    #tprint("Welcome Home!")
    #tprint("You Belong Here!")


    test = Twamp()
    
    
    test.main_game()
    test.random_game()
    test.death()
       
    


    
    
    
    #[print(" \n " + option) for option in options 
    # if option.lower() == "get status"]
    #print(input(" \n " + "Pick an option: "))

    
    

  



    """
    myra.set_name()
    myra.meal_plan()
    myra.major()
    myra.stress()
    myra.swem()
    myra.exams()
    myra.spend()
    """