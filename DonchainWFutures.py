import databento as db
import matplotlib.pyplot as plt

client = db.Historical("INSERTDATABENTOAPIHERE")

dataset = "GLBX.MDP3"
symbols = ["ES.n.0", "ES.n.1"]
start = "2024"

data = client.timeseries.get_range(
    dataset="GLBX.MDP3",
    schema="ohlcv-1d",
    stype_in="continuous",
    symbols=symbols,
    start=start,
)

df = data.to_df()
df.groupby("symbol")["close"].plot(
    xlabel="Date",
    ylabel="Price",
)

plt.legend()
plt.show()