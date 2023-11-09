from flask import Blueprint, Response, jsonify
from db.connection import Db
from model.user import bind_car, bind_phone, bind_user, build_response
import json
from pymarshaler.marshal import Marshal
from model.user import User

bp_user = Blueprint("user", __name__) 

# This is how you register a controller, it accepts OPTIONS and GET methods by default
@bp_user.route('/health', methods=["GET"])
def health():
    return Response(response="System is Up", status=200)


@bp_user.route('/users/<string:user_id>', methods=["GET"])
def get_user(user_id):
    # execute query
    db = Db("host='localhost' dbname='userdb' user='postgres' password='Jamesbond1'")
    db.connect()
    rs_user = db.query("SELECT * FROM users WHERE user_id = '%s'"%(user_id))
    rs_car = db.query("SELECT * FROM  user_cars WHERE user_id = '%s'"%(user_id))
    rs_phone = db.query("SELECT * FROM  user_phones WHERE user_id = '%s'"%(user_id))

    phone =  bind_phone(rs_phone) 
    car =  bind_car(rs_car) 
    user =  bind_user(rs_user, phone, car)  
   
    s = str(build_response(user), 'UTF-8')
  
    
    return jsonify(user=s, status=200, mimetype='application/json')