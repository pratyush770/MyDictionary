import re
from django.shortcuts import render
import requests
import bs4

# Create your views here.

def index(request):
    return render(request,'base.html')

def search(request):
    word = request.GET['word']
    res= requests.get('https://www.dictionary.com/browse/'+word)
    res2= requests.get('https://www.thesaurus.com/browse/'+word)
    if res:
        soup=bs4.BeautifulSoup(res.text, 'lxml')
        meaning=soup.find_all('div', {'value': '1'})
        meaning1=meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' is not found in the database'
        meaning = ''
        meaning1 = ''
    if res2:
        soup2=bs4.BeautifulSoup(res2.text, 'lxml')
        synonyms=soup2.find_all('a', {'class':'css-1kg1yv8 eh475bn0'})
        ss=[]
        for b in synonyms[0:20]:
            re=b.text.strip()
            ss.append(re)
        se=ss
        antonyms=soup2.find_all('a', {'class':'css-15bafsg eh475bn0'})
        aa=[]
        for c in antonyms[0:20]:
            r=c.text.strip()
            aa.append(r)
        ae=aa
    else:
        se=''
        ae=''
    results={
        'word':word,
        'meaning':meaning1,
    }
    return render(request,'search.html', {'se': se, 'ae': ae, 'results': results})
