## Performance Test | BubbleSort & Quicksort

Compare perfomance:
    
    Qksort.quicksort([3, 6, 8, 2, 4])
    Out[69]: 1.9753092601604294e-06
    
     bubblesort([3, 6, 8, 2, 4]).bubblesort()
     Out[96]: ([2, 3, 4, 6, 8], 'Running time 9.086423688131617e-06secs') 
     
     message = 'UVZQDEQ'
     alphabet = 'RBWGHGDT'      
     ASOUP = AlphabetSoup(message, alphabet)
     ASOUP.Alphabet()
     Out[51]: (False, ['D'], [], ['R', 'B', 'W', 'G', 'H', 'G', 'T'], 1.1061732948292047e-05)
   
Conclusion:

      Shows from the output that QuickSort is almost
      9X faster than bubblesort. Meaning Bubblesort took 
      9X the time to sort the numbers.
      So for deployment you could employ divide and conquer 
      in design of your algorithm.
