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

You may write the function in any programming language you prefer - but please consider the language required by the position for which you are applying.


In case that you need more time or you have some questions, please, feel free to contact me.  

## Solution is Contained inside the Script folder
### How to Use

```bash
git clone https://github.com/kennedyCzar/AlphabetSoup-Using-Django
```

##### algorithm core
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
```bash
Advantage of algorithm

1. Time Efficient: Could be time consuming also considering it loops in N
2. Time Coplexity: O(N**2 − N + 1) == O(N**2) Linear time
3. Space complexity: O(1) space efficient.
4. We could decide making it VEry fast by teating the different loops
seperate. that would give us a time complexity of O(N) + O(N) = O(N) at the
expense of space complexity.
 
 See Tim Wilson's sort algorithm for further Read https://en.wikipedia.org/wiki/Timsort
 ```
 
 
........In progress
