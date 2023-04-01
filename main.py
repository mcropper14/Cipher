
import random 

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
        


    def set_name(self):
        name = input("Enter a name for your twamp: ")
        self.name = name
        output = "Welcome to William and Mary " + self.name
        print(output) #return output 

        

    def person_info(self):
        pass 
    
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
        pass 

    def exams(self):
        pass 

    def disaster(self, disaster):
        pass 



if __name__ == '__main__':

    myra = Twamp()
    myra.set_name()
    myra.stress()
    myra.swem()