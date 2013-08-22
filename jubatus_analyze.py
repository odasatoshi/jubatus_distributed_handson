#!/usr/bin/env python

import sys
from nearest_neighbor import client
from nearest_neighbor import types

NAME = "sensor_nn"
nn = client.nearest_neighbor("127.0.0.1", 9199)
id_ = sys.argv[1]

print nn.similar_row_from_id(NAME, str(id_) , 5)
    

