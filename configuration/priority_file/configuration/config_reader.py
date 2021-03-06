# Import build-in packages
import configparser
import logging
import os
import socket

# Import our packages
from definitions import ROOT_DIR

# Module configuration
CONFIG_DIR_NAME = 'config'
DEFAULT_CONFIG_BASENAME = 'config'
LOCAL_CONFIG_BASENAME = 'local'
DEFAULT_FILE_EXT = '.ini'

# Internal module variable
__configuration = None

# Private functions
def __find_config_file():
    config_dir = os.path.join(ROOT_DIR, CONFIG_DIR_NAME)
    result = os.path.join(config_dir, f'{DEFAULT_CONFIG_BASENAME}{DEFAULT_FILE_EXT}')
    host_config_file = os.path.join(config_dir, f'{socket.gethostname().lower()}{DEFAULT_FILE_EXT}')
    if os.path.isfile(host_config_file):
        result = host_config_file
    local_config_file = os.path.join(config_dir, f'{LOCAL_CONFIG_BASENAME}{DEFAULT_FILE_EXT}')
    if os.path.isfile(local_config_file):
        result = local_config_file
    return result

# Public functions
def get_configuration():
    global __configuration
    if __configuration == None:
        path = __find_config_file()
        logging.debug(f'Reading configuration file from: {path}')
        config = configparser.ConfigParser()
        config.read(path)
        __configuration = config
    return config

def unload_configuration():
    global __configuration
    __configuration = None
