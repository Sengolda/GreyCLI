import os, subprocess
import sys
import random
from termcolor import colored

to_print = """
    ____                 ____ _     ___ 
    / ___|_ __ ___ _   _ / ___| |   |_ _|
    | |  _| '__/ _ \ | | | |   | |    | | 
    | |_| | | |  __/ |_| | |___| |___ | | 
    \____|_|  \___|\__, |\____|_____|___|
                    |___/ 
"""

print(colored(to_print, 'cyan'))
random_choiced_name = f'setup-{random.randint(100, 999)}'
supported_systems = ('darwin','linux')

token = input(colored("Token:", 'green'))

if sys.platform in supported_systems:
    subprocess.run(f"git clone https://github.com/Sengolda/greybot.git && mv greybot {random_choiced_name}", shell=True)
    subprocess.run(f'cd {random_choiced_name} && rm -f env.example', shell=True)
    subprocess.run(f"echo token={str(token)} > {random_choiced_name}/env", shell=True)

    print(colored('[+] Added env file.', 'green'))
    print(colored(f'[+] Success, your template is ready\nto start it just do `cd {random_choiced_name} && sh startbot.sh`', 'green'))
else:
    print(f"Sorry, your system is not supported by GreyCLI.")