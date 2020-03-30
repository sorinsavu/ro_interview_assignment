from data_structures.datacenter import Datacenter
import requests

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    retry = 1
    while retry < max_retries:
        r = requests.get(URL)
        if (r.status_code == 200):
            return r.json()
        retry = retry + 1
    pass
def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')
    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]
    print(datacenters)
    pass  # the rest of your logic here


if __name__ == '__main__':
    main()
