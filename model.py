dict_food = {'Beef(Herd)':60,'lamb':24,'cheese':21,'beef(dairy)':21,'chocolate':9,'coffee':17,'prawns(farmed)':12,'Palm oil':8,'Pork':7,'Poultry meat':6,'olive oil':6,'Fish(farmed)':5.0,'Eggs':4.5,'Fish(wild catch)':3,'milk':3,'Cane sugar':3,'groundnuts':2.5,'Wheat and rye':1.4,'tomatoes':1.4,'Maize(corn)':1,'cassava':1.0,'soymilk':0.9,'peas':0.9,'bananas':0.7,'root vegetables':0.4,'apples':0.3,'citrus fruits':0.3,"nuts":0.3}

def convert_food_to_CO2(food,kilos):
    if kilos =="":
        return 0
    kilos = float(kilos)
    co2= dict_food.get(food)
    return co2*kilos/1000

    
    
