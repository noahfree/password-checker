## password_checker.py

The program password_checker.py was created to implement/solve Web Exercise #5 from https://algs4.cs.princeton.edu/34hash/, which is as follows:

Password checker. Write a program that reads in a string from the command line and a dictionary of words from standard input, and checks whether it is a "good" password. Here, assume "good" means that it (i) is at least 8 characters long, (ii) is not a word in the dictionary, (iii) is not a word in the dictionary followed by a digit 0-9 (e.g., hello5), (iv) is not two words separated by a digit (e.g., hello2world)

To run the program, input the command "python3 password_checker.py" in the directory containing the password_checker.py file in addition to both "sgb-words.txt" and "1000-most-common-words.txt", which contain the list of common words to check the password against.

After receiving a potential password from the user, the program performs several operations to check if the password is "good" or not, based on the above criteria. First, it merely checks that the length of the input is greater than or equal to the LENGTH variable defined at the top of the program, which is currently set equal to 8. Next, any 1 digit integer is searched for in the password. Once these are found, we can divide the password into sections to check and see if any words exist in the password.

If there does not exist any integers in the password, then the full password is compared against the dictionary of words in order to see if the input was simply a common word. This is done using hashing in order to expedite the process. A hash value is computed for the password, and then it is compared against the hash value of every word in the list. If any of the hash values match, then False is returned to show that the password is BAD. Otherwise, True is returned.

If there exists one integer in the password and it is at the end of the string, the the password minus the last digit is compared against every word in the dictionary using hashing just like in the previous step. If the hash value matches any of the words, False is returned to show that the password is BAD. Otherwise, True is returned. If the one digit integer is not found at the end of the password, then everything before the digit and everything after the digit are each compared to every word in the word list, using hash value like in the previous two steps. If both of the hash values find matches in the word list, then False is returned to show that the password is BAD because it contains two common words separated by an integer. Otherwise, True is returned.

If there exists two integers in the password, True is returned to show that the password is GOOD by the given criteria.

Finally, the user is asked if they would like to run the program again, which they must input 'Y' or 'y' to input another password.
