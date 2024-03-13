import os, sys
os.system("git pull")
try:
    __import__("King").XYZ()
except Exception as e:
    exit(str(e))
