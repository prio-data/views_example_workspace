
# ViEWS 3 (views cloud) example repository

This repository demonstrates how to work with views cloud locally. The only
dependency is the `viewser` package (> 0.3.0), which can be installed with 
`pip install viewser`.

After installing viewser, it must be configured. Run `viewser configure` 
and enter the address of a server running views cloud.

Then, you can run the script in this repository with `python queryset.py`,
which will define a queryset and download the data to your working directory.

A queryset is defined as python code, which is published using
`viewser.operations.publish`. The format is shown and explained in
[queryset.py](./queryset.py).
