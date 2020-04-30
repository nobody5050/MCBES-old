from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import time
import sys

try:
    server = PyRakLibServer(19132)
    server.logger.info("Starting Proxy")
    handler = ServerHandler(server, None)
    handler.sendOption("name", "MCCPP;MINECON;TestServer")
    server.logger.info("server started!")
except Exception as e:
    server.logger.critical("Failed to start! error:"+str(e))
