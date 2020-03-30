from data_structures.entry import Entry
from itertools import filterfalse
import ipaddress

def is_valid_ip(net):
    def predicate(e):
        try:
            ip = ipaddress.ip_address(e.address)
            if not ip in net:
                print("ip {} not in network {}".format(e.address,net))
                return True
        except (ValueError, ipaddress.AddressValueError):
            print("invalid ip {} in network {}".format(e.address,net))
            return True
        return False
    return predicate

class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipaddress.ip_network(ipv4_network)
        self.entries = [ Entry(e['address'], e['available'], e['last_used']) for e in raw_entry_list ]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        self.entries[:] = filterfalse(is_valid_ip(self.ipv4_network),self.entries)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
    def __repr__(self):
        return "{0} -> {1}".format(self.ipv4_network, self.entries)
