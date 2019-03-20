# Import build-in packages
import logging

# Module configuration
LOG_LEVEL = logging.INFO

# Set module variable for external import
logger = logging.getLogger()

# Initialization
logging.basicConfig(
    level = LOG_LEVEL,
    format = '%(asctime)s [%(levelname)s] %(message)s'
)
