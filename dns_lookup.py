import socket
from datetime import datetime

print("===== DNS Lookup Tool =====")

while True:
    domain = input("\n Enter website (or type 'exit'): ")

    if domain.lower() == 'exit':
        print("Exiting program...")
        break

    try:
        ip = socket.gethostbyname(domain)
        time = datetime.now()

        print("Domain Name :", domain)
        print("IP Address  :", ip)
        print("Time        :", time)

        # Save result in file
        with open("dns_results.txt", "a") as file:
            file.write(f"{domain} -> {ip} at {time}\n")

    except:
        print("Invalid domain or error!")