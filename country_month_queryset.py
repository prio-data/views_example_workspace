from viewser.models import Queryset,DatabaseOperation,TransformOperation,RenameOperation
from viewser.operations import publish,fetch

queryset = Queryset(
        name = "country_month_example_queryset",
        themes = ["testing","delete-me"],
        loa = "country_month",
        description = """
        A queryset I'm using to test the new version of job_manager.
        """,
        operations = [
            [
                RenameOperation(arguments=["ged_sum"]),
                TransformOperation(name = "ops.gte",arguments = ["25"]),
                DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments = ["sum"]),
            ],
            [
                RenameOperation(arguments=["ged_tlag_1"]),
                TransformOperation(name = "lags.tlag",arguments = ["1"]),
                TransformOperation(name = "ops.gte",arguments = ["25"]),
                DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments = ["sum"]),
            ],
            [
                RenameOperation(arguments=["ged_tlag_2"]),
                TransformOperation(name = "lags.tlag",arguments = ["2"]),
                TransformOperation(name = "ops.gte",arguments = ["25"]),
                DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments = ["sum"]),
            ],
            [
                RenameOperation(arguments=["ged_tlag_3"]),
                TransformOperation(name = "lags.tlag",arguments = ["3"]),
                TransformOperation(name = "ops.gte",arguments = ["25"]),
                DatabaseOperation(name = "priogrid_month.ged_best_ns",arguments = ["sum"]),
            ],
        ]
    )

if __name__ == "__main__":
    publish(queryset)
    df = fetch("country_month_example_queryset")
    df.to_parquet("country_month_example_queryset.parquet")
