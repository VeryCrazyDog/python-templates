# Import build-in packages
import os
import socket
import configparser

# Import our packages
from definitions import ROOT_DIR

# Module configuration
CONFIG_DIR_NAME = 'config'
LOCAL_CONFIG_DIR_NAME = 'local'
CONFIG_FILENAME = 'config.ini'

# Constant
ENV_NAME_LOG_LEVEL = 'LOG_LEVEL'

# Functions
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

# Set module variable for external import
config_dir = __find_config_dir()
config_reader = configparser.ConfigParser()

# Initialization
config_reader.read(os.path.join(config_dir, CONFIG_FILENAME))
