# -- Flask Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

## Additional Imports
import datetime as dt
import model as model

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = dt.datetime.now()

# -- Routes --
@app.route('/')
@app.route('/index')
def index():
    data = {
        "ingredients":model.dict_food
    }
    
    return render_template('index.html', data=data)

@app.route('/convert',methods=["POST","GET"])
def convertC02emit():
    form = request.form
    kilos_list = request.form.getlist('kilos')
    print(kilos_list)
    carbonprint = 0
    i = 0
    for food in model.dict_food:
        carbonprint += model.convert_food_to_CO2(food,kilos_list[i])
        i+=1
    data = {
        "CO2":carbonprint, 
        "ingredients":model.dict_food
        }
    print(data)
    return render_template('index.html', data=data)



