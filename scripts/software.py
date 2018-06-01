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


def other():
    run("yum -y install  wget nmap git net-tools unzip vim gcc openssl-devel glibc openssl glibc-common gcc-c++ pcre pcre-devel zlib zlib-devel")

def epel():
    with cd("/usr/local/"):
        run("rpm -ivh https://www.ktianc.com/pag/epel.rpm")
        run("rpm -ivh https://www.ktianc.com/pag/remi.rpm")
        run("yum repolist")

def php56():
    run("yum -y install --enablerepo=remi --enablerepo=remi-php56 php php-opcache php-devel php-bcmath  php-tidy php-mbstring php-mcrypt php-mysqlnd php-fpm php-phpunit-PHPUnit php-pecl-xdebug php-pecl-xhprof php-gd")

def php70():
    run("rpm -Uvh https://www.ktianc.com/pag/webtatic.rpm")
    run("yum -y install php70w php70w-fpm php70w-mysqlnd php70w-gd php70w-opcache php70w-pecl-xdebug php70w-pecl-xhprof")


def phpmyadmin():
    run("yum -y install phpmyadmin")
    with cd("/etc/httpd/conf.d/"):
        run("mv phpMyAdmin.conf phpMyAdmin.conf_bak")
        run("wget -P /etc/httpd/conf.d/ https://www.ktianc.com/conf/phpMyAdmin.conf")
    run("sed -i s/'cookie'/'http'/g /etc/phpMyAdmin/config.inc.php")
    run("systemctl restart httpd")
    
    

def mysql():
    with cd("/usr/local"):
        run("wget https://www.ktianc.com/pag/mysql57.rpm")
        run("yum -y localinstall mysql57.rpm")
        run("yum -y install mysql-community-server")
        run("rm -rf mysql57.rpm")
        run("systemctl start mysqld")

def redis():
    "https://redis.io/download"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/redis4.0.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf redis4.0.tar.gz")
    with cd("/usr/local/redis-4.0.6"):
        run("make")
        run("make install")
    run("rm -rf /usr/local/redis4.0.tar.gz")
    run("rm -rf /usr/local/redis-4.0.6")

def mariadb():
    "https://downloads.mariadb.org/"
    run("wget -P /etc/yum.repos.d/ https://www.ktianc.com/cond/MariaDB.repo")
    run("yum install MriaDB-server MariaDB-client")

def java_y():
    "http://www.oracle.com/technetwork/java/javase/downloads/index.html"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/jdk162.rpm")
    with cd("/usr/local"):
        run("yum -y install jdk162.rpm")
    run("rm -rf /usr/local/jdk162.rpm")

def java_m():
    "http://www.oracle.com/technetwork/java/javase/downloads/index.html"
    run("wget -P /usr/local/ https://www.ktianc.com/pag/jdk162.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf jdk162.tar.gz")


    run("echo '\nexport JAVA_HOME=/usr/local/jdk1.8.0_162' >> /etc/profile")
    run("echo 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar' >> /etc/profile")
    run("echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile")
    run("source /etc/profile")
    run("rm -rf /usr/local/jdk162.tar.gz")

def vsftpd():
    run("yum -y install vsftpd")

def postfix():
    run("yum -y install postfix")

def dovecot():
    run("yum -y install dovecot")

def zabbix_agent():
    pass

def docker():
    run("yum install -y yum-utils device-mapper-persistent-data lvm2")
    run("yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo")
    run("yum-config-manager --enable docker-ce-edge")
    run("yum -y install docker-ce")

