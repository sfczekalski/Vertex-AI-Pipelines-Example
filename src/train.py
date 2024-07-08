import sys
import logging
import pandas as pd


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

X_train_path = sys.argv[1]
y_train_path = sys.argv[2]
X_test_path = sys.argv[3]
y_test_path = sys.argv[4]

df_X_train = pd.read_csv(X_train_path)
df_y_train = pd.read_csv(y_train_path)
df_X_test = pd.read_csv(X_test_path)
df_y_test = pd.read_csv(y_test_path)

logger.info(df_X_train.shape)
logger.info(df_y_train.shape)
logger.info(df_X_test.shape)
logger.info(df_y_test.shape)
