#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Practice for read .ini file
date: 2020.12.07
"""

from configparser import ConfigParser


def read_db_config(filename: str ='/home/secwalker/gitProjects/Python005-01/week03/homework/config.ini', section: str = 'mysql') -> dict:
    """Read database configuration file
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception(f'{section} not found in the {filename} file')

    return dict(items)

if __name__ == "__main__":
    print(read_db_config())