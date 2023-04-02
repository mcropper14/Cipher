
import random 
from art import *
import time 



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
        self.clases = 0
        self.maj =""
        #self.schedule = 0 

    def get_status(self):
        print("Attributes: ")
        print("\n " + " Your name is: " + self.name)
        print("\n " + " Your major is " + self.maj.upper())
        print("\n " + " Your happiness level is: " + str(self.happiness))
        print("\n " + " Your twampness level is: " + str(self.twampness))
        print("\n " + " You have: " + str(self.d_dollars) + " dining dollars.")
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
        self.name = name.capitalize()
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
        elif plan.lower() == 'block 100':
            self.d_dollars = 500
        elif plan.lower() == 'commuter 50' or 'commuter 25':
            self.d_dollars = 560

        print("You now have " + str(self.d_dollars) + " dining dollars.")
        print("\n")


    def spend(self):
        choice = input("Where do you want to spend your dining dollars: Caf or Sadler ")
        print("Caf or Sadler?")
        if self.d_dollars > 0:
            if choice.lower() == "caf":
                self.d_dollars -= 10 
            elif choice.lower() == "sadler":
                self.d_dollars -= 15
        print('You now have ' + str(self.d_dollars) + ' dining dollars.')
    

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
            print("That's awkward, you got kicked out of Swem at midnight.")
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


    def get_clases(self):
        self.clases = input('Enter number of classes enrolled in: ')
        print('\n')
        print('You are enrolled in ' + self.clases + ' classes.')
        print('\n')


    def major(self):
        print('Majors Include: STEM or Not STEM ')
        print("\n")
        self.maj = input('Choose Your Fate Wisely: ' + self.maj)
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
        self.schedule = self.clases
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
            print('This is your exam grade for your class: ' + str(i) +"%.")
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



    def new_day(self):
        pass


    def disaster(self):
        #poss_diss_list = [insta_hack, forgot_hw, dorm_fire]
        poss_diss = ['Your instagram was hacked', 'The dorm fire alarm went off when there was actually a fire', 'You forgot there was a test']
        diss = random.choice(poss_diss)
        print(diss)
        if diss == poss_diss[0]:
            poss_stole = ['your inside jokes','your dog pictures','your unflattering pictures','pictures of the homework you send to your friend. It\'s okay, you probably failed anyways.','pictures about your embarassing hobby']
            print('the hacker stole ' + random.choice(poss_stole))
            self.happiness -= 20
            print('You are slowly losing your lust for life. Your happiness is now',self.happiness)
      
        elif diss == poss_diss[1]:
           poss_lost = ['your computer','your textbook','your hopes and dreams']
           print('Your dorm caught on fire. You lost ' + random.choice(poss_lost))
           self.happiness -= 10
           print('You are slowly losing your lust for life. Your happiness is now',self.happiness)
      
        elif diss == poss_diss[2]:
           print('This is what you get for skipping class to sleep in')
           self.stres += 10
           print('You are stressed and dropping out seems like a better idea everyday. You are slowly losing your youthful optimism. Your stress is now',self.stres)
    

    def game_over(self): 
        choices = ["stress", "disaster", "housing"]
        choice = random.choice(choices)
        print("\n")
        print(" \\  /")
        print("o----")
        print(" /  \\")


    def shower(self):
        print(" \n ")
        print("Congrats, you decided to take a shower!")
        print(" \n ")
        print(" \n ")
        print("\n ")
        print("\n ")
        rain_chars = ['.', ',', ':', ';', '`']
        for i in range(25):
            col = random.randint(1, 80)
            row = random.randint(10, 20)
            print('\033[{};{}H'.format(row, col), end='')
            print(random.choice(rain_chars), end='')
            time.sleep(0.1)
            print('\n')
        if self.maj.lower() == "stem":
            print(" \n ")
            print("You broke the stereotype by showering as a stem major!")
            self.hygiene += 5
            self.health += 2 
        else:
            self.hygiene += 10
            self.health += 2 


    def housing_crisis(self):
        print("You got kicked out of GGV for setting the fire alarm off!")
        print("Kathy Rowe says you have to live in a tent.")
        print("This is your new home.")
        print("Welcome to Tent City!")
        print("   /\\")
        print("  /  \\")
        print(" /    \\")
        print("/      \\")

        self.twampness += 10 
        self.health -= 1 
        self.hygiene -= 20 
        self.sleep -= 1 
        

    def main_game(self):
        setup = True 
        while setup:
            options = ["Set Name", "Get Status", "Meal Plan", "Set Major", "Set Classes", "Quit Setup" ]
            for option in options:
                print(" \n " + option)
            print(" \n ")
            pick = input("Pick an option: ")
            if pick.lower() == "get status":
                self.get_status()
            elif pick.lower() == "set name":
                self.set_name()
            elif pick.lower() == "meal plan":
                self.meal_plan()
            elif pick.lower() == "set major":
                self.major()
            elif pick.lower() == "set classes":
                self.get_clases()
            elif pick.lower() == "quit setup":
                setup = False 
            else:
                print("Not a valid option")


    def choices(self):
        setup = True 
        while setup:
            options = ["Spend", "Swem", "Club", "Shower", "End Day" ]
            for option in options:
                print(" \n "+ option)
            print(" \n ")
            pick = input("Pick a option: ")
            if pick.lower() == "spend":
                self.spend()
            elif pick.lower() == "swem":
                self.swem()
            elif pick.lower() == "club":
                self.club()
            elif pick.lower() == "end day":
                setup = False 
            elif pick.lower() == "shower":
                self.shower()
            else:
                print("Not a valid option")


    def random_game(self):
        choices = ["stress", "disaster", "housing"]
        choice = random.choice(choices)
        print("\n ")
        if choice == choices[0]:
            self.stress()
        elif choice == choices[1]:
            self.disaster()
        elif choice == choices[2]:
            self.housing_crisis()


if __name__ == '__main__':

    #examples of twamps 
    print("\n ")
    print("\n ")
    #tprint("TWAMP Simulator")
    print("\n ")
    print("\n ")


    #tprint("Welcome Home!")
    #tprint("You Belong Here!")


    test = Twamp()
    
    
    test.main_game()
    test.choices()
    test.random_game()
    #end game 
       
    


    
    
    
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
