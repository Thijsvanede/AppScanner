import argparse
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocessor import Preprocessor
from appscanner import AppScanner

def extract_labels(files):
    # Initialise result
    result = list()
    # Loop over all files
    for file in files:
        # Extract directory name
        result.append(os.path.split(os.path.dirname(file))[-1])
    # Return result
    return result

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description='AppScanner.')
    parser.add_argument('--files', nargs='+', help='pcap files to run through '
                                                   'AppScanner. We use the '
                                                   'directory of each file as '
                                                   'label')
    parser.add_argument('--save', help='Save preprocessed data to given '
                                       'file.')
    parser.add_argument('--load', help='load preprocessed data from given '
                                       'file.')
    parser.add_argument('--test', type=float, help='Portion of data to be used '
                                                   'for testing. All other '
                                                   'data is used for training. '
                                                   '(default=0.33)')
    parser.add_argument('--threshold', type=float, help='Certainty threshold '
                                                   'used in AppScanner '
                                                   '(default=0.9)')

    # Parse given arguments
    args = parser.parse_args()

    # Create preprocessor object
    preprocessor = Preprocessor(verbose=True)

    # Parse files if required
    if args.files:
        # Extract files and labels
        files  = args.files
        labels = extract_labels(args.files)

        # Load data
        X, y = preprocessor.process(files, labels)

        # Save preprocessed data if necessary
        if args.save:
            preprocessor.save(args.save, X, y)

    # Load data if necessary
    if args.load:
        X, y = preprocessor.load(args.load)

    # Split X and y in training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                           test_size=args.test or 0.33,
                                           random_state=42)

    # Create appscanner object
    appscanner = AppScanner(args.threshold or 0.9)
    # Fit AppScanner
    appscanner.fit(X_train, y_train)
    # Predict AppScanner
    y_pred = appscanner.predict(X_test)

    # Print evaluation report
    print(classification_report(y_test, y_pred))
