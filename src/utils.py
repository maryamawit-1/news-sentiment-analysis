def calculate_daily_returns(df):

    df['Daily_Return'] = df['Close'].pct_change() * 100

    return df