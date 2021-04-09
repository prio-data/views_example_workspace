import logging

from viewser.operations import publish,fetch
from viewser.models import Queryset,Transformed,Database

logging.basicConfig(level=logging.DEBUG)

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
