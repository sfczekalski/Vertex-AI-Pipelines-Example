import sys
import logging


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

name = sys.argv[1]
logger.info(f"Hello {name}!")