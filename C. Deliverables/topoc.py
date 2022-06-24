#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):
    #adding hosts and switches
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    # addinf Core Switch cs5
    cs5 = self.addSwitch('cs5')
    s4 = self.addSwitch('s4')
    h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='10.0.1.10/24',defaultRoute="h1-eth0") 
    h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='10.0.1.20/24',defaultRoute="h2-eth0") 
    h3 = self.addHost('h3',mac='00:00:00:00:00:03',ip='10.0.1.30/24',defaultRoute="h3-eth0") 
    h4 = self.addHost('h4',mac='00:00:00:00:00:04',ip='10.0.2.10/24',defaultRoute="h4-eth0") 
    server= self.addHost('server',mac='00:00:00:00:00:05',ip='10.0.4.10/24',defaultRoute="server-eth0") 
    #adding links 
    self.addLink(h1,s1)
    self.addLink(h2,s2)
    self.addLink(h3,s3)
    self.addLink(h4,cs5)
    self.addLink(server,s4)
    self.addLink(s1,cs5)
    self.addLink(s2,cs5)
    self.addLink(s3,cs5)
    self.addLink(cs5,s4)

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()
  
  CLI(net)

  net.stop()


if __name__ == '__main__':
  configure()
