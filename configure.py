#!/usr/bin/python
#coding=utf-8

import os
import sys
import readline
import re

service_list = ["httpd","tomcat","nginx","vsftpd","postfix","dovecot","resin","mysqld","redis","firewalld","xinetd","nagios","php-fpm"]

service_d = {1:"software_conf : postfix dovecot vsftpd",
             2:"web_conf : httpd nginx_m nginx_y tomcat tengine",
             3:"restart : Reboot service",
             4:"file : Transfer files",
             5: "shell : Use system commands"}

add_service_list = ["nginx","tomcat"]

def colour(*num):  # list color
    print ("\nPlease select : \n")
    for i in list(num):
        print ("\t"+i)

def sys_com(pyfile,com,mode="-L"):

    if mode == "-P":
        os.system("fab -f scripts/{0}.py -P {1}".format(pyfile,com))
    else:
        os.system("fab -f scripts/{0}.py {1}".format(pyfile,com))


while True:
    service = raw_input("Please input service (q = Quit) >>> ")

    if service == "q":
        break

    elif service == "list":
        colour("software","web_conf","restart","file","shell")


#-------------------------------------------------software----------------------------------------------------------

    elif  service == "software":
        while True:
            software = raw_input("Please input need configure software name (q = Quit) >>> ")

            software_l = ["postfix","dovecot","vsftpd","mysql"]


            if software == "q":
                break

            elif software == "list":
                colour("portfix","dovecot","vsftpd","mysql")

            elif software in software_l:
                sys_com("software_conf",software,mode="-P")

            else:

                print("Error : Not have this service.")
#-------------------------------------------------web-------------------------------------------------------------

    elif service == "web_conf":
        while True:
            web = raw_input("Please input need configure web name (q = Quit) >>> ")

            web_l = ["httpd","nginx_m","nginx_y","tengine","tomcat"]
            if web == "q":
                break

            elif web == "list":
                colour("httpd","nginx_m","nginx_y","tengine","tomcat")

            elif web in web_l:
                sys_com("web_conf",web,mode="-P")

            else:

                print("Error : Not have this service.")

#-------------------------------------------------restart--------------------------------------------------------

    elif service == "restart":
        while True:
            reboot_s = raw_input("Please input need reboot service (q = Quit) >>> ")

            if reboot_s == "q":
                break

            elif reboot_s == "list":
                colour("httpd","tomcat","nginx","vsftpd","postfix","dovecot","resin","mysqld","redis","firewalld","xinetd","nagios","php-fpm")

            elif reboot_s in service_list:
                sys_com("restart","reboot_l:"+reboot_s,mode="-P")

            else:

                print "Not have this service."

#--------------------------------------------------command------------------------------------------------------

    elif service == "shell":
        while True:
            command = raw_input("Enter 'start' into execution (q = Quit) >>> ")

            if command == "start":
                os.system("fab -f scripts/command.py -P execute")

            elif command == "q":
                break

            else:

                print "Error:{0}:command not found".format(command)

#----------------------------------------------------file------------------------------------------------------

    elif service == "file":

        file_type  = raw_input("Please choose put or get >>> ")

        if file_type == "put":
            os.system("fab -f scripts/file.py -P file_put")

        elif file_type =="get":
            os.system("fab -f scripts/file.py -P get")

        else:

            print  "Error:{0}:command not found".format(command)

    else:

        print("Error:No this service,Please input list see.")

#-------------------------------------------------add service------------------------------------------------------
'''
    elif server == "add_service":

        file_type = raw_input("Please input add service:")

        if file_type in add_service_list:
            os.system("fab -f scripts/add.py")

        else:
'''   


