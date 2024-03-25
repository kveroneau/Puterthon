from puter import puter

def readFile(data):
    data.text().then(print)

def openFile(f):
    f.read().then(readFile)

def open():
    puter.ui.showOpenFilePicker().then(openFile)

def main():
    print('Thank you for importing these Puter Tests!')
    print('First choose a file:')
    open()

main()
