#!/home/khasan/Документы/tg-bot-QA/myenv/bin/python3
import os
import sys
imported_module = __import__(sys.argv[1])
try:
    print os.path.abspath(os.path.dirname(imported_module.__file__))
except AttributeError:
    print 'stdlib'

