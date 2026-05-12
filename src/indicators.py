from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator


def add_sma(df, window=20):

    sma = SMAIndicator(close=df['Close'], window=window)

    df[f'SMA_{window}'] = sma.sma_indicator()

    return df


def add_ema(df, window=20):

    ema = EMAIndicator(close=df['Close'], window=window)

    df[f'EMA_{window}'] = ema.ema_indicator()

    return df


def add_rsi(df, window=14):

    rsi = RSIIndicator(close=df['Close'], window=window)

    df['RSI'] = rsi.rsi()

    return df


def add_macd(df):

    macd = MACD(close=df['Close'])

    df['MACD'] = macd.macd()
    df['MACD_SIGNAL'] = macd.macd_signal()

    return df