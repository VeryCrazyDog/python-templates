# Import build-in packages
import os
import socket
import configparser

# Import our packages
from definitions import ROOT_DIR

# Internal module variable

# Functions
def __find_config_dir():
    config_dir = os.path.join(ROOT_DIR, 'config')
    result = config_dir
    host_config_dir = os.path.join(config_dir, socket.gethostname().lower())
    if os.path.isdir(host_config_dir):
        result = host_config_dir
    local_config_dir = os.path.join(config_dir, 'local')
    if os.path.isdir(local_config_dir):
        result = local_config_dir
    return result

config_dir = __find_config_dir()

ini_config = configparser.ConfigParser()
ini_config.read(os.path.join(config_dir, 'config.ini'))

# def get_configuration(logger):
#     global __configuration
#     if __configuration is None:
#         path = os.path.join(ROOT_DIR, 'config.ini')
#         __configuration = configparser.ConfigParser()
#         __configuration.read(path)
#         if logger is not None:
#             logger.debug('Configuration loaded from %s', path)
#     return __configuration


# def unload_configuration():
#     global __configuration
#     __configuration = None
