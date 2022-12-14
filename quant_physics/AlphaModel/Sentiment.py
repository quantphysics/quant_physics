import tweepy #Twitter API
import praw #Reddit API
from textblob import TextBlob


class SentimentAnalysis:
    """
    Abstraction for various platforms which will require sentiment analysis
    """

    def get_sentiment(self, texts):
        """
        Get the sentiment of a list of texts

        Input:
        * texts (list of strings) - list of texts, analyze sentiment of each text

        Return:
        * sentiment (float) - On a scale [-1.0, 1.0]. Negative to positive feelings within those text.
        """
        if isinstance(texts, list):
            sentiments = [TextBlob(t).sentiment.polarity for t in texts]
            return sum(sentiments) / len(sentiments)
        else: #For handling if you only put in one text
            sentiment = TextBlob(texts).sentiment.polarity
            return sentiments

        

class Reddit(SentimentAnalysis):
    '''
    Inherits from SentimentAnalysis class.
    When you initalize `Reddit`, this serves as the client.

    Inputs:
    * client_id (string)
    * client_secrete (string)
    * user_agent (string)

    How to set up the praw.Reddit() client stuff:
    https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
    
    Returns:
    1 for successful login.
    0 for failed login.
    '''
    def __init__(self, client_id, 
                       client_secret, 
                       user_agent):

        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent

        # Once Reddit is called, initalize logging into reddit
        try:
            self.reddit = praw.Reddit(client_id=client_id,
                                      client_secret=client_secret, 
                                      user_agent=user_agent)
            return 1
        except:
            print("Login failed, incorrect creditials")
            return 0

    def get_subreddit_sentiment(self, subreddit, limit=100):
        """
        Input:
        * subreddit (string) - name of subreddit (i.e. 'apple', 'ios')
        * limit (int) - limit for number of 'hottest' post to look at

        Return:
         * sentiment (float) - On a scale [-1.0, 1.0]. Negative to positive feelings within those text.
                               Comes from a method from SentimentAnalysis
        """
        # Use the PRAW library to access the subreddit
        subreddit = self.reddit.subreddit(subreddit)

        # Extract the text of each post on the subreddit
        texts = [p.title for p in subreddit.hot(limit=limit)]
        sentiments = self.get_sentiment(texts)
        
        return sentiments

class Twitter(SentimentAnalysis):
    '''
    Inherits from SentimentAnalysis class

    Inputs:
    * YOUR_CONSUMER_KEY (string)
    * YOUR_CONSUMER_SECRET (string)
    * YOUR_ACCESS_TOKEN (string)
    * YOUR_ACCESS_TOKEN_SECRET (string)

    Returns:
    1 for successful login.
    0 for failed login.
    '''

    def __init__(self, YOUR_CONSUMER_KEY,
                       YOUR_CONSUMER_SECRET,
                       YOUR_ACCESS_TOKEN,
                       YOUR_ACCESS_TOKEN_SECRET,):
        
        self.YOUR_CONSUMER_KEY = YOUR_CONSUMER_KEY
        self.YOUR_CONSUMER_SECRET = YOUR_CONSUMER_SECRET
        self.YOUR_ACCESS_TOKEN = YOUR_ACCESS_TOKEN
        self.YOUR_ACCESS_TOKEN_SECRE = YOUR_ACCESS_TOKEN_SECRET

        # Once Twitter is called, initalize logging into Twitter

        try:
            auth = tweepy.OAuthHandler(YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET)
            auth.set_access_token(YOUR_ACCESS_TOKEN, YOUR_ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(auth)
            return 1
        except:
            print("Login failed, incorrect creditials")
            return 0


    def get_twitter_sentiment(self, topic, limit):
        """
        Input:
        * topic (string) - name of topic to gather sentiment (i.e. "#apple, #ios)
        * limit (int) - limit for number of 'hottest' post to look at

        Return:
         * sentiment (float) - On a scale [-1.0, 1.0]. Negative to positive feelings within those text.
                               Comes from a method from SentimentAnalysis
        """
        # Use the tweepy library to access the Twitter API
        # Use the search() method of the API to search for tweets about the specified topic
        tweets = self.api.search(q=topic, lang="en", count=limit)

        # Extract the text of each tweet and calculate the sentiment of each tweet
        # using a sentiment analysis library, such as TextBlob, and return the average sentiment of all the tweets
        sentiments = self.get_sentiment(tweets)

        return sentiments
