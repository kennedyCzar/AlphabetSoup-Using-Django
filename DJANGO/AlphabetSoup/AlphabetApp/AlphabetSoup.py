# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:00:37 2018

@author: kennedy
"""

class AlphabetSoup(object):
    def __init__(self, message, alphabet):
        '''Arguments:
            @self: class construct
            @message: message we want to check if constructable
            @alphabet: alphabest of words from which 
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
        self.message_count = {}
        self.alphabet_count = {}
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
        
        #read all the letters in the message string
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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    