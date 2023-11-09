'''
from flask import Blueprint, Response, request, jsonify
from mq.client import QueueMgr

bp_mqm = Blueprint("mqm", __name__) 



@bp_mqm.route('/mqm/get/<string:queue>', methods=["GET"])
def get_message(queue):
    # execute query
    qmgr = QueueMgr("QM1", "DEV.APP.SVRCONN", "127.0.0.1(1414)")
    qmgr.connect()
    msg = qmgr.get_message(queue)
    qmgr.disconnect()
    s = str(msg, 'UTF-8')
    return jsonify(message=s, status=200, mimetype='application/json')

@bp_mqm.route('/mqm/put/<string:queue>', methods=["POST"])
def put_message(queue):
    # execute query
    qmgr = QueueMgr("QM1", "DEV.APP.SVRCONN", "127.0.0.1(1414)")
    qmgr.connect()
    qmgr.put_message(queue, request.get_data())
    qmgr.disconnect()

    return Response(response="Processed", status=200)
'''   