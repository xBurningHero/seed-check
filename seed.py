#!/usr/bin/python
import socket
import random

def testSeed(source):
  random.seed(source)
  val = random.randint(0,6)
  print source,' has seed value of: ',val

hosts = ['rt1.dal.resolvity.com','rt2.dal.resolvity.com','rt1.las.resolvity.com','rt2.las.resolvity.com']

for host in hosts:
  testSeed(host)
