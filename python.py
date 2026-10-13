amount = float(input ("Hello, I am an exchange rate calulcator! What $ amount would you like to convert? "))
print(amount)
#asks the user what anount and converts text to float (so python can calulcate amount)

from_currency = input ("What currency are you converting from (USD or CAD)? ")
print(from_currency)

to_currency = input ("What currency are you converting to (USD or CAD)? ")
print(to_currency)

file_name = "/Users/tessawang/Documents/FINE 3300/BankOfCanadaExchangeRate.2026.csv"
#variable called file_name storing the location of the csv

class ExchangeRates:
    def __init__(self, filename):
    #constructor, ie initializes the new object

        f = open(filename, "r")
        #opens and reads the file 

        data = f.read()
        #returns contents of file in single string

        rows = data.split("\n")
        #split into rows

        rows = [row.split(",") for row in rows]
        #go through each row, split/divide wherever you see a comma (because it's a csv file), and [] means make a list out of it

        if rows and rows[-1] == [""]:
            rows.pop()  
        #removes final row because it was empty

        column = rows[0].index("FXAUSDCAD")
        #finds the column with the header FXAUSDCAD based on row 0 

        f.close()
        #closes file
        
        self.__exchange_rate = float(rows[-1][column])
        #saves exchange rate

    def exchange_rate(self):
        return self.__exchange_rate 
    #creating a method called exchange rate to return value (1.3978)  

    def convert(self, amount, from_currency, to_currency):
            if from_currency == "USD" and to_currency == "CAD":
                return amount * self.__exchange_rate
            elif from_currency == "CAD" and to_currency == "USD":
                return amount / self.__exchange_rate
    #this part converts the amount using if and elif statements

rates = ExchangeRates(file_name)
#creates an object from the class above 

print(f"your amount would be equal to ${rates.convert(amount, from_currency, to_currency,):.2f} {to_currency}")
#prints the converted amount. Using an f-string so python can insert the values for amount and to currency


