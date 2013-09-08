#!/usr/bin/env python

import sys, time, random
from nearest_neighbor import client
from nearest_neighbor import types

NAME = "sensor_nn"
nn = client.nearest_neighbor("127.0.0.1", 9199)

while 1 :
  e_time = time.time() + 5.0
  cnt = 0

  while e_time > time.time() :
    r = random.randint(0, 10000)
    nn.similar_row_from_id(NAME, str(r) , 5)
    cnt += 1

  print cnt
