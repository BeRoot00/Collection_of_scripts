import optparse
import nmap

def scanner(tgHost, tgPort):
    #tgHost is the target address and tgPort is the target Port
    scan = nmap.PortScanner()
    scan.scan(tgHost,tgPort)
    status = scan[tgHost]['tcp'][int(tgPort)]['state'] #to get the status of the port (open or close)
    print(" [+] On the host " + str(tgHost) + " the TCP port is " + status)

def runScan():
    parser = optparse.OptionParser()
    parser.add_option('-H', dest='tgHost', type='string', help="specify your target host")
    parser.add_option('-p', dest='tgPort', type='string', help="specify your target port(s)")
    (options, args) = parser.parse_args()
    tgHost = options.tgHost
    tgPorts = str(options.tgPort).split(', ') #seperated by comma

    if (tgHost == None) | (tgPorts[0] == None):
        print("Usage: -H <target host> -p <target port>")
        exit(0)
    for tgPort in tgPorts:
        scanner(tgHost, tgPort)

if __name__ == '__main__':
    runScan()


