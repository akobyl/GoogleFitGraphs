# Google Fit Data Graphs

This script generates some interesting plots of your lifetime Google Fit data.  

## How to use

You first need to go to your google account and download all Fit data: https://support.google.com/accounts/answer/3024190?hl=en

Once the data is exported you will see a folder `Takeout\\Fit\\Daily Aggregations` which contains a `.csv` file for each day.  Add the absolute path to this folder in the `fitparse.py` file and run!

Currently you need to uncomment the plot which you want to see.  

Install required Python libraries if necessary `pip install -r requirements.txt`

Run the script `python fitparse.py`

## Possible improvements

* Add more plots
* Improve usability
* Improve output display
* Connect directly to google data API