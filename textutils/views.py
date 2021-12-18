# File created by Maham
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
import string
import re


def index(request):
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("about")

def about(request):
    return render(request, 'about.html')  

def contact(request):
    return render(request, 'contact.html')

def changecase(request):
    return render(request, 'changecase.html')

def sorting(request):
    return render(request, 'sorting.html')

def regex(request):
    return render(request, 'regex.html')

def wordsorting(request):
    return render(request, 'wordsorting.html')

def numbersorting(request):
    return render(request, 'numbersorting.html')

def emailextrator(request):
    return render(request, 'emailextrator.html')

def phonenumextrator(request):
    return render(request, 'phonenumextrator.html')

def termsandcondition(request):
    return render(request, 'termsandcondition.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')

def websitedetail(request):
    return render(request, 'websitedetail.html')

def features(request):
    return render(request, 'features.html')

def extraspaceremover(request):
    return render(request, 'extraspaceremover.html')

def newlineremover(request):
    return render(request, 'newlineremover.html')

def removepunctuations(request):
    return render(request, 'removepunctuations.html')

def counter(request):
    return render(request, 'counter.html')    

def analyze(request):
    djano_text=(request.POST.get('text','default'))
    #case changes
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    capitalize=request.POST.get('capitalize', 'off')
    camel_case=request.POST.get('camel_case', 'off')

    #Word Sorting 
    words_asc_order= request.POST.get('words_asc_order', 'off')
    words_dsc_order= request.POST.get('words_dsc_order', 'off')

    #Number Sorting
    numbers_asc_order= request.POST.get('numbers_asc_order', 'off')
    numbers_dsc_order= request.POST.get('numbers_dsc_order', 'off')
    
    #Regex Email Extrator
    email_extrator= request.POST.get('email_extrator', 'off')

    #Remove Punctuations
    remove_punctuations = request.POST.get('remove_punctuations', 'off')

    #New Line Remover
    new_line_remover = request.POST.get('new_line_remover', 'off')

    #Extra Space Remover
    extra_space_remover = request.POST.get('remove_punctuations', 'off')

    #Number Counter
    counter =  request.POST.get('counter', 'off')

     
    

    #-------------------------------------------------------------------------------------------------------------------
                                                     #Case Changes
    #-------------------------------------------------------------------------------------------------------------------                                          
    if uppercase=="on" and lowercase=="off" and capitalize=="off" and camel_case=="off":
        analyze=""
        for char in djano_text:
            analyze=analyze+char.upper()
        parameters = {'purpose': 'Change To Uppercase', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)
    
    # lowercase
    elif lowercase=="on" and uppercase=="off"  and capitalize=="off" and camel_case=="off":
        analyze=""
        analyze=djano_text.lower()
        parameters={'purpose':'Convert into lowercase','analyzed_text':analyze}
        return render(request,'analyze.html',parameters)

    elif capitalize=="on" and lowercase=="off" and uppercase=="off"  and camel_case=="off":
        analyze=""
        analyze=djano_text.capitalize()
        parameters={'purpose':'Convert into capitalize','analyzed_text':analyze}
        return render(request,'analyze.html',parameters)
        

    elif camel_case=="on" and lowercase=="off" and uppercase=="off"  and capitalize=="off":
        analyze=""
        analyze_case=""
        for char in djano_text:
            analyze_case=analyze_case+char
            temp=analyze_case.split(" ")
            analyze=temp[0] + ''.join(ele.title() for ele in temp[1:]) 
        parameters = {'purpose': 'Change To Uppercase', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)
    
    elif uppercase=="on" or lowercase=="on" or capitalize=="on" or camel_case=="on":
        analyze=""
        parameters = {'purpose': 'ERROR', 'analyzed_text': 'Error! Kindly, select any one option'}
        return render(request, 'analyze.html', parameters)
    
    #--------------------------------------------------------------------------------------------------------------------
                                                  #WORD SORTING
    #--------------------------------------------------------------------------------------------------------------------
    if words_asc_order =="on" and  words_dsc_order=="on":
        analyze_text=[]
        parameters = {'purpose': 'Change To Uppercase', 'analyzed_text': 'Error! Kindly, select any one option'}
        return render(request, 'analyze.html', parameters)

    elif words_asc_order=="on":
        analyze_text=list(djano_text.replace(' ', '\n').split())
        analyze_text.sort()
        analyze='\n'.join([str(elem) for elem in analyze_text ])
        parameters = {'purpose': 'Sort words as Ascending order', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)

        # re.split('; |, |\*|\n',analyze_new)
        # analyze_text=[]
        # analyze_text=list(djano_text.split("\n"))
        # analyze_text.sort()
        # analyze=' '.join([str(elem) for elem in analyze_text ])
        # parameters = {'purpose': 'Sort words as Ascending order', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', parameters)

        # analyze_text=[]
        # analyze_text=list(djano_text.split("\n"))
        # analyze_text.sort()
        # analyze=' '.join([str(elem) for elem in analyze_text ])
        # parameters = {'purpose': 'Sort words as Ascending order', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', parameters)

    # letter_dsc_order
    elif words_dsc_order=="on":
        analyze_text=list(djano_text.replace(' ', '\n').replace(',', ' ').split())
        analyze_text.sort()
        analyze_text.sort(reverse=True)
        analyze=' '.join([str(elem) for elem in analyze_text ])
        parameters = {'purpose': 'Sort words as Descending order', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)
    
    #--------------------------------------------------------------------------------------------------------------------
                                                  #NUMBERS SORTING
    #--------------------------------------------------------------------------------------------------------------------

    if numbers_asc_order  =="on" and  numbers_dsc_order =="on":
        analyze_text=[]
        parameters = {'purpose': 'ERROR', 'analyzed_text': 'Error! Kindly, select any one option'}
        return render(request, 'analyze.html', parameters)

    elif numbers_asc_order=="on":
        analyze_text=list(djano_text.replace(' ', '\n').split())
        analyze_new = list(map(int, analyze_text))
        analyze_new.sort()
        analyze='\n'.join(map(str, analyze_new))
        parameters = {'purpose': 'Sort words as Ascending order', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)

    elif numbers_dsc_order=="on":
        analyze_text=list(djano_text.replace(' ', '\n').split())
        analyze_new = list(map(int, analyze_text))
        analyze_new.sort(reverse=True)
        analyze='\n'.join(map(str, analyze_new))
        parameters = {'purpose': 'Sort words as Ascending order', 'analyzed_text': analyze}
        return render(request, 'analyze.html', parameters)      
    
    #--------------------------------------------------------------------------------------------------------------------
                                                  #Regex-Email Extractor
    #--------------------------------------------------------------------------------------------------------------------
    if email_extrator=="on" :
        analyze=""
        patt = re.compile(r'\w+@\w+\.\w+')
        matches = patt.findall(djano_text)
        matches.sort()
        analyze_text="\n"
        str(matches)[1:-1]
        analyze=analyze_text.join(map(str, matches))
        parameters = {'purpose': 'Email Extrator', 'analyzed_text':analyze}
        return render(request, 'analyze.html', parameters)

    #--------------------------------------------------------------------------------------------------------------------
                                                  #Remove Punctuations
    #--------------------------------------------------------------------------------------------------------------------
    if remove_punctuations=="on":
        analyze=""
        for char in djano_text:
            if char not in string.punctuation:
                analyze=analyze+char
        parameters={'purpose':'Remove Punctuations','analyzed_text':analyze}
        return render(request,'analyze.html',parameters)


    #--------------------------------------------------------------------------------------------------------------------
                                                  #New Line Remover
    #--------------------------------------------------------------------------------------------------------------------
    if new_line_remover == "on":
        analyze = ""
        for char in djano_text:
            if char != "\n"and char!="\r":
                analyze = analyze + char

        parameters = {'purpose': 'Removed NewLines', 'analyzed_text': analyze}
        # Analyze the text
        return render(request, 'analyze.html', parameters)


    #--------------------------------------------------------------------------------------------------------------------
                                                  #Extra Space Remover
    #--------------------------------------------------------------------------------------------------------------------

    if extra_space_remover=="on":
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyze = analyze + char

        parameters = {'purpose': 'Removed Extra Space', 'analyzed_text': analyze}

        return render(request, 'analyze.html', parameters)

    #--------------------------------------------------------------------------------------------------------------------
                                                    #Counter
    #--------------------------------------------------------------------------------------------------------------------
    if counter=="on":
        analyze=0
        for char in djano_text:
            analyze=int(analyze+1)
        parameters={'purpose':'Number Remover','analyzed_text':analyze}
        return render(request,'analyze.html',parameters)
        