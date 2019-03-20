# Import build-in packages
import logging
import os
import json
import logging.config

# Import our packages
from definitions import ROOT_DIR

# Module configuration
CONFIG_FILENAME = 'logging.json'

# Constants
KEY_HANDLERS = 'handlers'
KEY_FILENAME = 'filename'

# Set module variable for external import
logger = logging.getLogger()

# Private functions
def __read_config():
    path = os.path.join(ROOT_DIR, CONFIG_FILENAME)
    with open(path, 'r') as f:
        result = json.load(f)
    return result

def __create_log_dir():
    global config
    if KEY_HANDLERS in config:
        for handler in config[KEY_HANDLERS].values():
            if KEY_FILENAME in handler:
                log_path = handler[KEY_FILENAME]
                if not os.path.isabs(log_path):
                    log_path = os.path.join(ROOT_DIR, log_path)
                log_dir_path = os.path.dirname(log_path)
                if not os.path.isdir(log_dir_path):
                    os.makedirs(log_dir_path)

# Initialization
config = __read_config()
__create_log_dir()
logging.config.dictConfig(config)
