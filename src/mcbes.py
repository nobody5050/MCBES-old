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
    server.logger.info("Checking if this is a test build...")
    if "TRAVIS" in os.environ:
        handler.shutdown()
        time.sleep(2)
        sys.exit(0)
    else:
      server.logger.info("Not a test build! Enjoy your proxy!")
except Exception as e:
    server.logger.critical("Failed to start! error:"+str(e))
    handler.shutdown()
    time.sleep(2)
    sys.exit(1)
