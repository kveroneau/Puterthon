from browser import window, document

puter = window.puter

AppDiv = document.getElementById('pyapp')

def evalFile(data):
    document.getElementById('code').innerHTML=''
    data.text().then(exec)

def openFile(f):
    f.read().then(evalFile)

def RunScript():
    puter.ui.showOpenFilePicker().then(openFile)

def HideConsole():
    document.getElementById('code').hidden=True
    document.getElementById('docs').hidden=True

def DownloadApp(AppName):
    f=open('Apps/'+AppName+'.py')
    puter.ui.showSaveFilePicker(f.read(), AppName+'.py')
