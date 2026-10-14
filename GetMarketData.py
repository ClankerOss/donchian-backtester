import yfinance as yf
import pandas as pd

df = yf.download('BTC-USD', interval='1h', period='2y')

# Flatten MultiIndex columns
df.columns = df.columns.get_level_values(0)
df.columns = [c.lower() for c in df.columns]
df.index.name = 'timestamp'

df.to_parquet("BTCUSD3600.pq")