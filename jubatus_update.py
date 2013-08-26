#!/usr/bin/env python

import pika
import json
import msgpackrpc
from nearest_neighbor import client
from nearest_neighbor import types

NAME = "sensor_nn"

#See http://jubat.us/ja/faq_rpc_err_workaround.html
def update_jubatus(id_, datum_):
    nn = client.nearest_neighbor("127.0.0.1", 9199)
    retry_max = 1
    retry_interval = 1
    try:
        retry_count = retry_max
        while True:
            try:
                nn.set_row(NAME, str(id_) , datum_)
                break
            except (msgpackrpc.error.TransportError, msgpackrpc.error.TimeoutError) as e:
                retry_count -= 1
                if retry_count <= 0:
                    raise

                nn.get_client().close()
                nn = client.nearest_neighbor("127.0.0.1", 9199)

                time.sleep(retry_interval)
                continue

    except msgpackrpc.error.RPCError as e:
        raise

    finally:
        nn.get_client().close()

connection = pika.BlockingConnection(pika.ConnectionParameters(
   host='localhost', credentials = pika.PlainCredentials('jubatus','jubatus')))
channel = connection.channel()
channel.queue_declare(queue='sensor')

def callback(ch, method, properties, body):
    id_, val_ = json.loads(body)
    datum = types.datum([], [
           ["x", val_["x"]],
           ["y", val_["y"]],
           ["z", val_["z"]]
         ])
    update_jubatus(id_, datum)
    print datum

channel.basic_consume(callback, queue='sensor', no_ack=True)
channel.start_consuming()

