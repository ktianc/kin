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
env.key_filename = client.key_filename

command = raw_input("Please input command:")

def execute():
    run(command)
