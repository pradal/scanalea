""" Read csv files and produce TimeSeries Dataframe.

Read csv file with multi-variate information along time.
The data originated from K. Chenu.

Fields:
  - genotype (name)
  - plant (id)
  - phytomer (rank)
  - initiation time (relative to phytomer 1 (post cotyledone) , ie leaf rank#1)
  - surface (t - logistic model, ie P1,P2,Vm)
  - length (final)
  - width (final)
  - petiole length(final)
  - shape (final)

time is thermal.
"""

import pandas as pd

def read(filename, **kwds):
    """
    """
    sep = kwds.pop('sep', ' ')
    index_col = kwds.pop('index_col', None)
    return pd.DataFrame.from_csv(filename, sep=sep, index_col=index_col, **kwds)


def extract_plants(dataset):
    plants = df.plant.unique()
    datasets = []
    for i in plants:
        datasets.append(datasets[datasets['plant']==i])

    return datasets
