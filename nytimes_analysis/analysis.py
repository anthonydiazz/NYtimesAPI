from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re 

import string
import requests

data_stopwords = requests.get("https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt").text

def clean_title(input_string):
    
  dict_stopwords = {}
  for val in data_stopwords.split("\n"):
    dict_stopwords[val.strip()] = 1
 
  output_string = ""
  for word in input_string.lower().split():
    if (word in dict_stopwords):
      continue
    output_string += word + " "
  output_string = output_string.strip()


  output_string = re.sub(f"[{re.escape(string.punctuation)}]", "", output_string)
  return output_string
#this function is cleaning up the text

def top_10(file_name):
  dict = {}
  
  with open(file_name, 'r') as file:
   
    for line in file:    
      cleaned_line = line
      words = cleaned_line
  #here we are looping through each line 
      for word in words: 
  #after that we are looping through each word and if it existed already adding 1 and then if not just 1 
        if word in dict: 
          dict[word] += 1
  
        else:
          dict[word] = 1 
  
  
  return sorted(dict.items(), key=lambda value: value[1], reverse=True)[:10]
#this fucntion is opening the file and then reading it 
#then goiing through each line and counting how many times that word has shown up
def fraction(file_name):
  dict = {}
  
  with open(file_name, 'r') as file:

      for line in file:    
        cleaned_line = clean_title(line)
        words = cleaned_line.split()
        #looping through each line here 

        for word in words: 
#looping through each word here 
          if word in dict: 
            dict[word] += 1

          else:
            dict[word] = 1 


  word_count = 0
  for word in dict:
    word_count += dict[word]

  flu_count = dict['flu'] if 'flu' in dict else 0
  # we are doing the calculations for each of the words 
  death_count = dict['death'] if 'death' in dict else 0
  virus_count = dict['virus'] if 'virus' in dict else 0
  
  return [flu_count / word_count, death_count / word_count, virus_count/ word_count]

#this function is going into the dict, and finding the values that we want to find and then divinding them 

def get_sentiment(file_name):
  analyzer = SentimentIntensityAnalyzer()
  
  compound_sum = 0
  line_count = 0 


  with open(file_name, 'r') as file:

    for line in file:    
      cleaned_line = clean_title(line)
      vs = analyzer.polarity_scores(cleaned_line)
      compound_sum += vs['compound']
     #only looping through lines 
      line_count = 1

  return compound_sum / line_count

#this function is checking the postivty or negativity of each line 
def dollar_count(file_name):
  
  total = 0
  
  pattern = r'\$([\d,]+)'
  #the pattern that we are searching for 
  
  with open(file_name, 'r') as file:

    for line in file:    
      words = line.split()

      for word in words: 
        match = re.search (pattern, word)
        if match:
          value = float(match.group(1).replace(',', ''))

          total += value
  # this function goes in and checks the pattern and then finds the dollar count 
  return total

print("Most frequent words in 1918:")
for frequency in top_10("titles_1918.txt"):
  print(frequency[0], frequency[1])

print('\n\n')

print("Most frequent words in 2020:")
for frequency in top_10("titles_2020.txt"):
  print(frequency[0], frequency[1])

print('\n\n')

print("Fraction of articles in 2020:")
fraction_values = fraction("titles_2020.txt")
print("flu",fraction_values[0])
print("death",fraction_values[1])
print("virus",fraction_values[2])

print('\n\n')

print("Fraction of artilces in 1918:")
fraction_values = fraction("titles_1918.txt")
print("flu",fraction_values[0])
print("death",fraction_values[1])
print("virus",fraction_values[2])


print('\n\n')

print("Dollar Amounts")
formatted_amount = f"2020 ${dollar_count('titles_2020.txt'):,.2f}"
print(formatted_amount)

print('\n\n')

print("Dollar Amounts")
formatted_amount = f"1918 ${dollar_count('titles_1918.txt'):,.2f}"
print(formatted_amount)

print('\n\n')

print("Sentiment 1918")
print(f"The average sentiment of the articles is {get_sentiment('titles_1918.txt')}")

print('\n\n')

print("Sentiment 2020")
print(f"The average sentiment of the articles is {get_sentiment('titles_2020.txt')}")





  





        

    

      
    