# Network-Diagnostics-Toolkit-in-Python

This toolkit includes a port scanner, traceroute, and banner grab.

More may come in the future

Basic Syntax for Port Scanner:
> toolkit.py --scan --ip 127.0.0.1 --sp 1 --ep 100 --t 1

Basic Syntax for Traceroute:
> sudo toolkit.py --traceroute --ip 127.0.0.1 --t 1

Basic Syntax for Banner Grabbing
> toolkit.py --banner_grab --port 22 --ip 127.0.0.1

For any help:
> toolkit.py --help

### Options
--ip = set IP 

--sp = Starting Port for port scanner

--ep = Ending Port for port scanner

--t = timeout 

--port = port for banner grabbing 

--scan = specify port scanner

--traceroute = specify traceroute

--banner_grab = specify banner grabbing 

