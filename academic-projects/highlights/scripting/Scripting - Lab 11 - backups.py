import re

try:
    with open('backups.txt','r') as file:
        data = file.read()

except FileNotFoundError:
    print("File not found, please ensure the file exists.")

except Exception as e:
    print(f"Unkown error occurred: {e}")

else:
    rtr_regex = re.compile(r"(rtr-cinoh)-(\d\d\d\d\d)-(a|b)")
    swt_regex = re.compile(r"(swt-daltx)-(\d\d\d\d\d)-(a|b)")
    old_regex = re.compile(r"(rtr|swt)-(cinoh|daltx)-(\d){,4}-(a|b)")

    rtr_result = rtr_regex.findall(data)
    swt_result = swt_regex.findall(data)
    old_result = old_regex.findall(data)
    
    all_cinoh_rtrs = []
    all_daltx_swt = []
    old_names = []

    count = 0
    for device in rtr_result:
        device_name = f"{rtr_result[count][0]}-{rtr_result[count][1]}-{rtr_result[count][2]}"
        all_cinoh_rtrs.append(device_name)
        count += 1
    
    count = 0
    for device in swt_result:
        device_name = f"{swt_result[count][0]}-{swt_result[count][1]}-{swt_result[count][2]}"
        all_daltx_swt.append(device_name)
        count += 1
    
    count = 0
    for device in old_result:
        device_name = f"{old_result[count][0]}-{old_result[count][1]}-{old_result[count][2]}"
        old_names.append(device_name)
        count += 1

    print(all_cinoh_rtrs)
    print(all_daltx_swt)
    print(old_names)

finally:
    print("Wrapping up the script. Have a nice day!")