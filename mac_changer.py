#!/usr/bin/env python3
"""
Using shebang to declare that we need to use Python3 in Kali
"""

import subprocess
import argparse
import re


def get_arguments():
    """Specifying the argument which to be add in the terminal of Kali."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")

    # parser give us 2 vars, but we need only the first
    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC")
    return options


def change_mac(interface, new_mac):
    """Changing the MAC address"""

    print("[+] Starting changing the MAC Address...")

    # Not allowed injection of other command. Data input is validated!
    # calling function ifconfig from shell. First we need to turn off the shell
    subprocess.call(["ifconfig", f"{interface}", "down"])
    # change the mac address with the new one
    subprocess.call(["ifconfig", f"{interface}", "hw", "ether", f"{new_mac}"])
    # turn on the interface again
    subprocess.call(["ifconfig", f"{interface}", "up"])

    print("Configuration is done!")


def get_current_mac(interface):
    """Receiving the interface and getting the current MAC address"""

    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()

    pattern = r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
    mac_address_search_result = re.search(pattern, ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


if __name__ == "__main__":

    options = get_arguments()

    current_mac = get_current_mac(options.interface)
    print(f"Current MAC = {current_mac}")

    # with options.interface/new_mac we get access to the vars in function get_arguments
    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)

    if current_mac == options.new_mac:
        print(f"[+] MAC address was successfully changed to {current_mac}")
    else:
        print("[-] MAC address did not get changed.")
