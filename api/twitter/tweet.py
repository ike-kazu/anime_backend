import twitter
import os

import api.schemas.article as article_schema

auth = twitter.OAuth(consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
token=os.environ["TWITTER_ACCESS_TOKEN_KEY"],
token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

t = twitter.Twitter(auth=auth)

def tweet(article: article_schema.ArticleCreateResponse):
    
    print(article)
    
    #ツイートのみ
    status = f"""
    新しい記事が投稿されました！！
    {article["articleURL"]}
    #アニメアニメ
    """
    t.statuses.update(status=status) #Twitterに投稿