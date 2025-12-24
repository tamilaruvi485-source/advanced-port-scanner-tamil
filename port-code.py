import socket
from concurrent.futures import ThreadPoolExecutor

# Resolve domain to IP
def get_ip(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid domain or IP address")
        exit()

# Scan single port
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[OPEN] Port {port:<5} Service: {service}")
        s.close()
    except:
        pass

# Main program
print("="*50)
print("        ADVANCED PORT SCANNER (Python)")
print("      Cybersecurity & Ethical Hacking")
print("="*50)

target = input("Enter target IP / domain: ")
ip = get_ip(target)

print(f"\nTarget IP resolved as: {ip}")
print("Scanning common ports...\n")

common_ports = [
    21, 22, 23, 25, 53, 80, 110,
    135, 139, 143, 443, 445, 3389
]

with ThreadPoolExecutor(max_workers=10) as executor:
    for port in common_ports:
        executor.submit(scan_port, ip, port)

print("\nScan completed.")
print("="*50)

