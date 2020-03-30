from data_structures.cluster import Cluster

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

        pass
    def __repr__(self):
        return "{0} -> {1}".format(self.name, self.clusters)
