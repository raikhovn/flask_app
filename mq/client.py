'''
import pymqi

class QueueMgr:

    def __init__(self, qmgr_name: str, channel: str, ip: str):
        self.qmgr_name = qmgr_name
        self.channel = channel
        self.ip = ip
        self.qmgr = None
        

    def connect(self):
        #self.qmgr = pymqi.connect(self.qmgr_name, self.channel, self.ip, "mqm", "passw0rd")
        self.qmgr = pymqi.connect(self.qmgr_name, self.channel, self.ip)
        return

    def put_message(self, queue: str, msg: any):
        q = pymqi.Queue(self.qmgr, queue)
        q.put(msg)
        return

    def get_message(self, queue: str)-> any:
        q = pymqi.Queue(self.qmgr, queue)
        return q.get()    
    
    def disconnect(self):
        if self.qmgr is not None:
            self.qmgr.disconnect()
            self.qmgr = None
'''


