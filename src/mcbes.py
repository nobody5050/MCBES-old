from .libs.pyraklib.server import PyRakLibServer
from libs.pyraklib.server import ServerHandler
import time
import sys

server.logger.info("Starting Proxy")
try:
    server = PyRakLibServer(19132)
    handler = ServerHandler(server, None)
    handler.sendOption("name", "MCCPP;MINECON;TestServer")
    server.logger.info("server started!")
except Exception as e:
    server.logger.critical("Failed to start! error:"+str(e))
