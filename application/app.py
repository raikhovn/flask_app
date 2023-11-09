from flask import Flask
from endpoints.user import bp_user
#from endpoints.mqm import bp_mqm


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_user)
    #app.register_blueprint(bp_mqm)
    return app

#SET CHLAUTH('DEV.APP.SVRCONN') TYPE(BLOCKUSER) USERLIST(ALLOWANY)
#ALTER CHL('DEV.APP.SVRCONN') CHLTYPE(SVRCONN) MCAUSER('mqm')


    