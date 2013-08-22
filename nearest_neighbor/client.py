# This file is auto-generated from nearest_neighbor.idl
# *** DO NOT EDIT ***


import msgpackrpc
from types import *

class nearest_neighbor:
  def __init__ (self, host, port):
    address = msgpackrpc.Address(host, port)
    self.client = msgpackrpc.Client(address)

  def get_client (self):
    return self.client

  def init_table(self, name):
    retval = self.client.call('init_table', name)
    return retval

  def clear(self, name):
    retval = self.client.call('clear', name)
    return retval

  def set_row(self, name, id, d):
    retval = self.client.call('set_row', name, id, d)
    return retval

  def neighbor_row_from_id(self, name, id, size):
    retval = self.client.call('neighbor_row_from_id', name, id, size)
    return neighbor_result.from_msgpack(retval)

  def neighbor_row_from_data(self, name, query, size):
    retval = self.client.call('neighbor_row_from_data', name, query, size)
    return neighbor_result.from_msgpack(retval)

  def similar_row_from_id(self, name, id, ret_num):
    retval = self.client.call('similar_row_from_id', name, id, ret_num)
    return neighbor_result.from_msgpack(retval)

  def similar_row_from_data(self, name, query, ret_num):
    retval = self.client.call('similar_row_from_data', name, query, ret_num)
    return neighbor_result.from_msgpack(retval)

  def save(self, name, id):
    retval = self.client.call('save', name, id)
    return retval

  def load(self, name, id):
    retval = self.client.call('load', name, id)
    return retval

  def get_status(self, name):
    retval = self.client.call('get_status', name)
    return {k_retval : {k_v_retval : v_v_retval for k_v_retval,
        v_v_retval in v_retval.items()} for k_retval,v_retval in retval.items()}
