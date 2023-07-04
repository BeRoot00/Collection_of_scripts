import socket
import os
import sys

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, vuln_list):
    f = open(vuln_list, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print(" [+] Server is vulnerable to : ", banner.strip('\n'))

def main():
    if len(sys.argv) == 2:
        vuln_list = sys.argv[1]
        if not os.patrh.isfile(vuln_list):
            print("[-]" + vuln_list + " doesn't exist")
            exit(0)
        if not os.access(vuln_list, os.R_OK):
            print("[-]" + vuln_list + " access denied")
            exit(0)
    else:
        portList = [21,22,25,80,110,443]
        for x in range(2,253):
            ip = "192.168.1." + str(x)
            for port in portList:
                banner = retBanner(ip, port)
                if banner:
                    print("[+] " + ip + ": " + banner)
                    checkVulns(banner, vuln_banners.txt)
if __name__=='__main__':
    main()
