import json


class Subscriptions:
    def __init__(self):
        pass
     
    # Call back functions
    def test_callback(msg):
        raw = msg.payload.decode('utf-8')
        data = json.loads(raw)
        print("Call back called. Topic: " + msg.topic + "Message: " + str(data["msg"]))

    
    subs = {'stm_test': test_callback}
    

    
    

