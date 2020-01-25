#!/usr/bin/python
import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/apts2/")

from application import main

if __name__ == '__main__':
   main.app.run()
