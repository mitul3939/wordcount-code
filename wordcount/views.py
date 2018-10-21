from django.http import HttpResponse
from django.shortcuts import render 
def homepage(request):
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>EGGS</h1>')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    count1=0
    for word in wordlist:
        for c in word:
            count1+=1
        avgnum=count1/len(wordlist)
    count2=0
    for word in wordlist:
        for c in word:
            count2+=1
        repeated_word=wordlist.count("is")
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'avgnum':avgnum,'repeated_word':len(repeated_word)})

