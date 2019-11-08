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
env.key_filename = client.key_filename


def httpd():
    "https://mirrors.hust.edu.cn/apache/httpd/"
    run("yum -y install httpd")


def nginx_m():
    "https://nginx.org/en/download.html"
    run("yum -y install gcc make pcre-devel openssl-deve")
    run("wget -P /usr/local/ http://www.ktianc.top/pag/centos7/nginx1.12.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf nginx1.12.tar.gz")
    with cd("/usr/local/nginx-1.12.2"):
        run("./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module")
        run("make")
        run("make install")
    run("rm -rf /usr/local/nginx1.12.tar.gz")
    run("rm -rf /usr/local/nginx-1.12.2")

'''
def nginx_y():
    "https://nginx.org/packages/centos/7/noarch/RPMS/"
    run("wget -P /usr/local/ https://www.ktianc.top/pag/nginx.rpm")
    with cd("/usr/local"):
        run("rpm -Uvh nginx.rpm")
        run("yum -y install nginx")
    run("rm -rf /usr/local/nginx.rpm")
'''

def tomcat():
    "https://tomcat.apache.org/"
    run("wget -P /usr/local/ http://www.ktianc.top/pag/centos7/tomcat8.5.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf tomcat8.5.tar.gz")
        run("mv apache-tomcat-8.5.24 tomcat")
    run("rm -rf /usr/local/tomcat8.5.tar.gz")

'''
def tengine():
    "https://tengine.taobao.org/"
    run("wget -P /usr/local/ https://www.ktianc.top/pag/tengine2.2.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf tengine2.2.tar.gz")
    with cd("/usr/local/tengine-2.2.1"):
        run("./configure --prefix=/usr/local/nginx")
        run("make")
        run("make install")
    run("rm -rf /usr/local/tengine2.2.tar.gz")
    run("rm -rf /usr/local/tengine-2.2.1")


def resin():
    "https://caucho.com/products/resin/download"
    run("wget -P /usr/local/ https://www.ktianc.top/pag/resin4.0.tar.gz")
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
'''

def BT():
    "https://www.bt.cn/about.html"
    with cd("/usr/local"):
        run("yum install -y wget && wget -O install.sh https://download.bt.cn/install/install.sh && sh install.sh")
