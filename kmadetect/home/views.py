#kmadetect
#By Nguyen Trung


import sys
import json
sys.path.insert(0, '../reverse/')
sys.path.insert(0, '../detect/')
import reverse.reverse as rvs
import detect.Train as t

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

PATH_TEMP = '../reverse/tempApks'


# Create your views here.
def index(request):
   return render(request, 'pages/home.html')


def upload(request):
   context = {}

   if request.method == 'POST':
      uploaded_file = request.FILES['fileApk']
      fs = FileSystemStorage()
      name = fs.save(uploaded_file.name, uploaded_file)
      print(name)
      context['url'] = fs.path(name)

      # while True:
      #    if os.path.exists(fs.path(name)):
      #       break
      # time.sleep(20)

      # shutil.move(fs.path(name), os.path.join(PATH_TEMP, name))
      nameMd5, apk_total_analysis = rvs.reverse(name)
      if nameMd5 == 'Error':
         labelDetect = 'Null'
      else:
         labelDetect = t.detectApk(nameMd5)

      if labelDetect == 'Null':
         Mess = 'Cant detect what kind of file'
      else:
         Mess = 'Detected'

      context['labelDetect'] = labelDetect
      context['Mess'] = Mess
      context['apk_total_analysis'] = apk_total_analysis
      # context['pre_static_dict'] = apk_total_analysis['pre_static_dict']
      # context['static_analysis_dict'] = apk_total_analysis['static_analysis_dict']
      print(context)
      contextfinal = json.loads(json.dumps(context))
      print(contextfinal)
   return render(request, 'pages/resuilt.html', contextfinal)

def pagedownload(request):
    return render(request, 'pages/downloadapk.html')

def checkapk(request):
    return render(request, 'pages/checkapk.html')