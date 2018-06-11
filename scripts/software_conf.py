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

def vsftpd():
	with cd("/etc/vsftpd/"):
        run("mv vsftpd.conf vsftpd.conf.bak")
        run("rm -rf ftpusers")
        run("wget https://www.ktianc.com/conf/vsftpd.conf")
        run("wget https://www.ktianc.com/conf/ftpusers")
        run("firewall-cmd --zone=public --add-port=21/tcp --permanent")
        run("firewall-cmd --reload")
        run("setenforce 0")


def postfix():
    pass

def dovecot():
    pass
