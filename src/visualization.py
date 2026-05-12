import matplotlib.pyplot as plt


def plot_price_and_ma(df, stock_name):

    plt.figure(figsize=(14, 7))

    plt.plot(df['Date'], df['Close'], label='Close Price')

    if 'SMA_20' in df.columns:
        plt.plot(df['Date'], df['SMA_20'], label='SMA 20')

    if 'EMA_20' in df.columns:
        plt.plot(df['Date'], df['EMA_20'], label='EMA 20')

    plt.title(f'{stock_name} Price with Moving Averages')

    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.legend()

    plt.show()


def plot_rsi(df, stock_name):

    plt.figure(figsize=(14, 4))

    plt.plot(df['Date'], df['RSI'], label='RSI')

    plt.axhline(70, linestyle='--')
    plt.axhline(30, linestyle='--')

    plt.title(f'{stock_name} RSI')

    plt.show()


def plot_macd(df, stock_name):

    plt.figure(figsize=(14, 4))

    plt.plot(df['Date'], df['MACD'], label='MACD')
    plt.plot(df['Date'], df['MACD_SIGNAL'], label='Signal')

    plt.title(f'{stock_name} MACD')

    plt.legend()

    plt.show()