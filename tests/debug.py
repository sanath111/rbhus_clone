#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import os
import getpass
from logging import *
import tempfile

tempDir = tempfile.gettempdir()
# user = os.environ['USER']
user = getpass.getuser()

FORMAT = "%(asctime)s : %(pathname)s : %(funcName)s - %(levelname)s - %(lineno)d - %(message)s"
basicConfig(filename=tempDir + os.sep + "Rbhus_Clone_" + user + ".log",filemode='a', format=FORMAT, level=INFO)
