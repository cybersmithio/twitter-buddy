import twitter
import os

class TwitterBuddy(object):
    def __init__(self):
        print(f"Authenticating to Twitter with consumer key: {os.environ.get('twitter_consumer_key')}")
        self.api = twitter.Api(consumer_key=os.environ.get("twitter_consumer_key"),
                        consumer_secret=os.environ.get("twitter_consumer_secret"),
                        access_token_key=os.environ.get("twitter_access_token_key"),
                        access_token_secret=os.environ.get("twitter_access_token_secret"))
    
    def find_user_by_screen_name(self, name):
        users = self.api.UsersLookup(screen_name=name)
        for u in users:
            print(f"ID: {u.id} Name: {u.screen_name}")


    def get_user_timeline(self, id):
        statuses = self.api.GetUserTimeline(id)
        print([s.text for s in statuses])

if __name__ == "__main__":
    twitter_conn = TwitterBuddy()
    twitter_conn.find_user_by_screen_name('cybersmithio')
    