from django.http import HttpResponse,Http404
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"% now
    return HttpResponse(html)


def hours_ahead(request,nbHours):
	try:
		nbHours = int(nbHours)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=nbHours)
	html = "In %s hour(s), it will be %s."%(nbHours,dt)
	return HttpResponse(html)