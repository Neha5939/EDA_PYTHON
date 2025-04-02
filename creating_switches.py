from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel

class SimpleTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')  # Add a virtual switch
        host1 = self.addHost('h1')     # Add host 1
        host2 = self.addHost('h2')     # Add host 2
        self.addLink(host1, switch)    # Link host1 to switch
        self.addLink(host2, switch)    # Link host2 to switch

def run():
    topo = SimpleTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=Controller)
    net.start()
    net.pingAll()  # Test connectivity
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()