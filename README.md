"# Shyfund_AI" 


_________________________alpha vantage api documentation/requirements____________________________________________

import requests: python -m pip install requests



This API returns the simple moving average (SMA) values. See also: SMA explainer and mathematical reference.


API Parameters
❚ Required: function

The technical indicator of your choice. In this case, function=SMA

❚ Required: symbol

The name of the ticker of your choice. For example: symbol=IBM

❚ Required: interval

Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly

❚ Optional: month

Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.

By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history. For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.

❚ Required:time_period

Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., time_period=60, time_period=200)

❚ Required: series_type

The desired price type in the time series. Four types are supported: close, open, high, low

❚ Optional: datatype

By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

❚ Required: apikey

