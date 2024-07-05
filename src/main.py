import sys
import logging
import pandas as pd


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

dataset_path = sys.argv[1]
df = pd.read_csv(dataset_path)

logger.info(f"Dataset: {df}!")