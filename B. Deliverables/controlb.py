

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):

  def __init__ (self, connection):

    self.connection = connection

    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):

    flowMsg = of.ofp_flow_mod()
    flowMsg.idle_timeout = 60
    flowMsg.hard_timeout = 60
    flowMsg.match = of.ofp_match.from_packet(packet)
    flowMsg.data = packet_in


    ip = packet.find('ipv4')



    if ip is None:
        msgAction = of.ofp_action_output(port = of.OFPP_FLOOD)
        flowMsg.actions.append(msgAction)


    else:
        if switch_id is 1:

                if port_on_switch is 1:
                        msgAction = of.ofp_action_output(port = 2)
                        flowMsg.actions.append(msgAction)

                elif port_on_switch is 2:
                        msgAction = of.ofp_action_output(port = 1)
                        flowMsg.actions.append(msgAction)


        elif switch_id is 2:
                if port_on_switch is 1:
                        msgAction = of.ofp_action_output(port = 2)
                        flowMsg.actions.append(msgAction)

                elif port_on_switch is 2:
                        msgAction = of.ofp_action_output(port = 1)
                        flowMsg.actions.append(msgAction)


        elif switch_id is 3:

                if port_on_switch is 1:
                        msgAction = of.ofp_action_output(port = 2)
                        flowMsg.actions.append(msgAction)
                elif port_on_switch is 2:
                        msgAction = of.ofp_action_output(port = 1)
                        flowMsg.actions.append(msgAction)


        elif switch_id is 4:

                if port_on_switch is 1:
                        msgAction = of.ofp_action_output(port = 2)
                        flowMsg.actions.append(msgAction)

                elif port_on_switch is 2:
                        msgAction = of.ofp_action_output(port = 1)
                        flowMsg.actions.append(msgAction)

        elif switch_id is 5:
                if ip.dstip == '10.0.1.10':
                        msgAction = of.ofp_action_output(port = 2)
                        flowMsg.actions.append(msgAction)

                elif ip.dstip == '10.0.1.20':
                        msgAction = of.ofp_action_output(port = 3)
                        flowMsg.actions.append(msgAction)

                elif ip.dstip == '10.0.1.30':
                        msgAction = of.ofp_action_output(port = 4)
                        flowMsg.actions.append(msgAction)

                elif ip.dstip == '10.0.2.10':
                        msgAction = of.ofp_action_output(port = 1)
                        flowMsg.actions.append(msgAction)

                elif ip.dstip == '10.0.4.10':
                        msgAction = of.ofp_action_output(port = 5)
                        flowMsg.actions.append(msgAction)


    self.connection.send(flowMsg)
    return

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed

    packet_in = event.ofp
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)

