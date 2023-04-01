class Twamp:

    def __init__(self):
        self.happiness = 100
        self.twampness = 0 
        self.d_dollars = 800 #maybe don't put here
        self.health = 100
        self.stress = 0 
        self.hygiene = 0 


    def name(self):
        pass 

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

    def swem(self):
        pass

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
        if self.d_dollars == 0:
            print('You have starved')
        pass

