# CYBERMAFIA-PH
# Coded By AnonPrixor
# Reverse IP i'm selling Reverse IP Premium
import os
import sys
import requests
import wget
import time
import platform
# Nothing
try:
	from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
except Exception as e:
	print('[X] http-request-randomizer required! / pip install http-request-randomizer')
# Nothing
if platform.system() == "Windows":
	cmd = "cls"
	exc = "python"
else:
	cmd = "clear"
	exc = "python3"
#logo
def logo():
	print("""

					\033[1;33;40m██████╗ ██╗  ██╗       ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ███╗ █████╗ ███████╗██╗ █████╗ 
					\033[1;33;40m██╔══██╗██║  ██║      ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔════╝██║██╔══██╗
					\033[1;33;40m██████╔╝███████║█████╗██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██╔████╔██║███████║█████╗  ██║███████║
					\033[1;31;40m██╔═══╝ ██╔══██║╚════╝██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██╔══╝  ██║██╔══██║
					\033[1;31;40m██║     ██║  ██║      ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║     ██║██║  ██║
					\033[1;31;40m╚═╝     ╚═╝  ╚═╝       ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                    \033[1;35;40m                                        REVERSE IP / Coded By AnonPrixor                                                
		""")
# This is the magic happen.
def magic():
	logo()
	# Example
	print("\033[1;32;40mExample: python3 mafia.py <IP>\r\n")
	# Input Target
	target = input("\033[1;33;40mEnter Target#~ ")
	#target = sys.argv[1]
	# Reverse web
	sites = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + target).text
	# To print the text inside 
	print(sites)

magic()
