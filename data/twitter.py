import urllib3
import tweepy 
import time 
from tweepy import Stream 
from tweepy.auth import OAuthHandler 
from tweepy.streaming import StreamListener 

ckey='k8yNe1mnTfOOSEbF6E07SlNc8'
csecret='geLfzLAlOBnlx3FD7aJqGlRh4P3zbw7VJSZ421zpDWkBcbrNyI'
atoken='3181521055-gRmzbhV2hIzJoZeI9IcQCYqUsvkLUOyql5QgVyS'
asecret='KH8jpXXCjAvvPmzn1aJwuRlU4Pg43cvBYFCLAPWyPPVsf'

class listener(StreamListener): 
	def on_data(self,data): 
			tweet=data.split(',"text":"')[1].split('","source')[0]
			saveThis=tweet.lower()
			print saveThis
			simpanFile=open('anies20maret2017.csv','a')
			simpanFile.write(saveThis)
			simpanFile.write('\n')
			simpanFile.close()
			return True
	def on_error(self,status): 
		print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["aniesbaswedan"])

