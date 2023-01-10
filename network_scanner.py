#!/usr/bin/env python3
"""
This script is scanning the local network for all connected nodes.
"""

from scapy.layers.l2 import ARP, Ether, srp
import argparse


def scan(ip):
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
    answered_list = srp(arp_request_broadcast, iface="eth0", timeout=3, verbose=False)[0]

    client_list = []

    # Receiving IP and MAC, combine them in dictionary and add them to list
    for el in answered_list:
        client_dict = {"IP": el[1].psrc, "MAC": el[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(result_list):
    """Receiving information for IP and MAC and print them in nice format for the user"""

    print()
    print("IP Address\t\tMAC Address\n-----------------------------------------")
    for client in result_list:
        # Getting the result from the dictionary and print them
        print(f"{client['IP']}\t\t{client['MAC']}")


def get_ip():
    """Entering the IP on the CLI in Kali"""

    # Making parser instance
    parser = argparse.ArgumentParser()

    # Specify how to call our target
    parser.add_argument("-t", "--target", dest="target", help="Target the IP address")

    # Parsing the object
    result = parser.parse_args()

    # If we dont put IP , we get error msg
    if not result.target:
        parser.error("[-] Please specify an IP")

    # Getting the IP from our object
    return result.target


ip_addresses = get_ip()
scan_result = scan(ip_addresses)
print_result(scan_result)
