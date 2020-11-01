import pandas as pd
from typing import List

idx = pd.date_range(start="1997-01-01", end="1997-01-10", tz="utc", freq="D")

EQUITIES = [
    "JNJ",
    "KO",
    "AXP",
    "HON",
    "DIS",
    "PG",
    "INTC",
    "AMGN",
    "VZ",
    "GS",
    "UNH",
    "CSCO",
    "WMT",
    "JPM",
    "MRK",
    "MCD",
    "MMM",
    "CVX",
    "MSFT",
    "TRV",
    "CAT",
    "WBA",
    "DOW",
    "V",
    "CRM",
    "NKE",
    "IBM",
    "BA",
    "AAPL",
]


def generate_dummy_sp500_components(
    start_date: str, end_date: str, components: List[str] = None
):
    idx = pd.date_range(start=start_date, end=end_date, tz="utc", freq="D")
    df = pd.DataFrame(index=idx)

    if not components:
        df["components"] = ",".join(EQUITIES)
    else:
        raise NotImplementedError("components must be None!")

    return df
