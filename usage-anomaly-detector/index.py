import json
import threading
import random
import time
import numpy as np

from iofog_python_sdk.client import IoFogClient
from iofog_python_sdk.iomessage import IoMessage
from iofog_python_sdk.listener import *
import flask
from flask_cors import CORS,cross_origin


current_config = None
client = IoFogClient()
lock = threading.Lock()

final_result = ''

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def update_config():
    attempt_limit = 5
    config = None
    config = client.get_config()


    if attempt_limit == 0:
        print('Config update failed :(')
        return

    lock.acquire()
    global current_config
    current_config = config
    lock.release()



@app.route('/api/raw',methods=['GET'])
@cross_origin(methods=['GET'],origins='*')
def api():
    response = app.response_class(
        response=final_result,
        status=200,
        mimetype='application/json'
    )
    return response


def dummy():
    lock.acquire()
    config = current_config
    lock.release()

    if not config:
        print('Config is empty...')
        return False

class ControlListener(IoFogControlWsListener):
    def on_control_signal(self):
        update_config()

class MessageListener(IoFogMessageWsListener):

    def on_receipt(self, message_id, timestamp):
        print('Receipt: {} {}'.format(message_id, timestamp))

    def on_message(self, io_msg):
        usage_values = json.loads(str(io_msg.contentdata.decode('utf-8')))["train_data"]
        validation_values = json.loads(str(io_msg.contentdata.decode('utf-8')))["validation_data"]
        np_usage_values = np.array(usage_values)
        nplen = float(len(np_usage_values))
        mean = sum(np_usage_values) / nplen
        stdev = np.std(np_usage_values)
        print('data: mean: {} standard_dev: {}'.format(mean, stdev))

        min_expected_val = float(mean) - 2*float(stdev)
        max_expected_val = float(mean) + 2*float(stdev)
        for i in range(0,30):
            if validation_values[i] < min_expected_val or validation_values[i] > max_expected_val:
                print('anomaly usage at {} for device {} with value {}'.format(i,io_msg.tag ,validation_values[i]));
                local_msg=IoMessage()
                local_msg.tag = io_msg.tag
                global final_result
                final_result = '{"usage_data":['+",".join(map(str,validation_values))+'],"anomaly_value":'+str(validation_values[i])+',"anomaly_step":'+str(i)+'}'
                


update_config()
client.establish_message_ws_connection(MessageListener())
client.establish_control_ws_connection(ControlListener())  
CORS(app)      
app.run(host= '0.0.0.0')
#while True:
#    dummy();    
