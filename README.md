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
for ii in self.message:
            self.message_count[ii] = self.message_count.get(ii, 0) + 1
            #Repeat for alphabet
            for ii in self.alphabet:
                self.alphabet_count[ii] = self.alphabet_count.get(ii, 0) + 1
                #if the length of the alphabets is lower than the 
                #let of the message..No need to proceed..return False
                #Else return True
                for ii, value in self.message_count.items():
                    if self.alphabet_count.get(ii, 0) < value:
                        return False
        return True
```

#### Advantage of algorithm
```bash

1. Time Efficient: Could be time consuming also considering it loops in N
2. Time Coplexity: O(N**2 − N + 1) == O(N**2) 
3. Space complexity: O(1) space efficient.
4. We could decide making it Very fast by treating the different loops
seperate. that would give us a time complexity of O(N) + O(N) = O(N) at the
expense of space complexity.
 
 See Tim Wilson's sort algorithm for further Read https://en.wikipedia.org/wiki/Timsort
 ```
 
 #### DjangoApp for AlphabetSoup
 
 ![Image of Django App](https://github.com/kennedyCzar/AlphabetSoup-Using-Django/blob/master/IMAGES/djangoApp.PNG)
 
........In progress
