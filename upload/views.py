from django.shortcuts import render,redirect
from django.urls import reverse
from upload.forms import UploadForm,UploadsFilesForm
# Create your views here.

def upload(request):
    if request.POST:
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            uf.save()
            ufso = uf.instance
            return render(request, 'upload/upload.html', {'uf':uf,'ufso':ufso,})

    else:
        uf = UploadForm()

    return render(request,'upload/upload.html',{'name':'upload image','uf':uf,})


# ----------
def upload_files(request):
    if request.POST:
        uff = UploadsFilesForm(request.POST, request.FILES)
        if uff.is_valid():
            uff.save()
            uffso = uff.instance
            return render(request, 'upload/uploadfiles.html', {'uff':uff,'uffso':uffso,})

    else:
        uff = UploadsFilesForm()

    return render(request,'upload/uploadfiles.html',{'name':'upload files','uff':uff,})