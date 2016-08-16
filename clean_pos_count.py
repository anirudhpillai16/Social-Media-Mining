import re
import string
punc = [char for char in string.punctuation]

def clean(to_filter_list, text):
    '''
    input: 
        a. list of undesirable items we want to remove from text
        b. text we want to clean
    output:
        cleaned text
    '''
    for i in to_filter_list:
        #print i
        i="\\"+i
        text=re.sub(i, "", text)
    return text


def clean_lexicon(lex_input):
    lex_file_l=open(lex_input, "r").readlines()
    
    new_lex_file_l=[]
    for i in lex_file_l:
        i=i.strip()
        #i= i[:-1] # i is a word in the list
        i= re.sub("_", " ", i)
        new_lex_file_l.append(i)
    return new_lex_file_l


# Determine the percentage of positive words in a file:
def get_sentiment_diversity(pos_lex, neg_lex, input_file):
    '''
    just returns some stats about % of pos and neg sentiment in a file...
    '''
    input_string=open(input_file, "r").read().lower()
    input_string= clean(punc, input_string)
    len_words= float(len(input_string.split()))
    pos_count=0
    neg_count=0
    for w in pos_lex:
        pos_count+= input_string.count(w)
    for w in neg_lex:
        neg_count += input_string.count(w)
    return pos_count, neg_count, len_words
   
def main():
    # Call the code...
    #------------------
    print("Welcome to the sentiment statistician!!")
    # Get the lexicon:
    pos_lex= clean_lexicon("C:/Courses/SMM/pos.wn.txt")
    neg_lex= clean_lexicon("C:/Courses/SMM/neg.wn.txt")
    # Read the hamlet file
    input_file="C:/Courses/SMM/new.txt"
    # get sentiment stats
    pos_count, neg_count, len_words= get_sentiment_diversity(pos_lex, neg_lex, input_file)
    #-------------------------
    print "% of positive: ", round(pos_count/len_words, 4) 
    print "% of negative: ", round(neg_count/len_words, 4)

    
if __name__ == "__main__":
    main()