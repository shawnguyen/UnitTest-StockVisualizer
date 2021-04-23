####################################################################################################
#Imported datetime for checking format for startDate and endDate                                   #
####################################################################################################

import unittest
import datetime

def stockSymbol(stockInput):
    hasLowercase = any(map(str.islower, stockInput))
    hasNumber = any(map(str.isdigit, stockInput))
    lessThan1Char = len(stockInput) < 1
    moreThan7Char = len(stockInput) > 7

    if hasLowercase == True:
        raise ValueError("Invaild: Stock symbols cannot contain lowercase(s).")
    elif hasNumber == True:
        raise ValueError("Invaild: Stock symbols cannot contain number(s).")
    elif lessThan1Char | moreThan7Char == True:
        raise ValueError("Invaild: Stock symbol does not meet the character requirements. Must be 1-7 characters.")        
    return stockInput

def chartType(chartInput):
    return chartInput

def timeSeries(timeInput):
    if timeInput not in range(1,5):
        raise ValueError("Invaild: Time Series is not 1, 2, 3, or 4.")
    return timeInput

def startDate(startInput):
    try:
        datetime.datetime.strptime(startInput, "%Y-%m-%d")
    except ValueError:
        print("Invaild: Start date format incorrect. Format should be YYYY-MM-DD")

    hasLetters = any(map(str.isalpha, startInput))

    if hasLetters == True:
        raise ValueError("Invaild: Start date cannot contain letter(s).")
    return startInput

def endDate(endInput):
    try:
        datetime.datetime.strptime(endInput, "%Y-%m-%d")
    except ValueError:
        print("Invaild: End date format incorrect. Format should be YYYY-MM-DD")

    hasLetters = any(map(str.isalpha, endInput))

    if hasLetters == True:
        raise ValueError("Invaild: End date cannot contain letter(s).")
    return endInput

#Unit Testing
class TestDataVisualizer(unittest.TestCase):
    def test_stockSymbol(self):
        #Working test
        stockSymbol("AMD")

        #Will cause lowercase error
        #stockSymbol("AMd")

        #Will cause number error
        #stockSymbol("AMD1")

        #Will cause character requirement error
        #stockSymbol("")

        #Will cause character requirement error
        #stockSymbol("AMDAMDAMD")

    def test_chartType(self):
        barChart = 1
        lineChart = 2

        #Working test
        self.assertEqual(chartType(1), barChart)
        self.assertEqual(chartType(2), lineChart)

        #Failing test
        #self.assertEqual(chartType(3), barChart)
        #self.assertEqual(chartType(4), lineChart)

    def test_timeSeries(self):
        #Working test
        timeSeries(1)

        #Working test
        timeSeries(2)

        #Working test
        timeSeries(3)

        #Working test
        timeSeries(4)

        #Failing test
        #timeSeries(5)

    def test_startDate(self):
        #Working test
        startDate("2020-12-01")

        #Failing test
        #startDate("2020-mm-dd")

    def test_endDate(self):
        #Working test
        endDate("2020-12-30")

        #Failing test
        #endDate("2020-mm-dd")

if __name__ == '__main__':
    unittest.main()
