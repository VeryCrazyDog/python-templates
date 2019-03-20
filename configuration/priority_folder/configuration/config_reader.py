# Import build-in packages
import os
import socket
import configparser

# Import our packages
from definitions import ROOT_DIR

# Module configuration
CONFIG_DIR_NAME = 'config'
LOCAL_CONFIG_DIR_NAME = 'local'
DEFAULT_CONFIG_FILENAME = 'config.ini'

# Internal module variable
__logger = None
__config_dir = None
__configuration = {}

# Private functions
def __find_config_dir():
    config_dir = os.path.join(ROOT_DIR, CONFIG_DIR_NAME)
    result = config_dir
    host_config_dir = os.path.join(config_dir, socket.gethostname().lower())
    if os.path.isdir(host_config_dir):
        result = host_config_dir
    local_config_dir = os.path.join(config_dir, LOCAL_CONFIG_DIR_NAME)
    if os.path.isdir(local_config_dir):
        result = local_config_dir
    return result

# Public functions
def set_logger(logger):
    global __logger
    __logger = logger

def get_configuration(filename = None):
    if filename == None:
        filename = DEFAULT_CONFIG_FILENAME
    global __configuration
    if filename not in __configuration:
        global __config_dir
        if __config_dir == None:
            __config_dir = __find_config_dir()
            if __logger is not None:
                __logger.debug(f'Effective configuration directory: {__config_dir}')
        path = os.path.join(__config_dir, filename)
        if __logger is not None:
            __logger.debug(f'Reading configuration file at: {path}')
        config = configparser.ConfigParser()
        config.read(path)
        __configuration[filename] = config
    return __configuration[filename]

def unload_configuration():
    global __configuration
    __configuration = {}
    __config_dir = None
