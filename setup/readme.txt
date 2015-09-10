
yum install firewalld
vi /etc/sysctl.conf

net.ipv4.ip_forward=1


service firewalld start
firewall-cmd --permanent --add-forward-port=port=22:proto=tcp:toport=22
firewall-cmd --permanent --add-forward-port=port=80:proto=tcp:toport=8888
service firewalld restart
