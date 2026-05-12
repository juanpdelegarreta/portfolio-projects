import argparse
parser = argparse.ArgumentParser()

#adding the arguments
parser.add_argument('--device', help='Provide the device type: Router, Switch, Firewall, or IDS.', choices=['Router','Switch','Firewall','IDS'], required=True)
parser.add_argument('--command',help='Enter command, default is \'version\'', action='store', default='version', dest='run_command')
parser.add_argument('-e','--elevated', help='Elevate the command', action='store_true')

#parsing the arguments
args = parser.parse_args()

#taking action per the arguments
print(f'Your selected device is {args.device}')
print(f'Your selected command is {args.run_command}')
if args.elevated:
    print('With great power comes great responsibility!')