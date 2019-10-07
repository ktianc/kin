#!/usr/bin/python
#coding=utf-8

from fabric.api import *
import sys
sys.path.append("/usr/local/kin/host/")
import client
import os

env.hosts = client.ip
env.user = client.user
env.password = client.password
env.port = client.port
env.key_filename = client.key_filename

def vsftpd():
    with cd("/etc/vsftpd/"):
        run("mv vsftpd.conf vsftpd.conf.bak")
        run("rm -rf ftpusers")
        run("wget https://www.ktianc.top/conf/vsftpd.conf")
        run("wget https://www.ktianc.top/conf/ftpusers")
        run("firewall-cmd --zone=public --add-port=21/tcp --permanent")
        run("firewall-cmd --reload")
        run("setenforce 0")


def postfix():
    pass

def dovecot():
    pass

def mysql():
    new_passwd = raw_input("Please input new password : ")
    old_passwd = os.popen("cat /var/log/mysqld.log |grep generated|sed 's/^.*host: //g'").read().replace("\n","")
    run("mysqladmin -u root -p {0} password {1}").format(old_passwd,new_passwd)
    
