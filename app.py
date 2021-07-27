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
    }
    return render_template('index.html', data=model.dict_food)

@app.route('/convert',methods=["POST","GET"])
def convertC02emit():
    form = request.form
    kilos_list = request.form.getlist('kilos')
    print(kilos_list)
    carbonprint = model.convert_food_to_CO2(form["food"],form["kilos"])
    data = {"CO2":carbonprint}
    print(data)
    return render_template('results.html', data=data)


