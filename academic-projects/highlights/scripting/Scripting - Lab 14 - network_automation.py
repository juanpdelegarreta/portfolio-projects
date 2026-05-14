from netmiko import ConnectHandler

key_file = "~/.ssh/lab_14/test_rsa"
rt1_cisco = {
    "device_type": "cisco_ios",
    "host": "10.10.10.1",
    "username": "lab_14_test",
    "use_keys": True,
    "key_file": key_file,
    "secret": "abc123"
}

rt2_cisco = {
    "device_type": "cisco_ios",
    "host": "10.10.10.2",
    "username": "lab_14_test",
    "use_keys": True,
    "key_file": key_file,
    "secret": "abc123"
}

sw1_hp = {
    "device_type": "cisco_ios",
    "host": "10.10.10.3",
    "username": "lab_14_test",
    "use_keys": True,
    "key_file": key_file,
    "secret": "abc123"
}

rt_list = [rt1_cisco, rt2_cisco]
rt_commands = ["show version","iproute 192.168.100.0 255.255.255.0 10.10.10.10", "show ip route"]
sw_commands = []

for x in range[2,7]:
    sw_commands.append(f"vlan {x}", f"vlan {x} usernet{x}", f"tagged {x}")

for rt in rt_list:
    ssh_connection = ConnectHandler(**rt)
    ssh_connection.enable()
    result = ssh_connection.send_config_set(rt_commands)
    print(result)
    ssh_connection.disconnect()

ssh_connection = ConnectHandler(**sw1_hp)
ssh_connection.enable()
result = ssh_connection.send_config_set(sw_commands)
print(result)
ssh_connection.disconnect()