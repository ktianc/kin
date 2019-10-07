#!/usr/bin/python
#coding=utf-8

def host(ips,users,passwds=None,key=None):
    global ip,user,password,port,key_filename
    ip = ips
    user = users
    password = passwds
    port = 22
    key_filename = key

host("","root","")
