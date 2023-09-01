from termcolor import cprint
from itertools import cycle
from time import sleep
from sys import stdout
import subprocess
import os

colors = iter(cycle(['green', 'green']))
loading_chars = iter(cycle('/-\|'))
os.system('cls')

print('\n Welcome to WiFi Password Extractor(written by Anwar Kamel Ouail)\n')
sleep(.7)

for i in range(40):
    sleep(0.15)
    stdout.write(f'\r Extracting wifi passwords... {next(loading_chars)}')

sleep(1)
print('\n\n\n {:<30}|  Password\n'.format('Host name'))
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode().splitlines()

profiles = [i.split(':', 1)[1][1:] for i in output if 'All User Profile' in i]

for profile in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode(
        'ISO-8859-1').splitlines()
    color = next(colors)

    try:
        password = [b.split(':', 1)[1][1:] for b in result if 'Key Content' in b][0]
        cprint(f' {profile:<30}|  {password}', color=color)

    except:
        cprint(f' {profile:<30}|  <No password>', color=color)

    finally:
        sleep(.7)

figlet = f'''\n
  ___                          _   __                     _ _____             _ _ 
 / _ \                        | | / /                    | |  _  |           (_) |
/ /_\ \_ ____      ____ _ _ __| |/ /  __ _ _ __ ___   ___| | | | |_   _  __ _ _| |
|  _  | '_ \ \ /\ / / _` | '__|    \ / _` | '_ ` _ \ / _ \ | | | | | | |/ _` | | |
| | | | | | \ V  V / (_| | |  | |\  \ (_| | | | | | |  __/ \ \_/ / |_| | (_| | | |
\_| |_/_| |_|\_/\_/ \__,_|_|  \_| \_/\__,_|_| |_| |_|\___|_|\___/ \__,_|\__,_|_|_|

'''

for line in figlet.splitlines():
    print(line)
    sleep(.2)

sleep(1)
input('\n\n Press enter to exit...')
