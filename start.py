from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import time
import sys

print("Starting server!")
try:
    server = PyRakLibServer(19132)
    handler = ServerHandler(server, None)
except Exeption as e:
    print("Failed to start server!")
    print(" ")
    print(e)
