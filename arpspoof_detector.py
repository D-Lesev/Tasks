#!/usr/bin/env python3

from scapy.layers.l2 import ARP, Ether, srp
from scapy.all import sniff


def get_mac(ip):
    """Scanning for all local IP and MAC"""

    # This give us the IP for our target
    arp_request = ARP(pdst=ip)

    # This give us the MAC for our target
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Scapy allow us to combine both layers together
    arp_request_broadcast = broadcast / arp_request

    # This function give us answered and unanswered packets.
    # Verbose = False -> give us less information
    # Timeout -> the time we wait for reaction
    answered_list = srp(arp_request_broadcast, timeout=3, verbose=False)[0]
    return answered_list[0][1].hwsrc


def sniff_packet(interface):
    """sniffing the traffic"""

    # iface = interface via internet
    # store = not save the output in pc
    # prn = should execute function
    sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        try:
            real_mac = get_mac(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc

            if real_mac != response_mac:
                print("[+] You are under attack!")
        except IndexError:
            pass


sniff_packet("eth0")
