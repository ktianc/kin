#!/usr/bin/python
#coding=utf-8

from fabric.api import *
import sys
sys.path.append("/usr/local/kin/host/")
import client
import os


env.hosts = client.one
env.user  = client.user
env.password = client.password
env.port = client.port

def rpm_file(file_name):
    rpm_pag = open("/usr/local/kin/rpm_file/{0}".format(file_name),"r")
    pags = rpm_pag.read()
    rpm_list = pags.split("\n")
    rpm_list.remove("")
    for i in rpm_list:
    	run("rpm -e {0} --nodeps".format(i))
    run("rm -rf /usr/local/{0}".format(file_name))
    os.system("rm -rf /usr/local/kin/rpm_file/{0}".format(file_name))

#-----------------------web---------------------------
def nginx_m():
    run("cp -r /usr/local/nginx/html/ /tmp/")
    run("rm -rf /usr/local/nginx")

def nginx_y():
    run("yum -y remove nginx")

def httpd():
    run("yum -y remove httpd")

def tomcat():
    run("cp -r /usr/local/tomcat/webapps/ /tmp/")
    run("rm -rf /usr/local/tomcat")

def tengine():
    run("cp -r /usr/local/nginx/html/ /tmp/")
    run("rm -rf /usr/local/nginx")

def resin():
    run("rm -rf /usr/local/resin")

def BT():
    pass

#-------------------software--------------------------

#def other():
#	run("yum -y remove wget nmap net-tools unzip vim gcc openssl-devel  openssl   pcre pcre-devel zlib zlib-devel")

def epel():
    run("rpm -e remi-release")
    run("rpm -e epel-release --nodeps")

def php56():
    run("touch /usr/local/rpm_php")
    run("rpm -qa|grep php > /usr/local/rpm_php")
    get("/usr/local/rpm_php","/usr/local/kin/rpm_file/")
    rpm_file("rpm_php")

def php70():
    run("touch /usr/local/rpm_php")
    run("rpm -qa|grep php > /usr/local/rpm_php")
    get("/usr/local/rpm_php","/usr/local/kin/rpm_file/")
    rpm_file("rpm_php")
    run("rpm -e webtatic-release --nodeps")

def phpmyadmin():
    run("yum -y remove phpmyadmin")

def mysql():
    run("touch /usr/local/rpm_mysql")
    run("rpm -qa|grep mysql > /usr/local/rpm_mysql")
    get("/usr/local/rpm_mysql","/usr/local/kin/rpm_file/")
    rpm_file("rpm_mysql")

def redis():
    run("rm -rf /usr/local/redis")

def java_y():
    run("yum -y remove")

def java_m():
    run("rm -rf /usr/local/jdk1.8.0_162")
    run("sed -i '$d' /etc/profile")
    run("sed -i '$d' /etc/profile")
    run("sed -i '$d' /etc/profile")

def vsftpd():
    run("yum -y remove vsftpd")

def postfix():
    run("yum -y remove postfix")

def dovecot():
    run("yum -y remove dovecot")

def docker():
    run("yum -y remove docker-ce")
    run("rm -rf /var/lib/docker")

#-----------------------nagios---------------------

def plugins():
    run("rm -rf /usr/local/nagios")

def xinetd():
    run("yum -y remove xinetd")


def onekey():
    run("yum -y remove xinetd")
    run("rm -rf /usr/local/nagios")
    
