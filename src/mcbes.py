# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
import config_files.config as cfg
import time
import sys
import os
import json
import logging as log

if "TRAVIS" in os.environ:
    try:
        server = PyRakLibServer(19132)
        handler = ServerHandler(server, None)
        handler.sendOption("name", "MCCPP;MINECON;TestServer")
        time.sleep(10)
        handler.shutdown()
        time.sleep(2)
        sys.exit(0)
    except Exception as e:
        server.logger.critical("Failed to start! error:"+str(e))
        handler.shutdown()
        time.sleep(2)
        sys.exit(1)
else:
    try: 
        name = json.loads(cfg.server.name)
        server = PyRakLibServer(19132)
        log.info("Starting MCBES proxy! version 1.0")
        handler = ServerHandler(server, None)
        handler.sendOption("name", "MCCPP;MINECON;TestServer")
        log.info("server started!")
    except Exception as e:
        log.critical("Failed to start! error:"+str(e))
        handler.shutdown()
        time.sleep(2)
        sys.exit(1)
