#!/usr/bin/env python3
# Copyright 2021 Andrea Colangelo <andrea.colangelo@gmail.com>.
# This software is released under the terms of the WTFPL (http://www.wtfpl.net/txt/copying/).

import os
import sys

from configparser import ConfigParser
from git import Repo

ADDONS_PATH = sys.argv[1]
ENTERPRISE_PATH = sys.argv[2]
OODO_CONF_TEMPLATE_PATH = sys.argv[3]
ODOO_CONF_PATH = sys.argv[4]

if __name__ == '__main__':
    os.chdir(ADDONS_PATH)
    repo = Repo()

    submodules = [
        os.path.join(ADDONS_PATH, submodule.path)
        for submodule
        in repo.iter_submodules()
    ]
    # Sorting is needed to simulate an undocumented feature of odoo.sh and let
    # this docker-env behave just like that
    submodules = ','.join(sorted(submodules))
    addons_path = ','.join([ADDONS_PATH, ENTERPRISE_PATH, submodules])

    parser = ConfigParser()
    parser.read(OODO_CONF_TEMPLATE_PATH)
    parser.set('options', 'addons_path', addons_path)
    with open(ODOO_CONF_PATH, 'w') as odoo_conf_file:
        parser.write(odoo_conf_file)
