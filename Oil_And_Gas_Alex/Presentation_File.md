 # Title Slide 

<img src="oil-and-gas-turbines-renewable.jpg" alt="drawing" width="1500" height="857">
---

# Motivation & Summary Slide

## The Oil & Gas industry can ve very complex and confusing to understand. We wanted to explore how to best measure the health of this industry in today's world. 

<img src="https://s.hdnux.com/photos/20/04/75/4214654/9/rawImage.jpg" alt="drawing" width="1000" height="750"> 


## Our Questions

* What is the current state of Oil & Gas?
* To what extent is Alternative Energy taking over Oil & Gas?
* What can the stock market tell us about the health of Oil & Gas?


---
# Questions & Data

##Finding Data

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Yahoo_Finance_Logo_2019.svg/1200px-Yahoo_Finance_Logo_2019.svg.png
" alt="drawing" width="200" height="100"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Energy_Information_Administration_logo.svg/1200px-Energy_Information_Administration_logo.svg.png
" alt="drawing" width="200" height="100"> 


---
# Data Cleanup & Exploration

![](Production.png)
![](Stocks.png) 

## Production
* Read in csv from EIA with total production for petroleum and total production for nuclear and renewables. 
* Dropped columns with excess information.

## Stocks
* Pulled stock price data from Yahoo Finance API:
  * Oil and Gas = BP, XOM, CVX, RDS-B
  * Alternative =  BLX, CIG, ELP, PLUG
* Created data frame with all tickers 

## Issues

* What data to use? What is alternative/renewable energy? 
  * Renewable energy is useful energy that is collected from renewable resources, which are naturally replenished on a human timescale, including carbon neutral sources like sunlight, wind, rain, tides, waves, and geothermal heat.
* Date matching- alternative stock data only went back  went back to 2000 
* Production- finding comparable units of measure
* Stocks- finding enough data. Funds did not go back far enough, so we used individual stocks. 
* Data had to be formatted by years because it came daily


---
# Data Analysis
## Questions Revisited

* What is the current state of Oil & Gas? 
* To what extent is Alternative Energy taking over Oil & Gas?
* What can the stock market tell us about the health of Oil & Gas?

## Energy Production Analysis 
![](Oil_And_Gas/Images/combined_production.png)
* Oil & Gas Production is higher today than it's ever been in history. 
* Alternative Energy production jumped ahead from 2003-2011 and has steadily increased production since 1980.

## Stock Analysis
![](Oil_And_Gas/Images/stock_prices.png)

*NOTE- can we combine into portfolios?

![](Oil_And_Gas/Images/5_year_stdev.png) ![](Oil_And_Gas/Images/stdev_by_industry.png) 

* Alternative Energy is riskier than Oil & Gas

![](Oil_And_Gas/Images/cumulative_returns.png) 

* Alternative Energy returns have been higher than Oil & Gas in the last few years

![](Oil_And_Gas/Images/portfolio_correlation.png) 

![](Oil_And_Gas/Images/production_vs_returns_all.png) 


---
# Discussion
Discuss your findings. Did you find what you expected to find? If not, why not? What inferences or general conclusions can you draw from your analysis?

* Expectations: We expected that Oil and Gas Production would be lower than it was, given the talk about greener energy sources in the news. Instead, we can see that Oil & Gas production has spiked since 2011. 
* Findings:
  * Energy Production: 
  * Standard Deviation: Alternative Energy is more risky than Oil & Gas. 
  * Cumulative Returns: Alternative Energy returns have been higher than Oil & Gas in the last few years. 
  * Correlation: 

---
# Postmortem
* Discuss any difficulties that arose, and how you dealt with them.
* Discuss any additional questions that came up, but which you didn't have time to answer: What would you research next, if you had two more weeks?

![](Headlines.png)

Our original question was: Is the oil and gas industry a viable career path for a college graduate? Should young people who are involved in oil & gas course correct and find a new job? 

The problem with answering this specific question was that the project is based on historical data, and not future projections. (monte carlo simulation??)


We know that there are many more factors for measuring the health of the Oil & Gas Industry. In the future, we would take more factors into account, such as breaking down the uses for Petroleum products into more granular detail: 
  * Transportation fuels
  * Fuel oils for heating and electricity generation
  * Asphalt and road oil
  * Feedstocks for chemicals, plastics, and synthetic materials 

  This would help us understand more of the reasons for why the numbers move in the way that they do. 

---
# Questions
* Open-floor Q&A with the audience
