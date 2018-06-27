#!/usr/bin/python
#coding=utf-8

def host(ips,users,passwds,key=None):
    global ip,user,password,port,key_filename
    if "," in ips:
    	ip = ips.split(",")
    else:
    	ip = ips
    user = users
    password = passwds
    port = 22
    key_filename = key

host("ips","root","passwd","key")
