import datetime

class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = datetime.datetime.strptime(last_used, '%d/%m/%y %H:%M:%S')

    def __repr__(self):
        return '{0},{1},{2}'.format(self.address,self.available,self.last_used)
