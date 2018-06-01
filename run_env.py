#/usr/bin/python
#coding=utf-8

import os

os.system("yum -y install epel-release")
os.system("yum -y install gcc python-devel libffi-devel openssl-devel python-pip")
os.system("pip install fabric")