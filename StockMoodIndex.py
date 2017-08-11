import tweepy
from watson_developer_cloud import ToneAnalyzerV3
import matplotlib.pyplot as plt 

#Enter Twitter credentials
access_token = "Enter Access Token"
access_token_secret = "Enter Access Token Secret"
consumer_key = "Enter Consumer Key"
consumer_secret = "Enter Consumer Secret"

#Enter IBM Bluemix credentials
Bluemix_username = "Enter Bluemix Username"
Bluemix_password = "Enter Bluemix Password"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#queries the user for the string to search for and the number of tweets to retrieve
query = input("Enter a stock ticker symbol to query: ")
max_tweets = int(input("Enter the number of tweets to retrieve: "))

text_to_analyze = ""

for tweet in tweepy.Cursor(api.search, q = query).items(max_tweets):
    try:
        if(tweet.lang == 'en'):
            print(tweet.text)
            text_to_analyze += tweet.text
    except:
        pass

tone_analyzer = ToneAnalyzerV3(
    username=Bluemix_username,
    password=Bluemix_password,
    version='2016-05-19')

tone = tone_analyzer.tone(text_to_analyze)

tone_categories = ["Anger", "Disgust", "Fear", "Joy", "Sadness", "Analytical", "Confident", "Tentative"]
tone_category_positions = [1,2,3,4,5,6,7,8]
tone_scores = []

for x in range(5):
    tone_scores.append(tone["document_tone"]["tone_categories"][0]["tones"][x]["score"])
for x in range(3):
    tone_scores.append(tone["document_tone"]["tone_categories"][1]["tones"][x]["score"])

plt.bar(tone_category_positions,tone_scores)
plt.xticks(tone_category_positions,tone_categories)
plt.title("tone breakdown of last " + str(max_tweets) + " tweets containing the query " + query)
plt.xlabel("tone category")
axes = plt.gca()
axes.set_ylim([0,1])
plt.show()
