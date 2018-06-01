#!/usr/bin/python
#coding=utf-8
import os
import readline
import re
import sys
sys.path.append("/usr/local/kin/host/")
import client


software_d = {1:"other   : wget nmap net-tools unzip vim gcc openssl-devel glibc openssl glibc-common gcc-c++ pcre pcre-devel zlib zlib-devel",
                 2:"epel   : epel-release-latest-7.noarch.rpm and remi-release-7.rpm",
                 3:"php56   : php php-opcache php-devel php-bcmath  php-tidy php-mbstring php-mcrypt php-mysqlnd php-phpunit-PHPUnit php-pecl-xdebug php-pecl-xhprof php-gd",
                 4:"php70   : php php-common php-cli php70w-fpm php70w-mysqlnd php70w-gd php70w-opcache php70w-pecl-xdebug php70w-pecl-xhprof",
                 5:"phpmyadmin   : phpMyAdmin.noarch 4.4.15.10-2.el7",
                 6:"mysql   : mysql57-community-release-el7-8.noarch.rpm",
                 7:"redis   : redis-4.0.6.tar.gz",
                 8:"java_y   : jdk-8u162-linux-x64.rpm",
                 9:"java_m   : jdk-8u162-linux-x64.tar.gz",
                 10:"vsftpd   : vsftpd 3.0.2-22.el7",
                 11:"postfix   : postfix 2:2.10.1-6.el7",
                 12:"dovecot   : dovecot 1:2.2.10-8.el7",
                 13:"zabbix-agent    : No matching packages to list",
                 14:"docker    : No matching packages to list"}


web_d = {1:"httpd   : httpd 2.4.6-67.el7.centos.6",
        2:"nginx_m   : nginx-1.12.2.tar.gz",
        3:"nginx_y   : nginx-release-centos-7-0.el7.ngx.noarch.rpm",
        4:"tomcat   : apache-tomcat-8.5.24.tar.gz",
        5:"tengine   : tengine-2.2.1.tar.gz",
        6:"resin   : resin-4.0.55.tar.gz",
        7:"jboss   : No matching packages to list",
        8:"BT   :BT-5.5"}

web_list = ["httpd","nginx_m","nginx_y","tomcat","tengine","resin","jboss","BT"]

service_list = ["httpd","tomcat","nginx","vsftpd","postfix","dovecot","resin","mysqld","redis","firewalld"]

rm_list = ["epel","php56","php70","phpmyadmin","mysql","redis","java_y","java_m","vsftpd","postfix","dovecot","docker","zabbix-agent","httpd","nginx_m","nginx_y","tomcat","tengine","resin","jboss","BT","plugins","xinetd","onekey"]

rm_software = " epel php56 php70 phpmyadmin mysql redis java_y java_m vsftpd postfix dovecot docker zabbix-agent"

rm_web = "httpd nginx_m nginx_y  tomcat tengine resin jboss BT"

rm_nagios_c = "plugins xinetd nrpe configure onekey"

ip_dict = {}

software_list = ["other","epel","php56","php70","phpmyadmin","mysql","redis","java_y","java_m","vsftpd","postfix","dovecot","docker","zabbix-agent"]

service_d ={1:"software : other epel php56 php70 phpmyadmin mysql redis java_y java_m vsftpd postfix dovecot",
            2:"web : httpd nginx_m nginx_y tomcat tengine resin jboss BT",
            3:"nagios_c : plugins xinetd nrpe configure",
            4:"firewall : Open and close firewall,selinux",
            5:"restart : Reboot service",
            6:"shell : Use system commands",
            7:"file : Transfer files",
            8:"onekeyin : One key installation environment",
            9:"onekeyrm : One key remove environment",
            10:"remove : Delete the software package",
            11:"host : logon host"}

env_l = {1:"LAMP : apache:2.4  mysql:5.7  php:7.0",
         2:"LAMp : apache:2.4  mysql:5.7  php:5.6",
         3:"LNMP : nginx:1.12  mysql:5.7  php:7.0",
         4:"LNMp : nginx:1.12  mysql:5.7  php:5.6",
         }

quit_list = ["q","Q","quit","Quit","exit"]

def sys_com(pyfile,comm,mode="-l"):  # implement

        if mode == "-P":
            os.system("fab -f scripts/{0}.py {1} -P".format(pyfile,comm))
        
        else:
            os.system("fab -f scripts/{0}.py {1}".format(pyfile,comm))



def colour(*num):  # list color
    print ("\nPlease select: \n")
    for i in list(num):
        print ("\t"+i)


class onekeyinenv: # One key install environmental package

    def LNMP(self):
        sys_com("web","nginx_m")
        sys_com("software","mysql")
        sys_com("software","php70")

    def LNMp(self):
        sys_com("web","nginx_m")
        sys_com("software","mysql")
        sys_com("software","php56")

    def LAMP(self):
        sys_com("web","httpd")
        sys_com("software","mysql")
        sys_com("software","php70")

    def LAMp(self):
        sys_com("web","httpd")
        sys_com("software","mysql")
        sys_com("software","php56")

class onekeyrmenv: # One key remove environmental package

    def LNMP(self):
        sys_com("remove","nginx_m")
        sys_com("remove","mysql")
        sys_com("remove","php70")

    def LNMp(self):
        sys_com("remove","nginx_m")
        sys_com("remove","mysql")
        sys_com("remove","php56")

    def LAMP(self):
        sys_com("remove","httpd")
        sys_com("remove","mysql")
        sys_com("remove","php70")

    def LAMp(self):
        sys_com("remove","httpd")
        sys_com("remove","mysql")
        sys_com("remove","php56")




print "---------------------------Install-------------------------"
print "---------------Use list view the directory----------------\n"


while True:
    service = raw_input("Please input service (q = Quit) >>> ")

    if service in quit_list:
        break

    elif service == "list":
        colour(service_d[1],service_d[2],service_d[3],service_d[4],service_d[5],service_d[6],service_d[7],service_d[8],service_d[9],service_d[10],service_d[11])


#-------------------------------------------------software----------------------------------------------------------------------

    elif  service == "software":
        while True:
            software = raw_input("Please input prepare install software name, -P = Multithreading (q = Quit) >>> ")


            if software in quit_list:
                break

            elif software == "list":
                colour(software_d[1],software_d[2],software_d[3],software_d[4],software_d[5],software_d[6],software_d[7],software_d[8],software_d[9],software_d[10],software_d[11],software_d[12],software_d[13])

            elif software in software_list:
                sys_com("software",software)

            elif "-P" in software:
                for i in software_list:
                    if i in software:
                        sys_com("software",software,mode="-P")

            else:
                print "InputError:No this package,Please input list see."



#-------------------------------------------------web----------------------------------------------------------------------

    elif service == "web":
        while True:
            web_server = raw_input("Please input web server, -P = Multithreading (q = Quit) >>> ")


            if web_server in quit_list:
                break

            elif web_server == "list":
                colour(web_d[1],web_d[2],web_d[3],web_d[4],web_d[5],web_d[6],web_d[7],web_d[8])

            elif web_server in web_list:
                sys_com("web",web_server)

            elif "-P" in web_server:
                for i in web_list:
                    if i in web_server:
                        sys_com("web",web_server,mode="-P")

            else:
                print "InputError:No this package,Please input list see."


# ------------------------------------------------nagios_c-----------------------------------------------------------------------

    elif service == "nagios_c":
        while True:
            n_server = raw_input("Please input prepare install software name, -P = Multithreading (q = Quit) >>> ")


            if n_server in quit_list:
                break

            elif n_server == "list":
                colour("plugins","xinetd","nrpe","configure","onekey")

            elif n_server in ["plugins","xinetd","nrpe","configure","onekey"]:
                sys_com("nagios_c",n_server)

            elif "-P" in n_server:
                for i in ["plugins","xinetd","nrpe","configure","onekey"]:
                    if i in n_server:
                        sys_com("nagios_c",n_server,"-P")

            else:
                print "InputError:No this package,Please input list see"

#--------------------------------------------firewall----------------------------------------------------------------


    elif service == "firewall":

        while True:

            firewall_type = raw_input("Please input firewall type, -P = Multithreading (q = Quit) >>> ")

            if firewall_type == "list":
               colour("open_port","close_port","selinux")

            elif firewall_type in quit_list:
                break

            elif "open_port" and "-P" in firewall_type:

                while True:

                    firewall_port = raw_input("Enter the port to open(q = Quit) >>> ")

                    if firewall_port.isdigit():

                        sys_com("firewall","open_port:"+firewall_port,mode="-P")

                    elif firewall_port in quit_list:
                        break

                    elif firewall_port == "reload":
                        sys_com("firewall","reload",mode="-P")

                    else:

                        print "Enter the port to open."
                        print "Input reload reboot."

            elif "open_port"in firewall_type and "-P" not in firewall_type:

                while True:

                    firewall_port = raw_input("Enter the port to open(q = Quit) >>> ")

                    if firewall_port.isdigit():

                        sys_com("firewall","open_port:"+firewall_port)

                    elif firewall_port in quit_list:
                        break

                    elif firewall_port == "reload":
                        sys_com("firewall","reload")

                    else:

                        print "Enter the port to open."
                        print "Input reload reboot."
                        

            elif "close_port" and "-P" in firewall_type:

                while True:

                    firewall_port = raw_input("Enter the port to open(q = Quit) >>> ")

                    if firewall_port.isdigit():

                        sys_com("firewall", "close_port:" + firewall_port,mode="-P")

                    elif firewall_port == "reload":
                        sys_com("firewall","reload",mode="-P")

                    elif firewall_port in quit_list:
                        break

                    else:

                        print "Enter the port to open."
                        print "Input reload reboot."


            elif "close_port" in firewall_type and "-P" not in firewall_type:

                while True:

                    firewall_port = raw_input("Enter the port to open(q = Quit) >>> ")

                    if firewall_port.isdigit():

                        sys_com("firewall", "close_port:" + firewall_port)

                    elif firewall_port == "reload":
                        sys_com("firewall","reload")

                    elif firewall_port in quit_list:
                        break

                    else:

                        print "Enter the port to open."
                        print "Input reload reboot."



#-----------------------------------------------------selinux-----------------------------------------------------------


            elif firewall_type == "selinux":

                print "input 0 temporary close"
                print "input 1 permanent close"
                selinux_type = raw_input("Please input (q = Quit) >>> ")

                if selinux_type == "0":
                    sys_com("firewall","selinux_t",mode="-P")

                elif selinux_type == "1":
                    sys_com("firewall","selinux_p",mode="-P")

            else:

                print "InputError:No this service,Please select firewall or selinux."

#----------------------------------------------------restart------------------------------------------------------------

    elif service == "restart":
        while True:
            reboot_s = raw_input("Please input need reboot service (q = Quit) >>> ")

            if reboot_s in quit_list:
                break

            elif reboot_s == "list":
                colour("httpd","tomcat","nginx","vsftpd","postfix","dovecot","resin","mysqld","redis","firewalld")

            elif reboot_s in service_list:
                sys_com("restart","reboot_l:"+reboot_s,mode="-P")

            else:

                print "ValueError : Not have this service."

#--------------------------------------------------command------------------------------------------------------

    elif service == "shell":
        while True:
            command = raw_input("Enter 'start' into execution (q = Quit) >>> ")

            if command == "start":
                os.system("fab -f scripts/command.py -P execute")

            elif command in quit_list:
                break

            else:

                print "InputError:{0}:command not found".format(command)

#----------------------------------------------------file------------------------------------------------------

    elif service == "file":

        file_type = raw_input("Please choose put or get >>> ")


        if file_type == "put":
            os.system("fab -f scripts/file.py execute_put")

        elif file_type == "get":
            os.system("fab -f scripts/file.py execute_get")

        else:

            print "InputError:{0}:command not found".format(file_type)


#-------------------------------------------------onekeyin-------------------------------------------------


    elif service == "onekeyin":

        while True:
        
            inenv = raw_input("Please enter the name of the environment package >>> ")

            if inenv in quit_list:
                break

            elif inenv == "list":
                colour(env_l[1],env_l[2],env_l[3],env_l[4])

            elif inenv == "LAMP":
                deploy = onekeyinenv()
                deploy.LAMP()
                break

            elif inenv == "LAMp":
                deploy = onekeyinenv()
                deploy.LAMp()
                break

            elif inenv == "LNMP":
                deploy = onekeyinenv()
                deploy.LNMP()
                break

            elif inenv == "LNMp":
                deploy = onekeyinenv()
                deploy.LNMp()
                break

            else:
                print "InputError:No this service,Please input list see."


#-------------------------------------------------onekeyre-------------------------------------------------

    elif service == "onekeyrm":

        while True:

            rmenv = raw_input("Please enter the name of the environment package >>> ")

        
            if rmenv in quit_list:
                break

            elif rmenv == "list":
                colour(env_l[1],env_l[2],env_l[3],env_l[4])

            elif rmenv == "LAMP":
                deploy = onekeyrmenv()
                deploy.LAMP()
                break

            elif rmenv == "LAMp":
                deploy = onekeyrmenv()
                deploy.LAMp()
                break
  
            elif rmenv == "LNMP":
                deploy = onekeyrmenv()
                deploy.LNMP()
                break

            elif rmenv == "LNMp":
                deploy = onekeyrmenv()
                deploy.LNMp()
                break

            else:
                print "InputError:No this service,Please input list see."

#-------------------------------------------------remove-------------------------------------------------


    elif service == "remove":

        while True:

            repag = raw_input("Please enter the name of the package (q = Quit) >>> ")

            if repag in quit_list:
                break

            elif repag == "list":

                print "\nnagios client : {0}".format(rm_nagios_c)
                print "web : {0}".format(rm_web)
                print "software : {0}\n".format(rm_software)

            elif repag in rm_list:
                sys_com("remove",repag,mode="-P")

            elif repag == "php70":
                sys_com("remove",repag)

            elif repag == "php56":
                sys_com("remove",repag)

            else:
                print "InputError:No this package, Please input list see."

#-------------------------------------------------Host------------------------------------

    elif service == "host":

        while True:

            IP = raw_input("Please input host ip (q = Quit) >>> ")

            if IP in quit_list:
                break

            elif IP == "list":
                print "Client Host :\n"
                y = 0
                for x in client.one:
                    y += 1
                    z = str(y)
                    ip_dict[z] = x
                    print "{0}   : {1}".format(z,x)
                print "\n"

            elif IP in ip_dict.keys():
                os.system("ssh root@{0}".format(ip_dict[IP]))

            elif re.findall(r"^[0-9]{2,3}\.\d{2,3}\.\d{1,3}\.\d{1,3}$",IP):
                os.system("ssh root@{0}".format(IP))

            else:
                print "InputError : IP format is not correct."

#------------------------------------------end------------------------------------------------

    else:
        print "InputError:No this service,Please input list see."


