import sys
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


X_train_path = Path(sys.argv[1])
y_train_path = Path(sys.argv[2])
X_test_path = Path(sys.argv[3])
y_test_path = Path(sys.argv[4])

X_train_path.parent.mkdir(parents=True, exist_ok=True)
y_train_path.parent.mkdir(parents=True, exist_ok=True)
X_test_path.parent.mkdir(parents=True, exist_ok=True)
y_test_path.parent.mkdir(parents=True, exist_ok=True)

X, y = load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

X_train.reset_index(drop=True).to_csv(X_train_path, index=False)
y_train.reset_index(drop=True).to_csv(y_train_path, index=False)
X_test.reset_index(drop=True).to_csv(X_test_path, index=False)
y_test.reset_index(drop=True).to_csv(y_test_path, index=False)