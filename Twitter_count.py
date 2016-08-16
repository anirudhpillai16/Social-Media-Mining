# What if we wanted to know the percentages of positive and negative words to the overall words (tokens) in a file.
# Let's write some code to do that based on the positive and negative entries we acquired from SentiWordNet:
import re

def clean_lexicon(lex_input):
    lex_file_l=open(lex_input, "r").readlines()
    
    new_lex_file_l=[]
    for i in lex_file_l:
        i=i.strip()
        #i= i[:-1] # i is a word in the list
        i= re.sub("_", " ", i)
        new_lex_file_l.append(i)
    return new_lex_file_l

# Change the path to your local path:
pos_lex= clean_lexicon("C:/Courses/SMM/pos.wn.txt")
neg_lex= clean_lexicon("C:/Courses/SMM/neg.wn.txt")


# Determine the percentage of positive words in a file:
def get_sentiment_diversity(pos_lex, neg_lex, input_file):
    '''
    just returns some stats about % of pos and neg sentiment in a file...
    '''
    input_string=open(input_file, "r").read().lower()
    len_words= float(len(input_string.split()))
    pos_count=0
    neg_count=0
    for w in pos_lex:
        pos_count+= input_string.count(w)
    for w in neg_lex:
        neg_count += input_string.count(w)
    return pos_count, neg_count, len_words
   
# Call the function...
input_file="C:/Courses/SMM/new.txt"
pos_count, neg_count, len_words= get_sentiment_diversity(pos_lex, neg_lex, input_file)
#-------------------------
print "% of positive: ", round(pos_count/len_words, 4) 
print "% of negative: ", round(neg_count/len_words, 4)
