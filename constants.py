#!/usr/bin/python3
# *-* coding: utf-8 *-*

import os

kannada_fonts = ["Uni", "Kannada"]

db_params = {}

if os.name == 'nt':
    root_folder = r"D:\rbhus_clone_root"
    db_params = {'host': "localhost", 'db': "test", 'port': 3306, 'user': "root", 'passwd': "password"}
else:
    root_folder = os.path.expanduser(r"~/Documents/rbhus_clone_root")
    db_params = {'host': "mysqlserver", 'db': "test", 'port': 4501, 'user': "hruser", 'passwd': "5Dt09WXa"}

template_folder = os.path.join(root_folder, "template")
database_folder = os.path.join(root_folder, "database")

if not os.path.exists(root_folder):
    os.mkdir(root_folder)
if not os.path.exists(template_folder):
    os.mkdir(template_folder)
if not os.path.exists(database_folder):
    os.mkdir(database_folder)
