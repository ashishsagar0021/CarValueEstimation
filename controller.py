from flask import Blueprint, render_template, request, redirect, url_for
from views import carValueView

hello = Blueprint('hello', __name__)
get_car_value_bp = Blueprint('get_car_value', __name__)


@hello.route('/', methods=['GET', 'POST'])
def hello_route():
    if request.method == 'POST':
        make = request.form.get('make')
        model = request.form.get('model')
        year = request.form.get('year')
        mileage = request.form.get('mileage', 0.0)
        return redirect(url_for('get_car_value.get_car_value', make=make, model=model, year=year, mileage=mileage))
    return render_template('index.html')

@get_car_value_bp.route('/getCarValue')
def get_car_value():
    make = request.args.get('make')
    model = request.args.get('model')
    year = request.args.get('year')
    mileage = request.args.get('mileage', 0.0)
    carValue = carValueView(make, model, year, mileage)
    return render_template('get_car_value.html', make=make, model=model, year=year, mileage=mileage, carValue=carValue)