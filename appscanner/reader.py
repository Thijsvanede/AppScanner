from scapy.all import *
import numpy as np
import ipaddress

class Reader(object):

    def __init__(self, verbose=False):
        """Reader object for reading packets from .pcap files.

            Parameters
            ----------
            verbose : boolean, default=false
                If True, print which files are being read.
            """
        self.verbose = verbose

    def read(self, infile):
        """Read TCP packets from input file.

            Parameters
            ----------
            infile : string
                pcap file from which to read packets.

            Returns
            -------
            result : list
                List of packets extracted from pcap file.
                Each packet is represented as a list of:
                 - timestamp
                 - IP source (in byte representation)
                 - IP destination (in byte representation)
                 - TCP source port
                 - TCP destination port
                 - packet length.
            """
        # If verbose, print loading file
        if self.verbose:
            print("Loading {}...".format(infile))

        # Set buffer of packets
        self.packets = []
        # Process packets in infile
        sniff(prn=self.extract, lfilter=lambda x: TCP in x, offline=infile)

        # Convert to numpy array
        self.packets = np.array(self.packets)
        # In case of packets, sort on timestamp
        if self.packets.shape[0]:
            # Sort based on timestamp
            self.packets = self.packets[self.packets[:, 0].argsort()]

        # Return extracted packets
        return self.packets

    def extract(self, packet):
        """Extract relevant fields from given packet and adds it to globel
           self.packets variable.

            Parameters
            ----------
            packet : scapy.IP
                Scapy IP packet extracted by sniff function.
            """
        # Extract relevant content from packet
        data = [float(packet.time),
                int(ipaddress.ip_address(packet["IP"].src)),
                int(ipaddress.ip_address(packet["IP"].dst)),
                packet["TCP"].sport,
                packet["TCP"].dport,
                packet["IP"].len]
        # Add packet to buffer
        self.packets.append(data)
