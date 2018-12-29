import sys
from scapy.all import *

def main():
    src_net = '192.168.0.'
    dst_ip = '127.0.0.1'
    dst_port = 3000
    sleep = 1
    for src_host in range(2, 254):
        for src_port in range(1024, 1030):
            print(f'sending from {src_net}{src_host}:{src_port} to {dst_ip}:{dst_port}')
            src_ip = src_net+str(src_host)
            network_layer = IP(src=src_ip, dst=dst_ip)
            transport_layer = ICMP()
            send(network_layer/transport_layer)

if __name__ == '__main__':
    main()
