import netaddr
from io import StringIO
from netaddr import *
from os import listdir
from os.path import isfile, join

def build_subnet_list(file_path):
    """
    Build a list of subnets from a file

    :param file_path: The path to a file of text lines
    :return: A list of subnets

    """
    with open(file_path, 'r') as file:
        return build_subnet_list_from_file(file)

def build_subnet_list_from_file(file):
    """
    Build a list of subnets from a file.

    :param file: A file of text lines
    :return: A list of subnets

    >>> input = StringIO("103.214.228.0/24\\n192.136.54.0/24\\n")
    >>> build_subnet_list_from_file(input)
    [IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/24')]

    """
    subnets = []
    for line in file:
        subnets.append(IPNetwork(line.strip()))
    return subnets

def merge_subnets(subnets):
    """
    Merge a list of subnets combining adjacent subnets.

    :param subnets: A list of subnets
    :return: A list of merged subnets

    >>> subnets = [IPNetwork('192.136.55.0/24'), IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/24')]
    >>> merge_subnets(subnets)
    [IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/23')]
    """
    return netaddr.cidr_merge(subnets)

def get_files_in_directory(directory_path):
    """

    :param directory_path: The path of a directory
    :return: A list of paths of files in the derectory

    >>> get_files_in_directory('.')
    ['./subnet.py']

    """
    file_list = []
    for filename in listdir(directory_path):
        file_path = join(directory_path, filename)
        if isfile(file_path):
            file_list.append(file_path)
    return file_list;

def get_subnets_from_files(directory_path):
    """
    Creates a list of subnets built from all the subnets contained in the files in a directory.

    :param directory_path:
    :return: A list of subnets contained in the files

    >>> get_subnets_from_files('./data/test')
    [IPNetwork('103.214.228.0/24'), IPNetwork('192.136.54.0/23')]

    """
    all_subnets = []
    for file_path in get_files_in_directory(directory_path):
        # print(file_path)
        subnets = build_subnet_list(file_path)
        # print(subnets)
        all_subnets = all_subnets + subnets
    return merge_subnets(all_subnets)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
