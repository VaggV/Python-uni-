#python 2.7.15
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
api = tweepy.API(auth)

#zhtaei to onoma toy twitter gia ton 1o logariasmo
user1 = raw_input("Dwste to prwto onoma logariasmou twitter:")

#dhmiourgei kenh lista
tweeList1 = ""
for status in tweepy.Cursor(api.user_timeline, screen_name=user1, tweet_mode='extended').items(10):
    #prosthetei kathe fora sth lista ta tweet
    tweeList1 = tweeList1 + status.full_text + " "

#xwrizei tis lekseis sth lista
words1 = tweeList1.split()
#apothikevw se metavliti to noumero twn list item dhladh to noumero twn leksewn
lekseis1 = len(words1)

#pairnei ta stoixeia tou xrhsth apo to api
item1 = auth_api.get_user(user1)
#apothikevw se metavliti to noumero twn followers tou xrhsth
followers1 = str(item1.followers_count)

#ypologizw to ginomeno twn followers me to plithos twn leksewn
ginomeno1 = int(lekseis1)*int(followers1)
print "To ginomeno tou xrhsth 1:", ginomeno1


#apo dw kai katw h idia diadikasia me panw gia ton 2o user pou tha dwsei o xrhsths
user2 = raw_input("Dwste to deutero onoma logariasmou sto twitter:")

tweeList2 = ""
for status in tweepy.Cursor(api.user_timeline, screen_name=user2, tweet_mode='extended').items(10):
    tweeList2 = tweeList2 + status.full_text + " "

words2 = tweeList2.split()
lekseis2 = len(words2)

item2 = auth_api.get_user(user2)
followers2 = str(item2.followers_count)

ginomeno2 = int(lekseis2)*int(followers2)
print "to ginomeno tou xrhsth 2:", ginomeno2
#Telos gia ton 2o user

#sugkrish twn ginomenwn
if ginomeno1 > ginomeno2:
    print "o xrhsths", user1,"exei megalytero ginomeno"
elif ginomeno2 > ginomeno1:
    print "o xrhsths",user2,"exei megalytero ginomeno"
else:
    print"ta ginomena einai isa"
