# Import build-in packages
import configparser
import os
import socket

# Import our packages
from definitions import ROOT_DIR

# Module configuration
CONFIG_FILENAME = 'config.ini'

# Set module variable for external import
config_reader = configparser.ConfigParser()

# Initialization
config_reader.read(os.path.join(ROOT_DIR, CONFIG_FILENAME))
