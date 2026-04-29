# Import socket and argparse libraries
import argparse
import socket

# Port Scanner Function
def port_scanner(args):
# IP input
    ip_address = args.ip

# Defining starting and ending ports
    start_port = args.sp
    end_port = args.ep

# Function for port to service mapping
    def port_by_service(port_number):
        try:
            port_service = socket.getservbyport(port_number)
            return port_service
        except OSError:
            return 'Unknown'


# Reiterate through a range of ports and output the open ones
    for port in range(start_port, end_port + 1):
        socket_variable = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_variable.settimeout(args.t)
        connection = socket_variable.connect_ex((ip_address, port))
        if connection == 0:
         print(f'Port {port} is open: {port_by_service(port)}')
        socket_variable.close()

# Traceroute function
def traceroute(args):
    # defines destination IP and hop amount
    destination_ip = args.ip
    max_hop = 30

    print(f'Tracing route to {destination_ip}...')

    # Sends packets to destination IP, counting the hops
    for hop in  range(1, max_hop + 1):
        ttl = hop

        # Establishing the receiver and its TTL
        receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        receiver.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Establishing the sender and its TTL
        sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Sending to IP through port and setting timeout
        sender.sendto(b'', (destination_ip, 33434))
        receiver.settimeout(args.t)
        # Try and except statement to bypass timeout error and print *** for errors in hop
        try:
            # Breaking up Tuple
            receiving_data = receiver.recvfrom(512)
            data, address = receiving_data
            # Printing only the address with the hop
            print(address[0], hop)
            if address[0] == destination_ip:
                break
        # For bypassing the error and printing *** instead
        except TimeoutError:
            print (f'Hop {hop}: * * *')

        sender.close()
        receiver.close()

# Banner Grabbing Function
def banner_grab(args):
    # Defines the IP and port
    ip_address = args.ip
    banner_port = args.port

    try:
        # Establishing connection and receiving data
        socket_banner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_banner.settimeout(args.t)
        socket_banner.connect_ex((ip_address, banner_port))
        banner_info = socket_banner.recv(1024)

        # If statement to send back output on closed ports
        if banner_info == b'':
            print('No banner received')
        else:
        # printing and decoding the service info and stripping away characters
            print(banner_info.decode('utf-8').strip())
    # except statement to output in case of error (IP issues)
    except:
        print('Failed to retrieve data')


# Defines the help screen including description
toolkit = argparse.ArgumentParser(description='Tool for Network Diagnosis')

# Arguments for different options available in the tool
toolkit.add_argument('--ip', help='Specifies IP')
toolkit.add_argument('--sp', help='Starting Port', type=int)
toolkit.add_argument('--ep', help='Ending Port', type=int)
toolkit.add_argument('--t', help='timeout', type=int)
toolkit.add_argument('--scan', help='Specify desired scan', action='store_true')
toolkit.add_argument('--traceroute', help='Run Traceroute', action='store_true')
toolkit.add_argument('--port', help='Specify port for banner grabbing', type=int)
toolkit.add_argument('--banner_grab', help='Banner grab for useful service information', action='store_true')

# Storing
args = toolkit.parse_args()

# If statements to make running the tools optional
if args.scan:
    port_scanner(args)
if args.traceroute:
    traceroute(args)
if args.banner_grab:
    banner_grab(args)
