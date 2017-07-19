Part1
  	
1. As Switch:
a. Start VM mininet with the login ID mininet and password mininet.
b. In the terminal ifconfig -a to check all the interfaces lo,eth0,eth1 are up and if not "sudo 
dhclient interface_name" as this will let acess into mininet.
c. Start two terminals on host machine and ssh into mininet using the command mininet@192.168.56.101 with password as mininet.
d. Copy the files from your host machine to mininet's /pox/pox/misx/ folder by "scp topology.py of_tutorial_switch.py mininet@192.168.56.101:~/pox/pox/misc/"
e.  Run the command "sudo mn --custom topology.py --topo mytopo --mac --controller remote" on the terminal with mininet> in the folder /pox/pox/misc.
f. Change the directory to "mininet> cd mininet/pox" and execute the command "./pox.py log.level --DEBUG of_tutorial_switch"
g. In the terminal mininet> execute the the command "xterm h1 h2 h3" which creates 3 terminals for h1, h2, h3
h. In the h2 terminal execute the command "tcpdump -XX -n -i h2-eth0" to see the packets at h2 and similarly at h3 terminal execute the command "tcpdump -XX -n -i h3-eth0" to see the packets at h3.
i. In the h1 terminal execute the command "ping -c1 10.0.0.2" to ping h2 as it is with the ip address 10.0.0.2 
j. Close h1,h2,h3 and execute the command iperf in terminal with mininet> to see the bandwidth

		
2. As Router: Part A
a. Start VM mininet with the login ID mininet and password mininet.
b. In the terminal ifconfig -a to check all the interfaces lo,eth0,eth1 are up and if not "sudo 
dhclient interface_name" as this will let acess into mininet.
c. Start two terminals on host machine and ssh into mininet using the command mininet@192.168.56.101 with password as mininet.
d. Copy the files from your host machine to mininet's /pox/pox/misx/ folder by "scp topology.py of_tutorial_switch.py of_tutorial_router1.py mininet@192.168.56.101:~/pox/pox/misc/"
e.  Run the command "sudo mn --custom topology.py --topo mytopo --mac --controller remote" on the terminal with mininet> in the folder /pox/pox/misc.
f. Change the directory to "mininet> cd mininet/pox" and execute the command "./pox.py log.level --DEBUG of_tutorial_router1"
g. Execute pingall in mininet> terminal to ping hosts to each other and we can observe that few ports have already learned from the previous ping and few need routing table and check the ping statistics in mininet terminal.
h. In mininet> terminal execute the command "h1 ping -c1 h2" and we can observe the ARP request.
i. In mininet> terminal execute the command "h2 ping -c1 10.0.3.4" and we can see that its unreachable with the unreachable message displayed at controller terminal and the packet being lost.
j. Execute the command iperf in terminal with mininet> to see the bandwidth 