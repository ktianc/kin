#!/usr/bin/python
#coding=utf-8

from fabric.api import *
import sys
sys.path.append("/usr/local/kin/host/")
import client

env.hosts  = client.ip
env.user = client.user
env.password = client.password
env.port = client.port

file_name = raw_input("Please input file name:")
file_dir = raw_input("Please input file dir:")

def execute_put():
    put(file_name,file_dir)

def execute_get():
    get(file_name,file_dir)
