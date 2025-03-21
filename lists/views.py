from django.shortcuts import render

def custom_404_error(request,exception):
    return render(request,'404error.html',status=404)