# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from django.views.decorators.cache import cache_page
import pdb

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def upload(request):
	
	return HttpResponse('OK')