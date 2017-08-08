# rsyncweb
web framwrok transfer file by rsync based flask(python)
======================================================
这是一个用python的flask框架写的用于手动同步文件的web
一般情况下我们使用 sersync+rsync 监控文件自动同步
但是有时因为两个服务器之间文件的差异性,不能自动同步,这时我们的工具就可以使用了
这个工具主要是给开发人员使用的，当他们用SVN/git将文件提交到测试服的时候,将文件或者目录路径填写在文本框中，点击提交即可。
文件的同步主要依靠同步脚本
rsync  -aSz /home/wwwroot/dmg/$1 rsync://zhong@Ip/dmg/$1  --password-file=/etc/rsyncd.secrets

1 安装python环境
----------------
2 安装依赖包（falsk,request ...）
----------------------------
3 python rsync.py 运行
---------------------
3 浏览器访问 ip:port访问
-------------------------
