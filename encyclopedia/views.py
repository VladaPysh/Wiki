from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
import random
from django import forms

class NewPage(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    #get encyclopedia page by a title
    entryPage = util.get_entry(entry)
    #return error page if entry does not exist
    if entryPage is None:
        return render(request, "encyclopedia/error.html", {
            "title": entry
        })
    #show entry page information 
    else: 
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown(entryPage)
        })

def search(request):
    #get the query info
    query = request.GET.get('q')
    #compare to the list of entries available
    list_of_entries = util.list_entries()
    #if there is a match return entry page of a matching query
    if query in list_of_entries:
        return redirect("entry", entry=query)
    #if matching first few letters return to a search list of available results
    else:
        #declare a new list for entries which might partially match query
        entries = []
        #go through each entry in a list of entries to compare to the query(case insensitive) and add to a list
        for entry in list_of_entries:
            if query.lower() in entry.lower():
                entries.append(entry)
        #if found a match, display list of results
        if entries:
            return render(request, "encyclopedia/index.html", {
                "entries": entries
                })
        #if no match return error page
        else:
            return render(request, "encyclopedia/error.html", {
                "title": query
                })

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html", {
            "form": NewPage()
        })
    