import sys
import logging
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path


logger = logging.getLogger(__name__)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

X_train_path = sys.argv[1]
y_train_path = sys.argv[2]
X_test_path = sys.argv[3]
y_test_path = sys.argv[4]
model_save_path = Path(sys.argv[5])
model_save_path.parent.mkdir(parents=True, exist_ok=True)

df_X_train = pd.read_csv(X_train_path)
df_y_train = pd.read_csv(y_train_path)
df_X_test = pd.read_csv(X_test_path)
df_y_test = pd.read_csv(y_test_path)


model = DecisionTreeClassifier(random_state=42)
model.fit(df_X_train, df_y_train)

y_pred = model.predict(df_X_test)
accuracy = accuracy_score(df_y_test, y_pred)
logger.info(f"Model accuracy on test set: {round(accuracy, 3)}")

joblib.dump(model, model_save_path)