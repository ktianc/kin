#!/usr/bin/python
#coding=utf-8

from fabric.api import *
import sys
sys.path.append("/usr/local/kin/host/")
import client

env.hosts  = client.one
env.user = client.user
env.password = client.password
env.port = client.port

command = raw_input("Please input command:")

def execute():
    run(command)