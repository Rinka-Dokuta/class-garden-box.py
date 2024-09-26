class garden_box:
    
    def __init__(self):
        self.plant = 0
    
    def planting(self):
        self.plant += 1
        print(self.plant)
        
    def watering(self):
        print("There is", self.plant, "in  your garden box")
        
    def harvesting(self):
        self.plant -= 1
        print(self.plant)
        


        
        
my_garden = garden_box()

my_garden.planting()
my_garden.planting()
my_garden.planting()
my_garden.watering()
my_garden.harvesting()

