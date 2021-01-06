from django.shortcuts import render
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/error.html", {
            "title": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "content": markdown(entryPage)
        })

def search(request):
    entry = request.GET.get("q", "")
    entryPage = util.get_entry(entry)
    
    return render(request, "encyclopedia/entry.html", {
        "content": markdown(entryPage)
    })
