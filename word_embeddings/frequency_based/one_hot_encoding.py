def encoding_w_sklearn():
    from sklearn.preprocessing import OneHotEncoder

    # Create an instance of the one-hot encoder
    encoder = OneHotEncoder()

    # Your input data (can be a numpy array or a pandas dataframe)
    input_data = [['red', 'medium'], ['green', 'small'], ['blue', 'large']]

    # Fit the encoder to the input data
    encoder.fit(input_data)

    # Perform one-hot encoding
    one_hot_encoded_data = encoder.transform(input_data).toarray()

    # Print the encoded data
    print(one_hot_encoded_data)


def encoding_w_pandas():
    import pandas as pd

    # Your input data (can be a numpy array or a pandas dataframe)
    input_data = pd.DataFrame({'color': ['red', 'green', 'blue'], 'size': ['medium', 'small', 'large']})

    # Perform one-hot encoding
    one_hot_encoded_data = pd.get_dummies(input_data)

    # Print the encoded data
    print(one_hot_encoded_data)


if __name__ == '__main__':
    encoding_w_sklearn()
    encoding_w_pandas()
