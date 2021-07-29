dict_food = {'Beef (Herd)':60,'Lamb':24,'Cheese':21,'Beef (Dairy)':21,'Chocolate':9,'Coffee':17,'Prawns (Farmed)':12,'Palm Oil':8,'Pork':7,'Poultry Meat':6,'Olive Oil':6,'Fish (Farmed)':5.0,'Eggs':4.5,'Fish (Wild Catch)':3,'Milk':3,'Cane Sugar':3,'Groundnuts':2.5,'Wheat and Rye':1.4,'Tomatoes':1.4,'Maize (Corn)':1,'Cassava':1.0,'Soymilk':0.9,'Peas':0.9,'Bananas':0.7,'Root Vegetables':0.4,'Apples':0.3,'Citrus Fruits':0.3,'Nuts':0.3}
ingredients = sorted(dict_food.keys())

def convert_food_to_CO2(food,kilos):
    if kilos =="":
        return 0
    kilos = float(kilos)
    co2= dict_food.get(food)
    return co2*kilos/1000

    
    
