Network Port Scanner Documentation
Introduction

The Network Port Scanner is a Python script that allows users to scan a range of ports on a specified host or IP address to determine which ports are open and accessible. It utilizes the socket library to establish connections with the target host on different ports. This documentation provides an overview of the code structure, usage, and dependencies.
Getting Started

To use the Network Port Scanner script, follow these steps:

    Clone or download this repository to your local machine.

    Open the Python script in a code editor or integrated development environment (IDE).

    Run the script using the command:

    python port_scanner.py

    Follow the prompts to specify the target host or IP address, the range of ports to scan, and view the results.

Code Structure

The Network Port Scanner script consists of the following components:
1. ScanPort Class

class ScanPort:

    # Constructor
    def __init__(self, host_name, start_port, end_port):
        self.host_name = host_name
        self.start_port = start_port
        self.end_port = end_port

This class is the core of the scanner and is responsible for scanning a range of ports on a specified host. It takes the target host name or IP address, the starting port number, and the ending port number as input parameters.
2. IP Address Resolution

    # Scanning host IP address     
    def scan_ip(self):
        try:
            host_ip = socket.gethostbyname(self.host_name)
            print('The targeted host IP is:', host_ip)
        except socket.gaierror:
            print('Hostname could not be resolved.')

This method resolves the target host's IP address using socket.gethostbyname(). It prints the IP address if successful or indicates that the hostname could not be resolved in case of an error.
3. Port Scanning


    # Scanning ports from start_port to end_port
    def scan_ports(self):
        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            try:
                # Create a socket object
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_obj.settimeout(1)
                result = socket_obj.connect_ex((self.host_name, port))

                if result == 0:
                    open_ports.append(port)
                else:
                    socket_obj.close()

            # Error Handling
            except socket.error:
                print(f"Error while scanning port {port}.")

        return open_ports

This method performs the actual port scanning. It iterates through the specified range of ports and attempts to establish a connection with each port on the target host. If the connection is successful (port is open), it is added to the list of open ports.
4. Result Display


    # Print result 
    def result(self):
        open_ports = self.scan_ports()

        for port in open_ports:
            print(f"Port {port} is open")

This method displays the results of the port scan by calling the scan_ports method and printing the list of open ports.
5. Main Execution


if __name__ == "__main__":

    # Taking various inputs
    host_name = input("Enter the website: ")
    start_port = int(input("Enter starting port # : "))
    end_port = int(input("Enter ending port # : "))
    
    # Calling class and functions
    scan_port_object = ScanPort(host_name, start_port, end_port)
    scan_port_object.scan_ip()
    scan_port_object.scan_ports()
    scan_port_object.result()

The main part of the script prompts the user to enter the target host or IP address, the starting port number, and the ending port number. It then creates an instance of the ScanPort class and calls its methods to perform the port scan and display the results.
Usage

    Run the Python script to initiate the Network Port Scanner:

    python port_scanner.py

    Enter the target host name or IP address when prompted.

    Specify the range of ports you want to scan by entering the starting and ending port numbers.

    The script will scan the specified range of ports on the target host and display the list of open ports.

    Open ports indicate services or applications that are accessible on the target host.

Conclusion

This documentation provides an overview of the Network Port Scanner script, which allows you to scan a range of ports on a target host to identify open ports. You can use this script to perform network reconnaissance and identify potential services running on a target machine for security and troubleshooting purposes.
