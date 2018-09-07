# AlphabetSoup-Using-Django [![Hosted Live](https://img.shields.io/badge/Hosted-Live-brightgreen.svg?style=flat)](https://alphabetsoup.herokuapp.com/)
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

The function should determine if you can write your message with the letters found in your bowl of soup. 
The function should return True or False accordingly.

Try to make your function efficient.  Please use Big-O notation to explain how long it takes your function to
run in terms of the length of your message (m) and the number of letters in your bowl of soup (s).

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
1. We convert our message into a list for we we wan easily iterate
2. Do the same for the alphabet soup and ensure they are structured

We then create a while loop for which:
    if A <-- Alphabet & B is message
        we iterate over the range of B
            then we do same for A
                if the element of B can be found in A
                    Then we can form a message using this
                 we repeat this process and
                    store the content in another list we call final
      finally we ckeck the final list with the message list
        if this condition satisfies
            the we return a boolean True otherwise
                we return a False
  
  
#### Major Assumption towards solution
```
This Algorithm is pretty fast in concluding this a message can be formed from an Alphabet soup. This is 
simply because we did not loop over the entire Alphabet soup but rather, over the letters.

This cuts the execution time but half assuming we have thousand of words in the soup against very shourt message.
```

## Advantage of algorithm
```bash

1. Time Efficient: Extremely fast even while it runs in N.thanks to while loop
2. Time Complexity: O(N*logN)
3. Space complexity: O(1) space efficient.
4. Running in O(N*logN) is by far the most efficient and it gets the job done
    for message length less than 10. ie N < 10. for N > 10 the algorithm runs 
    in O(N**2). I had earlier demonstrated how the algorithm can run in O(N).
    Improving the algorithm would mean employing the rules of divide and conquer.
    But this would be at the expense of space complexity. Hence, we conclude it is
    time efficient in O(N*logN).
    
    Contributions are accepted to improve algorithms 
    to make it run in O(N) if possible.
 
 See Tim Wilson's sort algorithm for further Read https://en.wikipedia.org/wiki/Timsort
 ```
 
 ## DjangoApp for AlphabetSoup
 
 ###### Before input
 ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/djangoApp.PNG)
 
  ###### True Output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/true%20output.PNG)
  ###### False output
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/false%20output.PNG)

Or Just Download the EXE Zipped folder and extract the .EXE file. Run program and Voila.
  ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/TKinter%20App.PNG)
## Final words
```

The AlphaSoup algorithm is sort-like algorithm which is capable of telling if a
message can me form from a wordcloud or soup.
In addition to this i have demostrated how you can use 
this in a django application. It would be great to have a database but
is for dmonstration purpose and a database is not required at this point. 
Perhaps you could consider a database when hosting and trying to check users.
Again this is license opensource and contributions to improve the algoritm are welcomed.
```


[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/issues)
