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

def plugins():
    run("wget -P /usr/local/ https://www.ktianc.com/pag/plugins2.2.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf plugins2.2.tar.gz")
    with cd("/usr/local/nagios-plugins-2.2.1/"):
        run("./configure")
        run("make")
        run("make install")
        run("chown nagios:nagios /usr/local/nagios")
        run("chown -R nagios:nagios /usr/local/nagios/libexec")
    run("rm -rf /usr/local/plugins2.2.tar.gz ")
    run("rm -rf /usr/local/nagios-plugins-2.2.1")


def xinetd():
    run("yum -y install xinetd")
    run("firewall-cmd --zone=public --add-port=5666/tcp  --permanent")
    run("firewall-cmd --reload")

def nrpe():
    run("wget -P /usr/local/ https://www.ktianc.com/pag/nrpe3.1.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf nrpe3.1.tar.gz")
    with cd("/usr/local/nrpe-3.1.0"):
        run("./configure")
        run("make all")
        run("make install-plugin")
        run("make install-daemon")
        run("make install-config")
        run("make install-inetd")
    run("rm -rf /usr/local/nrpe3.1.tar.gz")
    run("rm -rf nrpe-3.1.0 ")

def configure():
    run("mv /usr/local/nagios/etc/nrpe.cfg  /usr/local/nagios/etc/nrpe.cfg_bak")
    run("wget -P /usr/local/nagios/etc/  https://www.ktianc.com/conf/nrpe.cfg")
    run('echo "nrpe            5666/tcp                # NRPE">> /etc/services')
    run("sed  -i 's/yes/no/g' /etc/xinetd.d/nrpe")
    run("sed  -i 's/127.0.0.1/218.206.209.131/g' /etc/xinetd.d/nrpe")
    run("systemctl restart xinetd")

def onekey():
    plugins()
    xinetd()
    nrpe()
    configure()

        
