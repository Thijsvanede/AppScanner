# AppScanner
This code implements the Single Large Random Forest Classifier of AppScanner [1].

## Dependencies
This code is written in Python3 and depends on the following libraries:
 * Numpy
 * Pandas
 * Scikit-learn
 * Scapy

To install these use the following command
```
pip3 install -U scapy numpy pandas scikit-learn
```

## Usage
The AppScanner implementation can be tested with the `main.py` script. This script allows you to specify .pcap files to load. After loading, the script splits the data into training and testing data and evaluates the performance. See `main.py --help` for more information.

### API
It is also possible to directly use the AppScanner code as an API. There are two main classes which need to be understood.
 * `preprocessor.py` for extracting features from `.pcap` files.
 * `appscanner.py` for applying the AppScanner detection.

#### Preprocessor
The `Preprocessor` object is used to extract data from `.pcap` files and label them. To this end, it uses the `process` function which requires a list of files and a list of labels. The list of files must be pathnames to pcap files. The list of labels must be labels corresponding to each file. The example below shows how the `Preprocessor` can be used.

##### Example
```python
from preprocessor import Preprocessor

# Create object
preprocessor = Preprocessor()
# Load from files
X, y = preprocessor.process(['<path_file_1>', ..., '<path_file_n>'],
                            ['<label_1>'    , ..., '<label_n>'])
```

#### AppScanner
The `AppScanner` object is used to find known applications in network traffic. It can be `fit` with `X_train` and `y_train` arrays obtained by the `Preprocessor`. After it has been `fit`, the `AppScanner` is able to `predict` unknown samples `X_test`. The example below shows how `AppScanner` can be used.

##### Example
```python
from appscanner import AppScanner

# Create object
scanner = AppScanner()

# Fit scanner
scanner.fit(X_train, y_train)
# Predict labels of test data
y_pred = scanner.predict(X_test)
```

## References
[1] `Taylor, V. F., Spolaor, R., Conti, M., & Martinovic, I. (2016, March). Appscanner: Automatic fingerprinting of smartphone apps from encrypted network traffic. In 2016 IEEE European Symposium on Security and Privacy (EuroS&P) (pp. 439-454). IEEE.`
