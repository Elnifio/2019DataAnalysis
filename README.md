# 2019DataAnalysis

**CHINESE INCLUDED**

This project fetches company data from IEXCloud 
and then creates a model that predicts the stock growth 
based on the earnings that this company posted.

### Required Modules
* pandas
* re
* sklearn
* matplotlib
* requests
* asyncio & aiohttp
* json
* sys & os

### Project Description
The ./Download_folder contains all raw data fetched on IEXCloud, 
as well as Python scripts used to download these data. 
All processed data were stored in current (src) folder.

All historical data - company earnings - 
are stored in ./normal_historical_data folder. 
Each file in this folder holds the stock data in the previous year for each company. 
./organized_data.txt holds all the earnings data in the previous fiscal period.
./overall_data.csv holds the detailed data 
- Name, EPS Surprise Dollar, delta open, and fiscal period.
Modeling in modeling.py.
