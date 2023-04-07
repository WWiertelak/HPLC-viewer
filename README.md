# HPLC Glyco-Sep Viewer
This program allows you to load and visualize data from High Performance Liquid Chromatography (HPLC) experiments with Glyco-Sep column. Example experiment was described by [Wiertelak et. al(2022)]( https://doi.org/10.1016/j.bbrc.2022.10.019)

## Requirements
This program requires the following libraries:

- pandas
- numpy
- matplotlib

## Installation
To use this program, clone the repository and import the HPLC_Viewer class from the hplc_viewer.py file.

## Initialization
To create an instance of the HPLC_Viewer class, you need to pass a name for your model:

```
my_hplc_viewer = HPLC_Viewer("My HPLC Model")
```

To load data into the HPLC_Viewer instance, you can use the load_data method. The method takes two parameters:

- raw_data: a pandas DataFrame containing raw data from HPLC
- run_time_minutes: the total run time of the HPLC separation in minutes
```
my_hplc_viewer.load_data(raw_data, run_time_minutes)
```
### Cleaning Data
To clean the data, use the clean_data method. The method takes two parameters:

- start: the start time for the separation range of interest
- stop: the stop time for the separation range of interest
```
my_hplc_viewer.clean_data(start, stop)
```
### Scaling Data
To scale the data, use the scale method. This method performs a min-max scaling of the fluorescence values.

```
my_hplc_viewer.scale()
```
### Loading GU Values
To load the retention time of dextran standard with Glucose Unit (GU) values, use the load_GU method. The method takes a pandas DataFrame containing the GU values.

```
my_hplc_viewer.load_GU(GU)
```
### Printing Data
To print the data, use the print_data method.

```
my_hplc_viewer.print_data()
```
### Plotting Data
To plot the data, use the plot method. The method generates a plot of fluorescence vs. time, with GU values shown on the top axis.

```
my_hplc_viewer.plot()
```
