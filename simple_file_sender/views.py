# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from django.views.decorators.cache import cache_page
from simple_file_sender.models import UploadedFile
import pdb

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def upload(request):
	# pdb.set_trace()
	if request.is_ajax() and request.method == 'POST':
		f = request.FILES['file']
		name = f.name
		new_file = UploadedFile()
		new_file.name = name
		new_file.data.save(name, f)
		new_file.save()
		return HttpResponse('OK')
	return HttpResponse('NO')