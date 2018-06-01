#!/usr/bin/python
#coding=utf-8

from fabric.api import *


import sys
sys.path.append("/usr/local/kin/host/")
import client


env.hosts = client.one
env.user = client.user
env.password = client.password
env.port = client.port



def httpd():
    "http://mirrors.hust.edu.cn/apache/httpd/"
    run("yum -y install httpd")


def nginx_m():
    "https://nginx.org/en/download.html"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/nginx1.12.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf nginx1.12.tar.gz")
    with cd("/usr/local/nginx-1.12.2"):
        run("./configure")
        run("make")
        run("make install")
    run("rm -rf /usr/local/nginx1.12.tar.gz")
    run("rm -rf /usr/local/nginx-1.12.2")

def nginx_y():
    "http://nginx.org/packages/centos/7/noarch/RPMS/"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/nginx.rpm")
    with cd("/usr/local"):
        run("rpm -Uvh nginx.rpm")
        run("yum -y install nginx")
    run("rm -rf /usr/local/nginx.rpm")

def tomcat():
    "http://tomcat.apache.org/"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/tomcat9.0.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf tomcat9.0.tar.gz")
        run("mv apache-tomcat-9.0.2 tomcat")
    run("rm -rf /usr/local/tomcat9.0.tar.gz")

def tengine():
    "http://tengine.taobao.org/"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/tengine2.2.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf tengine2.2.tar.gz")
    with cd("/usr/local/tengine-2.2.1"):
        run("./configure --prefix=/usr/local/nginx")
        run("make")
        run("make install")
    run("rm -rf /usr/local/tengine2.2.tar.gz")
    run("rm -rf /usr/local/tengine-2.2.1")

def resin():
    "http://caucho.com/products/resin/download"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/resin4.0.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf resin4.0.tar.gz")
    with cd("/usr/local/resin-4.0.55"):
        run("./configure --prefix=/usr/local/resin --with-java-home=/usr/local/jdk1.8.0_162 --enable-64bit  ")
        run("make")
        run("make install")
    run("rm -rf /usr/local/resin4.0.tar.gz")
    run("rm -rf /usr/local/resin-4.0.55")

def jboss():
    pass

def BT():
    "https://www.bt.cn/about.html"
    with cd("/usr/local"):
        run("yum install -y wget && wget -O install.sh http://download.bt.cn/install/install.sh && sh install.sh")
