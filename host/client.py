#!/usr/bin/python
#coding=utf-8

def host(ips,users,passwds):
    global ip,user,password,port
    if "," in ips:
    	ip = ips.split(",")
    else:
    	ip = ips
    user = users
    password = passwds
    port = 22

host("ips","root","passwd")
