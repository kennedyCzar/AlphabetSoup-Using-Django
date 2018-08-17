# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:00:37 2018

@author: kennedy

"""

'''
AlphabetSoup algorithm
--------------------------
Algorithm sorts a dictionary of words compares
them and return a boolean if a word 'message'
can be formed from alphabet 'wordsoup'
Time Cmomplexity: O(M*N) --> Worst case
Space complexity: O(1)

'''

class AlphabetSoup(object):
    def __init__(self, message, alphabet):
        '''Arguments:
            @self: class construct
            @message: message we want to check if constructable
            @alphabet: alphabet of words from which 
                        message is formed.
                        If True: Function returns True
                        Else: Function returns False
        '''
        self.message = message
        self.alphabet = alphabet
#        #Check for None
#        if self.message is None and self.alphabet is None:
#            if self.message is None and self.alphabet is not None:
#                if self.message is not None and self.alphabet is None:
#                    return None
    
        
    def is_empty(self, structure):
        '''
        Arguments:
            @Structure:
                @Dictionary check: Checks if dictionary is empty
                @list check: Checks if list is empty
                @string check: Checks if String is empty
                @tuple ckeck: Checks if tuple is empty
            @Return type:
                @True: If Structure is not empty
                @False: if struture is empty
        '''
        self.structure = structure
        
        if not self.structure:
            return True
        else:
            return False
    
      
    def Alphabet(self):
        '''
        Argument:
            @Self: calls own self
        Return type:
            @True: if conditions are met
            @Fasle: Otherwise
        '''
        
#        character = self.character
        
        #Exception to handle Unprecedented errors
        try:
            '''
            If Alphabet and message are both empty
            then we return None type 
            Otherwise we return the UPPERCASE of both
            message and alphabet and remove the whitespace between them
            '''
            if self.is_empty(self.message) and self.is_empty(self.alphabet):
                return None
            elif self.is_empty(self.message) or self.is_empty(self.alphabet):
                return None
            elif self.is_empty(self.message) and not self.is_empty(self.alphabet):
                return None
            elif not self.is_empty(self.message) and self.is_empty(self.alphabet):
                return None
            else:
                self.message = self.message.upper().replace(" ", "")
                self.alphabet = self.alphabet.upper().replace(" ", "")
        except Exception as e:
            raise(e)
        finally:
            pass
        
        import time
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
            return True
        else:
            return False
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
