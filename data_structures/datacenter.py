from data_structures.cluster import Cluster
from itertools import filterfalse
import re
import logging

def is_valid_cluster(name):
    r = re.compile(name[0:3].upper() + '-\\d{1,3}')
    def predicate(c):
        if not r.fullmatch(c.name):
            logging.warning("removing {} from {}".format(c.name,name))
            return True
        return False
    return predicate

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = [Cluster(key,value['networks'],value['security_level']) for key, value in cluster_dict.items()]
    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        self.clusters[:] = filterfalse(is_valid_cluster(self.name),self.clusters)
    def __repr__(self):
        return "{0} -> {1}".format(self.name, self.clusters)
