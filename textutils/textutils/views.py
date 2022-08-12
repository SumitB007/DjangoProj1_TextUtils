# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #abc = {'name':'Sumit','place':'Pune'}
    return render(request,'index.html')
    # return HttpResponse("<h1>hello</h1>")


#def navigator(request):
#    return HttpResponse('''<h1>Welcome to navigator</h1><br> <a href="https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_band&stacked=h">W3Schools</a>
#    <br><a href="https://codepen.io/SumitB007/pen/eYMzGQP">CodePen</a><br>
#    <a href="https://demo-saas.worksuite.biz/">Worksuite</a><br>
#    <a href="https://studio.youtube.com/channel/UC33wUHTe3GnM5VfiiEuK6ew/analytics/tab-overview/period-default">GamingGroots</a><br>
#    <a href="https://www.codingforentrepreneurs.com/guides/install-python-on-windows/">Python</a>''')
#Code for learning django not related to final website

'''def about(request):
    return HttpResponse("About")

def file_read(request):
    file = open("text_example.txt", "r")
    data = file.read()
    return HttpResponse(data)
    
    #Code for learning django not related to final website
'''

#Laying pipeline
def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #Get checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    lineremover = request.POST.get('lineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    #analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    #Check which box is on
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose' : 'Removed punc', 'analyzed_text': analyzed}
        #Analyze the texts
        #return render(request,'analyze.html',params)
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        # Analyze the texts
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra spaces removed', 'analyzed_text': analyzed}
        # Analyze the texts
        #return render(request, 'analyze.html', params)
        djtext = analyzed


    if (charcounter == "on"):
        analyzed = ""
        i = 0
        for char in djtext:
                i = i+1

        params = {'purpose': 'Character count', 'analyzed_text': i}
        # Analyze the texts
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (lineremover == "on"):
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char !="\r"):
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        # Analyze the texts
        #return render(request, 'analyze.html', params)
        #djtext = analyzed


    if(removepunc !="on" and lineremover != "on" and spaceremover !="on" and fullcaps != "on" and charcounter != "on"):
        return  HttpResponse("Error")


    return render(request, 'analyze.html', params)



#Code for learning django not related to final website
#Laying the  first pipeline
#def removepunc(request):
#    #Get the text
#    djtext = request.GET.get('text','default')
#    print(djtext)
#    #Analyze the texts
#    return HttpResponse("Remove punc")

#def capitalizefirst(request):
#    return HttpResponse("Capitalize First")

#def newlineremove(request):
#    return HttpResponse("New line remove")

#def spaceremove(request):
#    return HttpResponse("Space remove <br> <a href='/'>Back</a>")

#def charcount(request):
#    return HttpResponse("Character count")