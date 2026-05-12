import pandas as pd


def load_stock_data(file_path):
    """
    Load stock CSV data into pandas DataFrame
    """

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['Date'])

    df = df.sort_values('Date')

    return df


def load_news_data(file_path):
    """
    Load financial news dataset
    """

    df = pd.read_csv(file_path)

    # Convert mixed-format dates safely
    df['date'] = pd.to_datetime(
        df['date'],
        errors='coerce',
        utc=True
    )

    return df