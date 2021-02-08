from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
import random
from django import forms

class NewPage(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 30%'}))
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'style': 'height: 50%;width:100%'}))

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
            "entry": markdown(entryPage),
            "entry_title": entry
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
    if request.method == "POST":
        form = NewPage(request.POST)
        #check if form is valid
        if form.is_valid():
            #get values for title and context
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            #compare title name to the existing list of title names
            list_of_entries = util.list_entries()
            if title in list_of_entries:
                #if match return error 
                return render(request, "encyclopedia/error1.html", {
                    "title": title
                })
            #else save into a new file
            else:
                util.save_entry(title, f'#{title}\n{content}')
                return redirect("entry", entry=title)
        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": form
            })
    #if request get, render form page
    else:
        return render(request, "encyclopedia/newpage.html", {
            "form": NewPage()
        })

def edit(request, entry):
    if request.method == "POST":
        content = util.get_entry(entry)
        form = NewPage(request.POST)
        if form.is_valid():
            #save changes using save_entry and redirect to the entry page
            content = form.cleaned_data["content"]
            title = form.cleaned_data["title"]
            util.save_entry(title, content)
            return redirect("entry", entry=title)
    else:
        content = util.get_entry(entry)
        #get form fill with info about entry. title and content
        form = NewPage(initial={"title": entry, "content": content})
        return render(request, "encyclopedia/edit.html", {
            "form": form,
            "entry_title": entry
        })

def randompage(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return redirect("entry", entry=entry)