# stock_pillar_analysis

A stock analysis for value investment.

The purpose of this application is to provide a screening on a stock that ease the analysis to the user.

The application provides the math in a "checkbox-style".

We believe, based on past-stock performance and experience in trading stacks that these are the most fundamental rules in screening stocks:

1.	The 5 year Price over Earnings (P/E ratio) must be as low as possible (below 22.5)	
    
    o	This takes the Market Cap (The Shares Outstanding multiplied by its Share price) and divides it by the sum of profit in the last 5 years of the           company. 
    o	This totality gives the user information if the stock is overpriced or underpriced by comparing its stock price with its recent past earnings.
    
2.	The 5 year return of investment capital must be as high as possible (over 9%)
    
    o	This takes the sum of Free Cash Flow in the past 5 years of the company and divides it by the total debt/equity of the company.
    o	This totality gives the user information of how the company manages the money it self-invests to continually make its profit grow and at what             rate, compared to         the total debt it generates.
    
3.	Have revenue growth in the past 5 years

    o	This evaluates the trend in revenue growth of the company and verifies if in the past 5 years is increasing.
    
4.	Have Net Profit growth in the past 5 years
    
    o	This evaluates the trend in net profit growth generated from the company and verifies if in the past 5 years is increasing.
    
5.	The total number of Shares Outstanding is decreasing
   
   o	This evaluates if the company is investing its Free Cash Flow into buying back shares, effectively reducing the amount of shares available to buy         and increasing the value per share.
   
6.	The future long-term-liabilities (or debt) over the 5 year Free Cash Flow (LTL / FCF ratio) must be as low as possible (Below 5)
    
    o	The total debt owed on the long run divided by the average Free Cash Flow over the last 5 years to be less than 5.
    o	This totality gives the user information on how the company manages its Free Cash Flow in paying its debt.
    
7.	Cash Flow Growth in the past 5 years
    
    o	The total sum of Cash from operations minus capital expenditures, to determine the amount of Free Cash Flow available for usage.
    The use of Free Cash Flow consists of:
    o	Paying Dividends
    o	Buy Back Shares
    o	Pay Down Debt
    o	Make Acquisitions
    o	Reinvesting in themselves
    
8.	The Price to Free Cash Flow ratio must be as low as possible (below 20)

    o	This takes the MarketCap and divides it by the Free Cash Flow to try to get a ratio as low as possible.
    o	This is another indicator of weather the stock is overpriced or underpriced.


Instructions for running the program: 

Activate virtual environment: 

$ source venv/Scripts/activate
$ django-admin.py startproject stocks

To run the server, in the C/djangostock/stocks folder: 

$ python manage.py runserver

Migrated the database in a different terminal from the one the server was running on: 

$ python manage.py migrate
Created a super user:

$ python manage.py createsuperuser

For Windows, add winpty:

$ winpty python manage.py createsuperuser

To create an app:
Python manage.py startapp quotes
