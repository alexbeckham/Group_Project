# Data Cleaning

* ## Finding enough data for the Alternative Energy Industry with yfinance.
    * ## Seemed to only go back to early to mid 2000's.
* ## Getting the proper date formats from yfinance.
    * ## I could only get the daily stock prices.
        * ## So I had to create a function to reformat the date columns to only include the year.
        * ## Then I had to select only the last of each year.
        * ## This essentially showed us the stock price of the last day of each year.


# Stock Prices: Investors' opinion and outlook on the industries.

* ## WHAT does the data tell us.
    * This graph tells us the stock price of 4 stocks from both the Alternative Energy Industry and and the Oil and Gas industry from 1999 to 2020.
    * With regards to direction, they usually follow each other pretty closely. Meaning they usually have a positive correlation.
    * Since 2008 all 4 oil stocks are worth more than any alternative energy stock.
        * This obviously tells us that investors think oil companies and the oil and gas industry is worth more to them than alternative energy companies and their industry.
    * The exception to this rule is PLUG around 2019.
        * This stock skyrockets.
        * That is an interesting development that will come into play all throughout my analysis.
* ## WHAT are the stocks: 
    * ### These are 4 stocks of each industry.
        * Alternative: BLX, CIG, ELP, PLUG
        * Oil & Gas: BP, CVX, RDB-B, XOM
* ## WHY did we choose them.
    * **Alternative**: They are were in a popular clean energy etf called "iShares Global Clean Energy".
    * We only chose 4 of them for two reasons
        1) most of the stocks in that etf weren't really that old. So this made it hard to collect enough data to get a large enough stapshot to compare them to oil companies.
        2) A lot of the stocks in that etf can't be searched using yfinance's api.

    * **Oil and Gas**: We chose these stocks to represent investors' mentality towards the oil and gas industry because these are 4 of the biggest oil companies out there: BP, Chevron, Shell, and Exxon.
        * Unlike the alternative energy industry, which consistently dated back to only around 2000, we could consistently find the price of oil stocks that went back to the early 80's

# Cumulative Returns

* ## What does the data tell us.
    * Between 2000 and 2018 the cumulative returns of the Oil and Gas industry were superior.
    * However, around 2019 the Alternative Energy industry spikes higher than the Oil and Gas industry.
        * At face value, it would seem as though investors are finally realizing the potential of Alternative energy.
        * However, if you remember from the previous graph, all stock trends were usually very similar.
        * This is where we come back to our note about PLUG.
        * The reason for this large spike in Cumulative Returns is completely due to PLUG and it's rocket to the moon.

# 5-Year Rolling Standard Deviation

* ## What does the data tell us?
    * Between the years 2004-2020 the alternative energy portfolio was never lower than the oil and gas industry.
        * Meaning that the alternative energy industry has been a riskier investment than the oil and gas industry for the past 16 years.
# Correlation
* This graph just confirms our initial assumption from the stocks graph that both industries are generally positively correlated.
* It is interesting to note that when you run .corr() on these seemingly positively correlated portfolios, it actually returns a value of 0.04.
    * This again must be due to the fact that PLUG's spike, which was in the opposite direction of all stocks. However, the spike was so large that it carries the rest of the portfolio in the same direction. 
    * This move in the opposite direction by the Alternative Energy portfolio must've been great enough to offset the otherwise positive correlation.
# Conclusion of the risk and returns for both industries in terms of stock performance.

* The cumulative returns of the oil and gas industry from 2000 to 2019 were higher and their risk lower.
    * This tells us that in terms of risk adjusted returns, the oil and gas industry has been superior to the alternative energy industry.
