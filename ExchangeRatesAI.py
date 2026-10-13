# Import Python's built-in csv module, which provides tools for reading CSV data (this is not your file)
import csv


# Define a class called ExchangeRates that reads the exchange rate file and does the conversions
class ExchangeRates:
    # The constructor runs when we create an ExchangeRates object; it takes the path to the file
    def __init__(self, file_path):
        # Save the file path in the object so other methods can use it
        self.file_path = file_path
        # Read the latest USD/CAD rate from the file and store it (this is CAD per 1 USD)
        self.usd_cad_rate = self._load_latest_rate()

    # Helper method that opens the file and returns the most recent USD/CAD rate
    def _load_latest_rate(self):
        # Open the file for reading (utf-8-sig removes a hidden BOM character at the start if there is one)
        with open(self.file_path, "r", encoding="utf-8-sig", newline="") as file:
            # Read the whole file into one text string
            text = file.read()

        # Split the text into separate lines so we can look at the first line
        lines = text.splitlines()

        # If the first line contains a tab, the file is tab-separated; otherwise assume commas
        delimiter = "\t" if "\t" in lines[0] else ","

        # Use the csv module to split every line into a list of cells using the detected delimiter
        rows = list(csv.reader(lines, delimiter=delimiter))

        # Start with no header row found
        header_index = None
        # Loop through each row along with its position number
        for i, row in enumerate(rows):
            # The real header row starts with "Date" (ignoring capitals and quotes)
            if row and row[0].strip().strip('"').lower() == "date":
                # Remember which row is the header
                header_index = i
                # Stop searching once found
                break

        # If there is no header row, the file isn't in the expected format
        if header_index is None:
            # Stop with a clear error message
            raise ValueError("Could not find the header row (starting with 'Date') in the file.")

        # Get the column names from the header row and remove extra spaces or quotes
        header = [name.strip().strip('"') for name in rows[header_index]]

        # Make sure the USD/CAD column exists in the header
        if "FXAUSDCAD" not in header:
            # Show the column names we did find so the problem is easy to spot
            raise ValueError(f"Could not find the FXAUSDCAD column. Columns found: {header}")

        # Find the position (column number) of the USD/CAD column
        usd_cad_col = header.index("FXAUSDCAD")

        # Go through the data rows from the bottom up so we reach the latest rate first
        for row in reversed(rows[header_index + 1:]):
            # Make sure this row is long enough to contain the USD/CAD column
            if len(row) > usd_cad_col:
                # Get the cell value and remove extra spaces or quotes
                value = row[usd_cad_col].strip().strip('"')
                # Only use this row if the cell is not empty
                if value != "":
                    # Convert the text to a decimal number and return it
                    return float(value)

        # If every USD/CAD cell was empty, there is no usable rate
        raise ValueError("No USD/CAD exchange rate values found in the file.")

    # Method that converts an amount from one currency to another
    def convert(self, amount, from_currency, to_currency):
        # Make both currency codes uppercase and remove spaces so "usd " and "USD" both work
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        # Check that both currencies are supported (only USD or CAD)
        if from_currency not in ("USD", "CAD") or to_currency not in ("USD", "CAD"):
            # Stop with a clear error message if not
            raise ValueError("Currencies must be either USD or CAD.")

        # If both currencies are the same, no conversion is needed
        if from_currency == to_currency:
            # Return the amount unchanged
            return amount

        # Converting USD to CAD: multiply by the rate (the rate is CAD per 1 USD)
        if from_currency == "USD" and to_currency == "CAD":
            # Return the amount in CAD
            return amount * self.usd_cad_rate

        # Otherwise we are converting CAD to USD: divide by the rate
        return amount / self.usd_cad_rate


# Define the main function that handles the user interaction
def main():
    # Path to the exchange rate file on this computer
    file_path = "/Users/tessawang/Documents/FINE 3300/BankOfCanadaExchangeRate.2026.csv"

    # Create an ExchangeRates object, which reads the latest rate from the file
    rates = ExchangeRates(file_path)

    # Show the user which rate is being used
    print(f"Latest USD/CAD exchange rate: {rates.usd_cad_rate}")

    # Keep asking for the amount until the user enters a valid number
    while True:
        # Try to turn the user's input into a decimal number
        try:
            # Ask the user for the amount to convert
            amount = float(input("Enter the amount to convert: "))
            # A valid number was entered, so leave the loop
            break
        # If the input could not be converted to a number, ask again
        except ValueError:
            # Tell the user what went wrong
            print("Please enter a valid number.")

    # Keep asking for the 'from' currency until the user enters USD or CAD
    while True:
        # Ask for the currency to convert from, and standardize it
        from_currency = input("Convert from (USD or CAD): ").strip().upper()
        # Accept only USD or CAD
        if from_currency in ("USD", "CAD"):
            # Valid input, so leave the loop
            break
        # Otherwise explain the problem and ask again
        print("Invalid currency. Please enter USD or CAD.")

    # Keep asking for the 'to' currency until the user enters USD or CAD
    while True:
        # Ask for the currency to convert to, and standardize it
        to_currency = input("Convert to (USD or CAD): ").strip().upper()
        # Accept only USD or CAD
        if to_currency in ("USD", "CAD"):
            # Valid input, so leave the loop
            break
        # Otherwise explain the problem and ask again
        print("Invalid currency. Please enter USD or CAD.")

    # Call the convert method to calculate the converted amount
    result = rates.convert(amount, from_currency, to_currency)

    # Print the original and converted amounts with a $ sign, commas, and 2 decimal places
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


# Run main() only when this file is run directly (not when it is imported by another file)
if __name__ == "__main__":
    main()