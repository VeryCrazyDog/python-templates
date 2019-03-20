# Import build-in packages
import os
import logging

# Module configuration
DEFAULT_LOG_LEVEL = logging.INFO

# Constant
ENV_NAME_LOG_LEVEL = 'LOG_LEVEL'

# Internal module variable
__log_level = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARN': logging.WARN,
    'WARNING': logging.WARN,
    'ERROR': logging.ERROR,
    'FATAL': logging.CRITICAL,
    'CRITICAL': logging.CRITICAL
}.get(os.getenv(ENV_NAME_LOG_LEVEL, '').upper(), DEFAULT_LOG_LEVEL)

# Set module variable for external import
logger = logging.getLogger()

# Initialization
logging.basicConfig(
    level = __log_level,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)
