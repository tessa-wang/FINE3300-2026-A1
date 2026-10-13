# FINE3300-2026-A1
### Description
- FINE 3300, Fall Semester 2026, Assignment 1
- Created an exchange rate calculator (python.py) and compared it with a vibe coded version (ExchangeRatesAI.py)
### Tessa Wang's Write-Up


**(a) provide the link to your GitHub repository.**

https://github.com/tessa-wang/FINE3300-2026-A1.git

**(b) paste the output from your program for $100,000 USD to CAD, and vice versa.**

$100,000 USD to CAD output:  Your amount would be equal to $139,780.00 CAD

$100,000 CAD to USD output:  Your amount would be equal to $71,540.99 USD

**(c) list the LLM model that you used for part 2 along with all the prompts given to the LLM model.**

I prompted Claude Sonnet 5.5 with the following: 

“I’ve downloaded the csv file and the path is: /Users/tessawang/Documents/FINE 3300/BankOfCanadaExchangeRate.2026.csv

I’ve also created a file in VS code called ExchangeRatesAI.py.
I need you to follow part 2 of the instructions below and give me code that I can directly paste into the ExchangeRatesAI.py. file

Also use comments in the code (#) to describe each line of code so I understand what you are doing.

Part 1: Exchange Rates Download the BankOfCanadaExchangeRates.2026.csv file from Canvas. Open and view the structure of the file. Notice that the last row of data consists the latest exchange rate. While there are many currency pairs listed, the one that is of interest to us is the USD/CAD. Design a class (call it ExchangeRates) that takes an exchange rate file. Write a method/function (call it convert) that takes the amount and two currencies (USD or CAD) and converts from one currency to another using the exchange rate read from the file. You must prompt the user to specify the amount, the ’from’ & ’to’ currency, i.e. USD or CAD. Note: . 

Part 2: Vibe Coding Vibe Coding is where you use a Large Language Model (LLM) to write code for you. You specify the prompt to the model and focus on high level requirements while the language model focuses on the actual technical implementation. Use any AI model of your choice and have it do part 1 of the assignment. Do not provide the model with your code. Create a separate python file (name it ExchangeRatesAI.py) and test it within your Visual Studio Code environment. If the results are not correct, repeat the directions to the AI model until you have it produce the correct output. Compare the code that you created with the code that the AI model generated. Write a paragraph comparing the code and stating the exact model that you used along with the prompts that you provided.” 

“There was an error message: ValueError: Could not find a USD/CAD column in the file. Rewrite and the header is (FXAUSDCAD).”

**(d) include the comparison of your code and the LLM code.**

My code and the LLM code differed in many ways. The model I used was Claude Sonnet 5.5. The major differences I noticed were the type of functions being called and the amount of if else statements used. I didn’t account for the possibility that the user would input something my code couldn’t understand, so I didn’t have if statements that would say something along the lines of “invalid, please try again.” This is something the LLM did, using while loops, try and except, and break.

The LLM also read the file differently. I used open, read, and split to turn the file into a list of rows, while the LLM used Python’s csv module and searched for the header row by name. It also skipped empty cells instead of just reading the last row like mine did. I also recognized that the LLM wrote its variables as self.file_path = file_path instead of the way we learned in class – which would have been self.__file_path = file_path. Another difference is that the LLM had a main() function which was for the user’s inputs, whereas I asked for the input at the top of my file. 

Overall, it was beneficial to compare my code with the LLM’s, as it taught me the importance of accounting for situations where the user’s input may not perfectly match what the code needs.
