KIN
 ======

    批量交互式运维工具

    server：python2.7，fabric，windows or linux

    client: centos7系列，ssh服务

    请在server端先执行run_env.py文件

    使用之前需要在host/client.py文件中添加上你的客户端ip、用户名、密码
    * //客户端与客户端的用户名须一致，最好为 root
    * //客户端与客户端的密码须一致，更利于部署，管理
 
    $python install.py   //执行安装，根据提示进行下一步
    $python configure.py  //进行配置，根据提示进行下一步

    list    //可以使用list进行查看

    install：
    安装  
    configure：
    配置
  
    * file :文件的传输
    * shell : 批量执行shell命令
    * onekeyin ： 一键安装环境
    * onekeyrm ： 一键卸载环境
    * remove ： 删除单个软件
    * nagios_c : nagios客户端
    * firewall : 开启端口、关闭端口、关闭selinux
    * restart ： 重启服务、暂停服务
_________
[__K__](https://www.ktianc.com "ktianc")  
  __Programming enrich life__
