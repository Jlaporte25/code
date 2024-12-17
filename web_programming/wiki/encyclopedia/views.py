from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
import markdown2
from django.http import Http404
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()

    # Find matching entries
    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

    # If exact match, redirect to the entry page
    if query in entries:
        return redirect("encyclopedia:entry", title=query)

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "entries": matching_entries
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Check if the entry already exists
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists."
            })

        # Save the new entry
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)

    return render(request, "encyclopedia/new_page.html")

def entry(request, title):
    # Retrieve the content of the entry
    entry_content = util.get_entry(title)

    # If the entry does not exist, raise a 404 error
    if entry_content is None:
        raise Http404("Entry not found")

    # Convert Markdown to HTML
    entry_html = markdown2.markdown(entry_content)

    # Return the entry page
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": entry_html
    })

# views.py
def edit_page(request, title):
    entry_content = util.get_entry(title)

    if request.method == "POST":
        new_content = request.POST.get("content")
        util.save_entry(title, new_content)
        return redirect("encyclopedia:entry", title=title)

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": entry_content
    })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect("encyclopedia:entry", title=random_entry)