'''
Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

Your Input and output should look something like this

Input : Please enter a string Mississippi

Output : i = 04 s = 04 p =02 m =01
'''


input= print(str("Enter your string: "))

d = dict()
for key in input:
  d[key] = d.get(key, 0) + 1
  return d
 
 

def most_frequent(string):
   
    frequency_list = [(freq, letter) for (letter, freq) in most_frequent.iteritems()]
    frequency_list.sort(reverse=True)
    return [letter for freq, letter in frequency_list]



print (most_frequent(input))
