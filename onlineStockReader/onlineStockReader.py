import bs4 as bs        #   Beautiful Soup, for extracting from web
import urllib.request   #   For handling URLs
import re               #   For regex and compile function
import time             #   For refresh timer

class Stock:
    def __init__(self, symbol = 'symbol'):
        self.companyName    = 'companyName'
        self.lastValue      = 9999.99
        self.change         = 0
        self.symbol         = symbol
        self.url            = 'about:blank'
        self.pol            = '+'

class StockList:
    def __init__(self):
        self.List = {}

    def addSym(self):
        symToAdd            = input('Enter new stock symbol, ' +
                                    'or comma seperated list: ')
        symToAddClean       = symToAdd.replace(' ', '').split(',')
        for sym in symToAddClean:
            self.List[sym] = Stock(sym)
            importWebInfo(sym)
        
    def subSym(self):
        symToRem = input('Enter stock symbol, ' +
                         'or comma seperated list of symbols, to remove: ')
        symToRemClean       = symToRem.replace(' ', '').split(',')
        for sym in symToRemClean:
            del self.List[symToRemClean]

def menu():
    choice = int(0)
    while not choice == 4:
        print('1. Add symbol')
        print('2. Rem symbol')
        print('3. See stocks')
        print('4. Quit')
        print()
        try:
            choice = int(input('  enter choice: '))
            menuChoiceHandler(choice)
        except ValueError:
            print('Please enter a valid menu choice by number.\n')

def menuChoiceHandler(choice):
    if int(choice) == 1:
        stocks.addSym()
    elif int(choice) == 2:
        stocks.subSym()
    elif int(choice) == 3:
        updateStocks(stocks)

def importWebInfo(symToAdd):
    url             = 'https://www.marketwatch.com/investing/stock/' + symToAdd
    page            = urllib.request.urlopen(url)
    soup            = bs.BeautifulSoup(page, 'html.parser')
    name            = soup.find_all('h1', attrs={'class':'company__name'})
    companyName     = name[0].string

    #   Supposing success, add the company to the list   
    stocks.List[symToAdd].companyName = companyName
    stocks.List[symToAdd].url = url

    #   Print a reassuring confirmation
    print(stocks.List[symToAdd].companyName + ' added.\n')
    return

def updateStocks(stocks, refreshRate = 5):
    #   Currently this is using a try loop with a keyboard interrupt
    #   exception so that the user can stop the auto-refresh and return
    #   to the main menu. It's clumsy and I don't like it.
    try:
        while True:
            for stock in stocks.List:

                #   To adjust the refresh rate to default or user choice
                #   we need to measure response times.
                responseTimeBegin = time.time()
                
                page    = urllib.request.urlopen(stocks.List[stock].url)
                soup    = bs.BeautifulSoup(page, 'html.parser')
                
                quotes = soup.find_all('bg-quote', attrs={'field':'Last'})
                changes = soup.find_all('span',
                                        attrs={'class':'change--point--q'})

                stocks.List[stock].lastValue = quotes[0].string
                stocks.List[stock].change = changes[0].string

                #   If the stock is up, we'll print a + sign next to the
                #   change. If the stock is down, a neg sign will already
                #   be prepended by the website.
                if float(stocks.List[stock].change) > 0:
                    stocks.List[stock].pol = '+'
                else:
                    stocks.List[stock].pol = ''

                #   end timer
                responseTimeEnd = time.time()

            for stock in stocks.List:
                print(stocks.List[stock].companyName + ': $' +
                      stocks.List[stock].lastValue + '(' +
                      stocks.List[stock].pol +
                      stocks.List[stock].change + ')')
            print()
            print('ctrl-c to stop, wait for refresh.')

            responseTime = responseTimeEnd - responseTimeBegin
            refreshRateDelta = responseTime * len(stocks.List)

            #   default refresh is every 5s. This can be changed.
            #   The following will adjust the time for the time
            #   it takes to read from the web.
            if refreshRate > refreshRateDelta and refreshRate-refreshRateDelta > 0:
                time.sleep(refreshRate-refreshRateDelta)
            
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    stocks = StockList()
    menu()
