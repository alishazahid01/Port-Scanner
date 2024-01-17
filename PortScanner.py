# Network port scanner using socket
import socket

# Class for scanning port
class ScanPort:

    #Constructor
    def __init__(self, host_name, start_port, end_port):
        self.host_name = host_name
        self.start_port = start_port
        self.end_port = end_port

    # scanning host ip address     
    def scan_ip(self):
        try:
            host_ip = socket.gethostbyname(self.host_name)
            print('The targeted host IP is:', host_ip)
        except socket.gaierror:
            print('Hostname could not be resolved.')

    # Scanning ports from start_port to end_port
    def scan_ports(self):
        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            try:
                #create a socket object
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_obj.settimeout(1)
                result = socket_obj.connect_ex((self.host_name, port))

                if result == 0:
                    open_ports.append(port)
                else:
                    socket_obj.close()

            #Error Handling
            except socket.error:
                print(f"Error while scanning port {port}.")

        return open_ports
    
    # Print result 
    def result(self):
        open_ports = self.scan_ports()

        for port in open_ports:
            print(f"Port {port} is open")

# __main__
if __name__ == "__main__":

    # Taking various inputs
    host_name = input("Enter the website: ")
    start_port = int(input("Enter starting port # : "))
    end_port = int(input("Enter ending port # : "))
    
    #Calling class anf functions
    scan_port_object = ScanPort(host_name, start_port, end_port)
    scan_port_object.scan_ip()
    scan_port_object.scan_ports()
    scan_port_object.result()

    
