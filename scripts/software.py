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


def other():
    run("yum -y install  wget nmap git net-tools lrzsz vim")

def epel():
    run("rpm -ivh http://www.ktianc.top/pag/centos7/epel.rpm")
    run("yum repolist")

def php56():
    run("rpm -ivh http://www.ktianc.top/pag/centos7/remi.rpm")
    run("yum repolist")
    run("yum -y install --enablerepo=remi --enablerepo=remi-php56 php php-opcache php-devel php-bcmath  php-tidy php-mbstring php-mcrypt php-mysqlnd php-fpm php-phpunit-PHPUnit php-pecl-xdebug php-pecl-xhprof php-gd")

def php70():
    run("rpm -Uvh https://www.ktianc.top/pag/webtatic.rpm")
    run("yum -y install php70w php70w-fpm php70w-mysqlnd php70w-gd php70w-opcache php70w-pecl-xdebug php70w-pecl-xhprof")
#    run("yum -y install --enablerepo=remi --enablerepo=remi-php70 php php-fpm php-mysqlnd php-gd php-opcache php-pecl-xdebug php-pecl-xhprof")

'''
def phpmyadmin():
    run("yum -y install phpmyadmin")
    with cd("/etc/httpd/conf.d/"):
        run("mv phpMyAdmin.conf phpMyAdmin.conf_bak")
        run("wget -P /etc/httpd/conf.d/ https://www.ktianc.top/conf/phpMyAdmin.conf")
    run("sed -i s/'cookie'/'http'/g /etc/phpMyAdmin/config.inc.php")
    run("systemctl restart httpd")
'''

def mysql():
    with cd("/usr/local"):
        run("wget http://www.ktianc.top/pag/centos7/mysql/mysql57.rpm")
        run("yum -y localinstall mysql57.rpm")
        run("yum -y install mysql-community-server")
        run("rm -rf mysql57.rpm")
        run("systemctl start mysqld")

def redis():
    "https://redis.io/download"
    run("wget -P /usr/local/ http://www.ktianc.top/pag/centos7/redis4.0.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf redis4.0.tar.gz")
    with cd("/usr/local/redis-4.0.6"):
        run("make")
        run("make install")
    run("rm -rf /usr/local/redis4.0.tar.gz")
    run("rm -rf /usr/local/redis-4.0.6")

'''
def mariadb():
    "https://downloads.mariadb.org/"
    run("wget -P /etc/yum.repos.d/ https://www.ktianc.top/cond/MariaDB.repo")
    run("yum install MriaDB-server MariaDB-client")
'''

def java_y():
    "https://www.oracle.com/technetwork/java/javase/downloads/index.html"
    run("wget -P /usr/local/ http://www.ktianc.top/pag/centos7/jdk162.rpm")
    with cd("/usr/local"):
        run("yum -y install jdk162.rpm")
    run("rm -rf /usr/local/jdk162.rpm")

def java_m():
    "https://www.oracle.com/technetwork/java/javase/downloads/index.html"
    run("wget -P /usr/local/ http://www.ktianc.top/pag/centos7/jdk-8u221-linux-x64.tar.gz")
    with cd("/usr/local"):
        run("tar -zxvf jdk-8u221-linux-x64.tar.gz")
    run("echo '\nexport JAVA_HOME=/usr/local/jdk1.8.0_221' >> /etc/profile")
    run("echo 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar' >> /etc/profile")
    run("echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile")
    run("source /etc/profile")
    run("rm -rf /usr/local/jdk-8u221-linux-x64.tar.gz")

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

def zabbix_server():
    a = 0
    # 请提前安装好mysql数据库，并创建数据库zabbix，用户zabbix
    # 检测有没有安装mysql数据库
    mysql_passwd = raw_input("Please input zabbix user database password：")
    try:
        run("mysqld --version")
        a = 1
    finally:
        if not a:
            print "未检测到MySQL数据库"
    try:
        run("php --version")
    except:
        run("yum -y install php php-bcmath php-gd php-ldap php-mbstring php-xml php-mysql")
    # 密码是否正确，查看有没有zabbix数据库
    run("yum install -y yum-utils java-headless dejavu-sans-fonts fping OpenIPMI-libs libevent net-snmp-libs unixODBC")
    run("yum install -y http://www.ktianc.top/pag/centos7/iksemel-1.4-20.122.el7.x86_64.rpm")
    run("yum -y install httpd")
    run("rpm -Uvh http://www.ktianc.top/pag/centos7/zabbix/zabbix-server-mysql-4.4.1-1.el7.x86_64.rpm")
    run("rpm -Uvh http://www.ktianc.top/pag/centos7/zabbix/zabbix-web-4.4.1-1.el7.noarch.rpm http://www.ktianc.top/pag/centos7/zabbix/zabbix-web-mysql-4.4.1-1.el7.noarch.rpm")
    run("rpm -Uvh http://www.ktianc.top/pag/centos7/zabbix/zabbix-agent-4.4.1-1.el7.x86_64.rpm")
    run("rpm -Uvh http://www.ktianc.top/pag/centos7/zabbix/zabbix-get-4.4.1-1.el7.x86_64.rpm")
    # 导入数据库
    run("zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p{0} zabbix".format(mysql_passwd))
    # 修改连接数据库密码
    run("sed -i 's/# DBPassword=/DBPassword={0}/g' /etc/zabbix/zabbix_server.conf".format(mysql_passwd))
    # 修改时区
    run("sed -i 's!# php_value date.timezone Europe/Riga!php_value date.timezone Asia/Shanghai!g' /etc/httpd/conf.d/zabbix.conf")
    # 获取字体
    with cd("/usr/share/zabbix/assets/fonts"):
        run("wget http://www.ktianc.top/pag/conf/simkai.ttf")
    # 删除默认软连接的字符集
    run("sed -i '0,/graphfont/s/graphfont/simkai/' /usr/share/zabbix/include/defines.inc.php")
    run("systemctl restart httpd zabbix-server zabbix-agent")
    print "访问地址：http://localhost/zabbix\n用户名：Admin\n密码：zabbix"

