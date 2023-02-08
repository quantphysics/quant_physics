import praw # Reddit API
import datetime
import pandas as pd
import concurrent.futures #

class Redditor:
    '''
    Args:
    - client_id (string)
    - client_secrete (string)
    - user_agent (string)

    How to set up the praw.Reddit() client:
    https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
    '''

    __accepted_time_filter__ = ["all", "day", "hour", "month", "week", "year"]

    def __init__(self, client_id, 
                       client_secret, 
                       user_agent, 
                       read_only=True):

        self.subreddit = None

        # Once Reddit is called, initalize logging into reddit
        try:
            self.reddit = praw.Reddit(client_id=client_id,
                                      client_secret=client_secret, 
                                      user_agent=user_agent)
        except:
            raise ValueError('Login credientials failed.')

    def select_subreddit(self, subreddit):
      '''
      After initializing Redditor w/ login credentias,
      choose a subreddit to look at.

      Args
      - subreddit (string): 

      Returns
      - self (Redditor): 

      Example Usage:
      ```
      redditor = Redditor(...)
      wsb = redditor.select_subreddit('wallstreetbets')
      ```
      '''
      self.subreddit = self.reddit.subreddit(subreddit)
      return self
    
    def get_hot(self, limit=50, **kwargs) -> pd.DataFrame:
      '''
      Grab hot posts of subreddit.
      '''
      hot_posts = self._posts_to_dataframe(self.subreddit.hot(limit=limit, **kwargs))
      return hot_posts

    def get_top(self, time_filter, limit=50, **kwargs) -> pd.DataFrame:
      '''
      Grab top posts of subreddit for a given time frame.
      '''
      if time_filter not in self.__accepted_time_filter__:
        raise ValueError('`time_filter` must be: {}'.format(self.__accepted_time_filter__))
      top_posts = self._posts_to_dataframe(self.subreddit.top(time_filter, limit=limit, **kwargs))
      return top_posts

    def get_controversial(self, time_filter, limit=50, **kwargs) -> pd.DataFrame:
      '''
      Grab controversial posts of subreddit for a given time frame
      '''
      if time_filter not in self.__accepted_time_filter__:
        raise ValueError('`time_filter` must be: {}'.format(self.__accepted_time_filter__))
      controversial_posts = self._posts_to_dataframe(self.subreddit.controversial(time_filter=time_filter, limit=50, **kwargs))
      return controversial_posts
    
    def get_new(self, limit=50, **kwargs):
      '''
      Grab new posts of a subreddit
      '''
      new_posts = self._posts_to_dataframe(self.subreddit.new(limit=limit, **kwargs))
      return new_posts
    

    def _posts_to_dataframe(self, posts: list) -> pd.DataFrame:
      '''
      Parallel processing of posts to create DataFrame

      Args:
      - posts (list(praw.models.Submission)): 

      Returns:
      - df (pd.DataFrame): DataFrame template of all posts
      '''
      with concurrent.futures.ThreadPoolExecutor() as executor:
          data = list(executor.map(self._process_post, posts))
      df = pd.DataFrame(data)
      return df
  
    def _process_post(self, post: 'praw.models.Submission') -> dict:
      '''
      Processes a post into dictionary
      '''
      info = {}

      info['author'] = post.author.name
      info['author_id'] = post.author.id
      info['author_num_followers'] = post.author.subreddit.subscribers
      info['author_link_karma'] = post.author.link_karma
      info['author_comment_karma'] = post.author.comment_karma
      info['author_is_gold'] = post.author.is_gold
      info['author_has_verified_email'] = post.author.has_verified_email
      info['post_created_date_utc'] = post.created_utc
      info['post_id'] = post.id
      info['title'] = post.title
      info['body'] = post.selftext 
      info['score'] = post.score
      info['upvote_ratio'] = post.upvote_ratio, 
      info['num_upvotes'] = post.score * post.upvote_ratio
      info['num_downvotes'] = post.score * (1 - post.upvote_ratio)
      info['num_comments'] = post.num_comments
      info['num_crossposts'] = post.num_crossposts
      info['num_reports'] = post.num_reports
      info['num_awards'] = len(post.all_awardings)
      info['is_sticked'] = post.stickied

      return info