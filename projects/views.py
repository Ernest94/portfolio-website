from django.shortcuts import render

def project_index(request):
    return render(request, 'project_index.html')

def project_detail(request, pk):
    if pk==1:
        return render(request, "project_detail_zwerfbond.html")
    elif pk==2:
        return render(request, "project_detail_omassoep.html")
