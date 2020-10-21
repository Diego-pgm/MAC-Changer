#!/usr/bin/env python3

import subprocess
import argparse

"""A script to change the MAC address on Linux with Python 3.5+ from terminal
"""

def change_mac(interface, new_mac):
	"""
	Given an interface and a MAC address and it changes the original MAC address 
	for the given MAC address

	Args:
		interface (str): The interface to change its MAC address
		new_mac (str): The new MAC address  
	"""
	print('[+] Changing MAC address for: ' + interface + "to: " + new_mac)
	subprocess.run(['ifconfig', interface, 'down'])
	subprocess.run(['ifconfig', interface, 'hw ether', new_mac]) 
	subprocess.run(['ifconfig', interface, 'up'])
	


def get_arguments():
	"""
	Returns a tupple of strings containing the interface and the new MAC address
	
	Returns:
		tuple of strings: (interface, new_mac)

	"""
	parser = argparse.ArgumentParser(description='Specify the interface and the new MAC address')
	parser.add_argument('-i', '--interface', dest='interface', help='Interface to change its MAC address')
	parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC address')
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error('[-] Please specify an interface, use --help for more info')
	elif not options.new_mac:
		parser.error('[-] Please specify a MAC address')
	return options


options = get_arguments()
interface = options.interface
new_mac = options.new_mac
change_mac(interface, new_mac)


