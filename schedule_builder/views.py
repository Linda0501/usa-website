from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Course

# Create your views here.
def index(request):
        #return render(request, 'schedule_builder.html', {})
	courses = Course.objects.all()
	context = {"courses": courses}
	t = get_template("schedule_builder.html")
	vals = request.GET.getlist('course_name')
	html = t.render(context)
	return HttpResponse(html, context)

def home(request):
	html = get_template("index.html")
	context = Context({})
	return HttpResponse(html.render(context))

def aboutus(request):
	html = get_template("aboutus.html")
	context = Context({})
	return HttpResponse(html.render({}))

def stat133(request):
	t = get_template("stat-133.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat134(request):
	t = get_template("stat-134.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat135(request):
	t = get_template("stat-135.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat150(request):
	t = get_template("stat-150.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat151a(request):
	t = get_template("stat-151a.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat151b(request):
	t = get_template("stat-151b.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat152(request):
	t = get_template("stat-152.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat153(request):
	t = get_template("stat-153.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat154(request):
	t = get_template("stat-154.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat155(request):
	t = get_template("stat-155.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat157(request):
	t = get_template("stat-157.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat158(request):
	t = get_template("stat-158.html")
	context = Context({})
	return HttpResponse(t.render(context))

def stat159(request):
	t = get_template("stat-159.html")
	context = Context({})
	return HttpResponse(t.render(context))

def people(request):
	t = get_template("people.html")
	context = Context({})
	return HttpResponse(t.render(context))

def courseMap(request):
	t = get_template("course-map.html")
	context = Context({})
	return HttpResponse(t.render(context))

def webdev(request):
	t = get_template("webdev.html")
	context = Context({})
	return HttpResponse(t.render(context))

def careerex(request):
	t = get_template("careerex.html")
	context = Context({})
	return HttpResponse(t.render(context))

def research(request):
	t = get_template("research.html")
	context = Context({})
	return HttpResponse(t.render(context))
def project(request):
	t = get_template("project.html")
	context = Context({})
	return HttpResponse(t.render(context))
