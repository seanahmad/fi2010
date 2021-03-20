import pandas

url = "https://raw.githubusercontent.com/simaki/fi2010/main/data/data.csv"


def fetch_fi2010() -> pandas.DataFrame:
    """
    Load the FI2010 dataset with no auction.

    Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine
    Learning Methods. A Ntakaris, M Magris, J Kanniainen, M Gabbouj, A Iosifidis.
    arXiv:1705.03233 [cs.CE].  https://arxiv.org/abs/1705.03233
    """
    return pandas.read_csv(url, index_col=0)
