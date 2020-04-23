import os
import subprocess
import socket

test = True

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"loadkeys {bcolors.OKBLUE}us{bcolors.ENDC}") #loadkeys
if not test:
    os.system("loadkeys us")

if subprocess.run(["ls", "/sys/firmware/efi/efivars"], stdout=subprocess.DEVNULL).returncode == 0: #check EFI
    is_efi = True
else:
    is_efi = False
print(f"EFI: {bcolors.OKBLUE}{is_efi}{bcolors.ENDC}")

try: #check ethernet connection
    socket.gethostbyaddr('archlinux.org')
except socket.gaierror:
    print(f"{bcolors.WARNING}To use this script you need to be connectet to internet.{bcolors.ENDC}")
    exit()
print(f"Internet: {bcolors.OKGREEN}OK{bcolors.ENDC}")

print(f"timedatectl set-ntp {bcolors.OKBLUE}true{bcolors.ENDC}")
if not test: #set NTP time update
    os.system("timedatectl set-ntp true")
