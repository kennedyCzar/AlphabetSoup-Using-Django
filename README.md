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

## Algorithm core
```python

self.listA = list(self.message)
self.listB = list(self.alphabet)
self.final = []
self.start_time = time.clock()
while self.listA != []:
    for msg in self.listA:
        if msg in self.listB:
            self.final.append(msg)
            self.listA.remove(msg)
            self.listB.remove(msg)
        elif msg not in self.listB:
            self.listA.remove(msg)
    continue
if sorted(self.final) == sorted(list(self.message)):
    return True, self.final, self.listA, self.listB, time.clock() - self.start_time
else:
    return False, self.final, self.listA, self.listB, time.clock() - self.start_time
```

## Mathematical background

The intuition behind this algorithm is quite straight forward.
1. We have a message input and also an alphabet input
  Our objective is to determine if we can write this message using
  the input alphabets.
  
  What we very much need to check is if the letters in the message are 
  available in the alphabet and if this is true.
  Then we can be sure to conclude mathematically using the following assumptions
    
  Hence if 
  &emsp;_v_ &larr; Alphabet and
  &emsp; _&beta;_ &larr; is message
 
  &emsp;&emsp;&emsp;__if__ _v_ &ge; _&beta;_ __then return__ TRUE and FALSE otherwise  
   Meaning if _v_ is a superset of _&beta;_

2. Then we may assume indeed this word can be formed from alphabets soup.
    This would save us from writing outrageous loops ust to check this.
  


## Advantage of algorithm
```bash

1. Time Efficient: Could be time consuming also considering it loops in N
2. Time Complexity: O(N**2) for Worst Case
3. Space complexity: O(1) space efficient.
4. Running in O(N**2) is bar far not the most efficient but it gets the job don however the inputs come. I had earlier demonstrated 
    how the algorithm can run in O(M) O(N), this however wasnt the best solution as some inputs exhibited strange behaviours.
 
 See Tim Wilson's sort algorithm for further Read https://en.wikipedia.org/wiki/Timsort
 ```
 
 ## DjangoApp for AlphabetSoup
 
 ###### Before input
 ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/djangoApp.PNG)
 
  ###### True Output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/true%20output.PNG)
  ###### False output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/false%20output.PNG)

## Final words
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
