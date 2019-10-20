#!/bin/bash
yum install gcc screen dstat wget perl python cpan epel-release httpd php php-pear libpcap-devel libssh2 libssh php-devel libssh2-devel -y
yum install nload htop -y
pecl install -f ssh2
touch /etc/php.d/ssh2.ini
systemctl enable httpd
systemctl start httpd
service httpd restart
echo extension=ssh2.so > /etc/php.d/ssh2.ini
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=https
firewall-cmd --reload
service httpd restart
setenforce 0