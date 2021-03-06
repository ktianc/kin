#!/usr/bin/python
#coding=utf-8

from fabric.api import *

import sys
sys.path.append("/usr/local/kin/host")
import client

env.hosts = client.ip
env.user = client.user
env.password = client.password
env.port = client.port
env.key_filename = client.key_filename

def httpd():
    with cd("/etc/httpd/conf/"):
        run("mv httpd.conf httpd.conf_bak")
        run("wget -P /etc/httpd/conf/ https://www.ktianc.top/conf/httpd.conf")
        run("wget -P /etc/httpd/conf/ https://www.ktianc.top/conf/hosts-vhosts.conf")

def nginx_m():
    with cd("/usr/local/nginx/conf"):
        run("rm -rf nginx.conf")
        run("wget -P /usr/local/nginx/conf https://www.ktianc.top/conf/nginx.conf")
        run("wget -P /usr/local/nginx/conf https://www.ktianc.top/conf/default.conf")

def nginx_y():
    with cd("/etc/nginx/conf"):
        run("mv default.conf default.conf_bak")
        run("wget -P /etc/nginx/conf/ default.conf")

def tomcat():
    with cd("/usr/local/tomcat/conf"):
        run("mv server.xml server.xml_bak")
        run("wget -P /usr/local/tomcat/conf/ https://www.ktianc.top/conf/server.xml")

def tengine():
    with cd("/usr/local/nginx/conf"):
        run("rm -rf nginx.conf")
        run("wget -P /usr/local/nginx/conf/ https://www.ktianc.top/conf/nginx.conf")






