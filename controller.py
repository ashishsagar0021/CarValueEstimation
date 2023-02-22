from flask import Blueprint, render_template, request, redirect, url_for

hello = Blueprint('hello', __name__)
get_car_value_bp = Blueprint('get_car_value', __name__)

@hello.route('/', methods=['GET', 'POST'])
def hello_route():
    if request.method == 'POST':
        field1 = request.form.get('field1')
        field2 = request.form.get('field2')
        field3 = request.form.get('field3')
        field4 = request.form.get('field4', '')
        return redirect(url_for('get_car_value.get_car_value', field1=field1, field2=field2, field3=field3, field4=field4))
    return render_template('index.html')

@get_car_value_bp.route('/getCarValue')
def get_car_value():
    field1 = request.args.get('field1')
    field2 = request.args.get('field2')
    field3 = request.args.get('field3')
    field4 = request.args.get('field4', '')
    return render_template('get_car_value.html', field1=field1, field2=field2, field3=field3, field4=field4)


# Data columns (total 25 columns):
#  #   Column                     Dtype
# ---  ------                     -----
#  0   vin                        object
#  1   year                       int64
#  2   make                       object
#  3   model                      object
#  4   trim                       object
#  5   dealer_name                object
#  6   dealer_street              object
#  7   dealer_city                object
#  8   dealer_state               object
#  9   dealer_zip                 object
#  10  listing_price              float64
#  11  listing_mileage            float64
#  12  used                       bool
#  13  certified                  bool
#  14  style                      object
#  15  driven_wheels              object
#  16  engine                     object
#  17  fuel_type                  object
#  18  exterior_color             object
#  19  interior_color             object
#  20  seller_website             object
#  21  first_seen_date            object
#  22  last_seen_date             object
#  23  dealer_vdp_last_seen_date  object
#  24  listing_status             object
# dtypes: bool(2), float64(2), int64(1), object(20)