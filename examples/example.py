# Imports
from appscanner.preprocessor import Preprocessor
from appscanner.appscanner   import AppScanner
from sklearn.preprocessing   import MinMaxScaler

# Create preprocessor
preprocessor = Preprocessor()
# Load from files
X_train, y_train = preprocessor.process(
    files  = ['<path_file_1>', ..., '<path_file_n>'], # Path   to your own train pcap files
    labels = ['<label_1>'    , ..., '<label_n>'],     # Labels of your own train pcap files
)

# Load from files
X_test, y_test = preprocessor.process(
    files  = ['<path_file_1>', ..., '<path_file_n>'], # Path   to your own test pcap files
    labels = ['<label_1>'    , ..., '<label_n>'],     # Labels of your own test pcap files
)

# Scale features
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# Pass through appscanner
scanner = AppScanner(threshold=0.9)

# Fit scanner
scanner.fit(X_train, y_train)
# Predict labels of test data
y_pred = scanner.predict(X_test)