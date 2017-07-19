from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1',ip="10.0.1.100",defaultRoute="via 10.0.1.1" )
        host2 = self.addHost( 'h2',ip="10.0.2.100",defaultRoute="via 10.0.2.1" )
        host3 = self.addHost( 'h3',ip="10.0.3.100",defaultRoute="via 10.0.3.1" )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )

        # Add links
        self.addLink( host1, s1 )
        self.addLink( host2, s1 )
        self.addLink( host3, s2 )
        self.addLink( s1, s2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

