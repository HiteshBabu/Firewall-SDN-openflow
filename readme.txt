Part2

a. Start VM mininet with the login ID mininet and password mininet.
b. In the terminal ifconfig -a to check all the interfaces lo,eth0,eth1 are up and if not "sudo 
dhclient interface_name" as this will let acess into mininet.
c. Start two terminals on host machine and ssh into mininet using the command mininet@192.168.56.101 with password as mininet.
d. Copy the files from your host machine to mininet's /pox/pox/misx/ folder by "scp of_tutorial2.py mytopo2.py mininet@192.168.56.101:~/pox/pox/misc/"
e.  Run the command "sudo mn --custom mytopo2.py --topo mytopo --mac --controller remote" on the terminal with mininet> in the /pox/pox/misc folder.
f. Change the directory to "mininet> cd mininet/pox" and execute the command "./pox.py log.level --DEBUG of_tutorial2"
g. In the terminal mininet> execute the command "h3 ping -c1 h4" and in the other terminal with controller we can observe flow of packet and the mininet terminal we can observe the ping statistics.
h. Execute pingall in mininet> terminal to ping hosts to each other and we can observe that few ports have already learned from the previous ping and few need routing table and check the ping statistics in mininet terminal.
i. In mininet> terminal execute the command "h3 ping -c1 10.0.34.67" and we can see that its unreachable with the unreachable message displayed at controller terminal and the packet being lost.
j. Execute the command iperf in terminal with mininet> to see the bandwidth.