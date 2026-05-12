import logging, datetime, platform, ipaddress, base64

#Setting the log config
logging.basicConfig(level="INFO", format='%(asctime)s | %(levelname)s | %(lineno)d | %(pathname)s | %(message)s')

#This block of code has the datetime object and uses it with the logging package
right_now = datetime.datetime.now()
logging.info(right_now.strftime("%A"))
logging.info(right_now.strftime("%B %d, %Y"))
logging.info(right_now.year)

#This block of code uses the platform package and its functions
logging.info(platform.architecture())
logging.info(platform.node())
logging.info(platform.processor())
logging.info(platform.python_build())
logging.info(platform.python_version())

#This block of code iterates a log print through all of the IP addresses in the CIDR block
for net in ipaddress.IPv4Network("10.2.0.0/23"):
    logging.info(ipaddress.IPv4Address(net))

#This block creates an info log for private IPs and a warning log for non-private IPs
ip_list = ["1.1.1.1", "192.168.0.5", "10.35.62.19", "100.3.68.2", "172.1.45.16", "172.18.30.12", "245.25.63.49", "172.32.52.73", "10.200.200.45", "49.27.6.25", "192.167.4.92", "192.168.99.100", "10.10.10.10", "8.8.8.8"]
for ip in ip_list:
    address = ipaddress.IPv4Address(ip)
    if address.is_private == True:
        logging.info(f"{ip} is private.")
    else:
        logging.warning(f"{ip} is NOT private!")

#We are doing the logging.info function with the standard decode of the encoded text and then decoded with the utf-8 to return a string
logging.info(
    base64.standard_b64decode(
        "SSBob3BlIHlvdSBhcmUgZW5qb3lpbmcgSVQtMjE1IHNvIGZhciEgQWRkIHRoZSBzZW50YW5jZSAnSSB1bmRlcnN0b29kIHRoZSBhc3NpZ25tZW50IGFuZCB3b3VsZCBsaWtlIGV4dHJhIGNyZWRpdCcgYXQgdGhlIGJvdHRvbSBvZiB5b3VyIHdvcmQgZG9jdW1lbnQgZm9yIGxhYiA3IGFuc3dlcnMgYW5kIEkgd2lsbCBnaXZlIHlvdSAxMCBwb2ludHMgZXh0cmEgY3JlZGl0IQ=="
        ).decode("utf-8")
    )