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

def reload():
    run("firewall-cmd --reload")

def open_port(port):
    run("firewall-cmd --zone=public --add-port={0}/tcp --permanent".format(port))

def close_port(port):
    run("firewall-cmd --zone=public --remove-port={0}/tcp --permanent".format(port))


def selinux_t():
    run("setenforce 0")

def selinux_p():
    run('sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/sysconfig/selinux')
