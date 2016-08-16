library(twitteR)
library(tm)
library(wordcloud)
library(plyr)
consumer_key<-'JHczjcfqumdkctsVtvKUuHIC2'
consumer_secret<-'juaRhKDZ9vdBAq0kRgtSMqa3yYtY7JMddyXhLOJclr9HohOzLl'
access_token<- '79117612-Km3xflBVmZI9Utgqd4FtQHSt7CaOIbqqp0juGJ3lc'
access_secret<- '6gJOXcPmZk6c4qclgDgavPDS080JNIgFn7exFujR097Lc'

setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
srk_tweets<- searchTwitter("Shahrukh Khan+ Fan",n=1000,lang = "en",resultType = "recent")
srk_tweets
tweets.txt= lapply(srk_tweets,function(t)t$getText())
pos= scan('C:/Courses/SMM/Positive.txt',what = 'character',comment.char=';')
neg= scan('C:/Courses/SMM/Negative.txt',what = 'character',comment.char=';')
source('C:/Courses/SMM/sentiment.R')
analysis= score.sentiment(tweets.txt, pos.words, neg.words)
table(analysis$score)

