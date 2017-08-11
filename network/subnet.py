import netaddr
from io import StringIO
from netaddr import *
from os import listdir
from os.path import isfile, join


class Subnets(object):
    def __init__(self, subnets):
        self.subnets = subnets

    @classmethod
    def build_from_directory(cls, directory_path):
        """

        :param directory_path:
        :return: A Subnets object initialised with a list of all the subnets contained in the files in a directory.

        >>> s = Subnets.build_from_directory('./data/test')
        >>> s.subnets
        [IPNetwork('192.136.55.0/24'), IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/24')]
        """
        all_subnets = []
        for file_path in Subnets.get_files_in_directory(directory_path):
            subnets = Subnets.build_subnet_list(file_path)
            all_subnets += subnets
        return cls(all_subnets)

    @staticmethod
    def get_files_in_directory(directory_path):
        """

        :param directory_path: The path of a directory
        :return: A list of paths of files in the derectory

        >>> Subnets.get_files_in_directory('.')
        ['./subnet.py']

        """
        file_list = []
        for filename in listdir(directory_path):
            file_path = join(directory_path, filename)
            if isfile(file_path):
                file_list.append(file_path)
        return file_list

    @staticmethod
    def build_subnet_list(file_path):
        with open(file_path, 'r') as file:
            return Subnets.build_subnet_list_from_file(file)

    @staticmethod
    def build_subnet_list_from_file(file):
        """
        Build a list of subnets from a file.

        :param file: A file of text lines
        :return: A list of subnets

        >>> input = StringIO("103.214.228.0/24\\n192.136.54.0/24\\n")
        >>> Subnets.build_subnet_list_from_file(input)
        [IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/24')]

        """
        subnets = []
        for line in file:
            subnets.append(IPNetwork(line.strip()))
        return subnets

    def merge(self):
        """
        Merge a list of subnets combining adjacent subnets.

        :param subnets: A list of subnets
        :return: A list of merged subnets

        >>> s = Subnets([IPNetwork('192.136.55.0/24'), IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/24')])
        >>> s.merge()
        [IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/23')]
        """
        return netaddr.cidr_merge(self.subnets)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
