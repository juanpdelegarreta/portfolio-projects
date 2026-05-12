from netmiko import ConnectHandler
import sys
import getpass

device = {}
supported_devices = [
    "cisco_asa",
    "cisco_apic",
    "cisco_ftd",
    "cisco_ios",
    "cisco_nxos",
    "cisco_s200",
    "cisco_s300",
    "cisco_tp",
    "cisco_viptela",
    "cisco_wlc",
    "cisco_xe",
    "cisco_xr"
]

while True:
    selection = input("Enter a device type or \'q\' to quit: ").strip()
    if selection.lower() == "q":
        sys.exit()
    elif selection not in supported_devices:
        print(f"That's not a supported device. Select from the following: {supported_devices}")
        continue
    elif selection in supported_devices:
        break

device = {"device_type":selection}
user = input("Enter the username: ").strip()
device.update({"username":user})
passwd = getpass.getpass(prompt="Enter the user's password: ").strip()
device.update({"password":passwd})
enable_pwd = input("Do you want to enter the enable password? y/n:  ").strip().lower()

if enable_pwd == "y":
    enable_pwd = getpass.getpass(prompt="Enter the secret password: ").strip()
    device.update({"secret":enable_pwd})

host = input("Enter the host: ").strip()
device.update({"host":host})

commands = []

while commands:
    if not commands:
        comm = input("Please enter a command:  ").strip()
        commands.append(comm)
    else:
        check = input("Do you want to add another command? y/n").strip().lower()
        if check == "y":
            comm = input("Please enter another command: ").strip()
            commands.append(comm)
        elif check == "n":
            break
        else:
            print("You must choose \'y\' for yes or \'n\' for no.")

ssh_connection = ConnectHandler(**device)
if "secret" in device:
    ssh_connection.enable()
result = ssh_connection.send_config_set(commands)
print(result)
ssh_connection.disconnect()