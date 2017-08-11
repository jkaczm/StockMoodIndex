The program StockMoodIndex does three basic things:

1) Retrieves the latest user-specified number of tweets containing a user-specified string (Stock ticker symbol).

2) Sends the text to IBM Watson to analyze its tone

3) Outputs the results as a bar graph


To accomplish 1, the program uses the Tweepy python library to access the Twitter API.
The tweets are in JSON format.  

To accompish 2, the program uses the Watson_Developer_Cloud package to 
interface with the IBM Watson Tone Analyzer API.  The results are also in JSON format.

To accomplish 3, the program uses the matplotlib python library to plot the levels of each tone category.  
The levels range from 0 to 1.  


The program is intended to be a tool to perform sentiment analysis in regard to stocks 
or other financial securities.  However, the program performs the same function for any string 
the user specifies and so can be used to analyze the tone of tweets containing any other keyword.  

 