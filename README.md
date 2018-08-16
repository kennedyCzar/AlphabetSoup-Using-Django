# AlphabetSoup-Using-Django
Everyone loves alphabet soup.  And of course, you want to know if you can construct a message from the letters found in your bowl.
```
Task:
```
Write a function that takes as input two strings:
the message you want to write
all the letters found in your bowl of alphabet soup.

```
Assumptions:
```
It may be a very large bowl of soup containing many letters.
There is no guarantee that each letter occurs a similar number of times - indeed some letters might be missing entirely.
The letters are ordered randomly.

The function should determine if you can write your message with the letters found in your bowl of soup. The function should return True or False accordingly.

Try to make your function efficient.  Please use Big-O notation to explain how long it takes your function to run in terms of the length of your message (m) and the number of letters in your bowl of soup (s).

## Solution is Contained inside the Script folder
### How to Use

```bash
git clone https://github.com/kennedyCzar/AlphabetSoup-Using-Django

Unpack the zip file into any dirctory of choice on your local drive.

You can run the script file directly from the testBB.py file.

To use the Django application
------------------------------------------
>conda install django
OR
>pip install django

>Open anaconda propmt
Navigate to the dirctory where you unpacked the zipped file

>Enter into the Djnago project folder
>cd /DJANGO/AlphabetSoup
>dir
(This command checks the file in the AlphabetSoup directory.
Ensure you are in the folder that contains the manage.py file)
then run the command
>python manage.py runserver
(This should start django on the localhost and ip 8000 or 8050
depending on which is open.) OR specify your own ip and port
>python manage.py runserver ip:port
>Enter the ip:port in any browser of choice(preferably chrome)
```

##### Algorithm core
```python

#read all the letters in the message string
for ii in self.message:
    self.message_count[ii] = self.message_count.get(ii, 0) + 1
#Repeat for alphabet
for ii in self.alphabet:
    self.alphabet_count[ii] = self.alphabet_count.get(ii, 0) + 1
    #if the length of the alphabets is lower than the 
    #let of the message..No need to proceed..return False
    #Else return True
return self.compare(self.message_count, self.alphabet_count), time.clock() - self.time

#Compare function
 if sum(self.alphabet_count.values()) > sum(self.message_count.values()):
    self.compare = set(self.message_count).issubset(set(self.alphabet_count))
    if self.compare == True:
      return True
    else:
      return False
  else:
    raise ValueError('message cannot be greater than alphabet')
```

##### Mathematical background

The intuition behind this algorithm is quite straight forward.
1. We have a message input and also an alphabet input
  Our objective is to determine if we can write this message using
  the input alphabets.
  
  What we very much need to check is if the letters in the message are 
  available in the alphabet and if this is true.
  Then we can be sure to conclude mathematically using the following assumptions
  
    &emsp;&emsp;&emsp;__if__ _&beta;_ &le; _&alpha;_
  
2. if \beta \bigsub Alphabets
    Then we may assume indeed this word can be formed from alphabets soup.
    This would save us from writing outrageous loops ust to check this.
  


##### Advantage of algorithm
```bash

1. Time Efficient: Could be time consuming also considering it loops in N
2. Time Complexity: O(M) + O(N) = O(N)--> Worst case :: Linear time
3. Space complexity: O(1) space efficient.
4. Running in O(M * N) is a little time consuming in the order of 4.7exp(-5) but the algorithm runs
in time within 1.2exp(-5) which is quite reasonable. This is a good thing as O(M * N) is computational expensive for deployment.
 
 See Tim Wilson's sort algorithm for further Read https://en.wikipedia.org/wiki/Timsort
 ```
 
 #### DjangoApp for AlphabetSoup
 
 ###### Before input
 ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/djangoApp.PNG)
 
  ###### True Output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/true%20output.PNG)
  ###### False output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/false%20output.PNG)

##### Final words
```

The AlphaSoup algorithm is sort-like algorithm which is capable of telling if a
message can me form from a wordcloud or soup.
In addition to this i have demostrated how you can use 
this in a django application. It would be great to have a database but
is for dmonstration purpose and a database is not required at this point. 
Perhaps you coulc consider a database when hosting and trying to check users.
Again this is license opensource and contributions to improve the algoritm are welcomed.
```


[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/issues)
