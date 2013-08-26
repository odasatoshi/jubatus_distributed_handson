#!/usr/bin/env python
import random, time, json
import argparse
import pika, logging

def getData(sigma):
    x,y,z = random.randint(0,2), random.randint(0,2), random.randint(0,2)
    dat = {}
    dat["x"], dat["y"], dat["z"] = random.normalvariate(x,sigma), random.normalvariate(y,sigma), random.normalvariate(z,sigma)
    dat["gp"] = 9 * x + 3 * y + z
    return dat
 
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description='Generate and enqueue psudo sensor data')
    parser.add_argument('--speed', '-P', type=int, default = 1)
    parser.add_argument('--count', '-N', type=int, default = 100)
    parser.add_argument('--seed', '-S', default = 0)
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials = pika.PlainCredentials('jubatus','jubatus')))
    channel = connection.channel()
    channel.queue_declare(queue='sensor')

    random.seed(args.seed)
    for cnt in xrange(args.count):
        da = getData(0.1)
        channel.basic_publish(exchange='',
                      routing_key='sensor',
                      body= json.dumps((cnt, da)))
        print cnt, da["gp"]
        time.sleep( 1.0 / args.speed)
    connection.close()

