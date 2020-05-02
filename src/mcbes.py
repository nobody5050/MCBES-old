# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import time
import sys
import os

try:
    server = PyRakLibServer(19132)
    server.logger.info("Starting Proxy")
    handler = ServerHandler(server, None)
    handler.sendOption("name", "MCCPP;MINECON;TestServer")
    server.logger.info("server started!")
    server.logger.debug("Checking if this is a test build...")
    if "TRAVIS" in os.environ:
        handler.shutdown()
        time.sleep(2)
        sys.exit(0)
    else:
      server.logger.debug("Not a test build! Enjoy your proxy!")
except Exception as e:
    server.logger.critical("Failed to start! error:"+str(e))
    handler.shutdown()
    time.sleep(2)
    sys.exit(1)
