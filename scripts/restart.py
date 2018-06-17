#!/usr/bin/python
#coding=utf-8

from fabric.api import *
import sys
sys.path.append("/usr/local/kin/host/")
import client


env.hosts = client.ip
env.user = client.user
env.password = client.password
env.port = client.port

def reboot_l(service):

    run("systemctl restart {0}".format(service))

def stop_l(service):

    run("systemctl stop {0}".format(service))

def start_l(service):
	
    run("systemctl start {0}".format(service))
