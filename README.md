# Encrypting_message

This is just a simple encryption algorithm, but it doesn't take any key element to encrypt. The index value of a character acts as a key element. let me tell you an example: Testcase 1: msg="hello world" Explanation: index of 'h' is 0,so we add nothing to the ascii value of 'h index of 'e' is 1,so we add 1 to the ascii value of 'e' i.e., 'f' index of 'l' is 2,so we add 2 to the ascii value of 'l' i.e., 'n' In order to decrease the large numbers,we apply mod 26(number of alphabets).
