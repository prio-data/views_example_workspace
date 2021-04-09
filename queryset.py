"""
This script defines a queryset, and then fetches it.

The queryset is defined in a remote database, and can then be fetched with the
'fetch' function from other clients.

"""
import logging

from viewser.operations import publish,fetch
from viewser.models import Queryset,Transformed,Database

logging.basicConfig(level=logging.DEBUG)

"""
First define the queryset.

The name argument specifies the name of the queryset, which is used when
retrieving the data corresponding to it.

The loa argument specifies the level of analysis of the queryset. Currently,
two LOAs are offered: priogrid_month and country_month. Variables can be retrieved
across LOAs (as with country.name here).

The theme argument is simply a string identifier which might be useful for grouping
querysets together? Should probably allow each queryset to have multiple themes / tags.

The operations argument holds a list of lists, containing operations.
Each such list corresponds to a column, and is defined by specifying a database
column, and the operations to apply to it.

In the example shown here, we define a queryset at the priogrid_month level.
For each cell - month, we retrieve country.name values.  We also retrieve
ged_best_ns values for each cell, both as raw values and time-lagged by 1, 2
and 3 steps.
"""

my_queryset = Queryset(
        name = "my_queryset",
        loa = "priogrid_month",
        theme = "testing",
        operations = [
                [
                    Database(path="country.name",args=["values"])
                ],

                [
                    Database(path="priogrid_month.ged_best_ns",args=["values"]),
                ],

                [
                    Transformed(path="lags.tlag",args=["1"]),
                    Database(path="priogrid_month.ged_best_ns",args=["values"]),
                ],

                [
                    Transformed(path="lags.tlag",args=["2"]),
                    Database(path="priogrid_month.ged_best_ns",args=["values"]),
                ],

                [
                    Transformed(path="lags.tlag",args=["3"]),
                    Database(path="priogrid_month.ged_best_ns",args=["values"]),
                ],
            ]
    )

if __name__ == "__main__":
    publish(my_queryset)
    data = fetch(my_queryset.name)
    
    # Analysis goes here 

    data.to_parquet("out.parquet")
