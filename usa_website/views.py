from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Course, Blog
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from .forms import PostForm, AttendanceForm

from .utils.attendance import *

from .utils import attendance

# from .utils.attendance import GetAttendanceHeader, GetAttendanceDetails, LookupSIDs

##################################
####### MAIN STUFF ###############
##################################

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
    context = {}
    return HttpResponse(html.render(context))

def aboutus(request):
    html = get_template("aboutus.html")
    context = {}
    return HttpResponse(html.render({}))

def calendar(request):
    html = get_template("calendar.html")
    context = {}
    return HttpResponse(html.render({}))

##################################
########## COURSES ###############
##################################

def courseMap(request):
    t = get_template("course_map/course-map.html")
    context = {}
    return HttpResponse(t.render(context))

def data8(request):
    t = get_template("data-8.html")
    context = {}
    return HttpResponse(t.render(context))

def stat2(request):
    t = get_template("stat-2.html")
    context = {}
    return HttpResponse(t.render(context))

def stat20(request):
    t = get_template("stat-20.html")
    context = {}
    return HttpResponse(t.render(context))

def stat88(request):
    t = get_template("stat-88.html")
    context = {}
    return HttpResponse(t.render(context))

def stat89a(request):
    t = get_template("stat-89a.html")
    context = {}
    return HttpResponse(t.render(context))

def data100(request):
    t = get_template("data-100.html")
    context = {}
    return HttpResponse(t.render(context))

def data102(request):
    t = get_template("data-102.html")
    context = {}
    return HttpResponse(t.render(context))

def stat140(request):
    t = get_template("stat-140.html")
    context = {}
    return HttpResponse(t.render(context))

def stat133(request):
    t = get_template("stat-133.html")
    context = {}
    return HttpResponse(t.render(context))

def stat134(request):
    t = get_template("stat-134.html")
    context = {}
    return HttpResponse(t.render(context))

def stat135(request):
    t = get_template("stat-135.html")
    context = {}
    return HttpResponse(t.render(context))

def stat150(request):
    t = get_template("stat-150.html")
    context = {}
    return HttpResponse(t.render(context))

def stat151a(request):
    t = get_template("stat-151a.html")
    context = {}
    return HttpResponse(t.render(context))

def stat151b(request):
    t = get_template("stat-151b.html")
    context = {}
    return HttpResponse(t.render(context))

def stat152(request):
    t = get_template("stat-152.html")
    context = {}
    return HttpResponse(t.render(context))

def stat153(request):
    t = get_template("stat-153.html")
    context = {}
    return HttpResponse(t.render(context))

def stat154(request):
    t = get_template("stat-154.html")
    context = {}
    return HttpResponse(t.render(context))

def stat155(request):
    t = get_template("stat-155.html")
    context = {}
    return HttpResponse(t.render(context))

def stat157(request):
    t = get_template("stat-157.html")
    context = {}
    return HttpResponse(t.render(context))

def stat158(request):
    t = get_template("stat-158.html")
    context = {}
    return HttpResponse(t.render(context))

def stat159(request):
    t = get_template("stat-159.html")
    context = {}
    return HttpResponse(t.render(context))

def people(request):
    t = get_template("people.html")
    context = {}
    return HttpResponse(t.render(context))

##################################
###### COMMITTEE PAGES ###########
##################################

def webdev(request):
    t = get_template("committees/webdev.html")
    context = {}
    return HttpResponse(t.render(context))

def careerex(request):
    t = get_template("committees/careerex.html")
    context = {}
    return HttpResponse(t.render(context))

def research(request):
    t = get_template("committees/rp.html")
    context = {}
    return HttpResponse(t.render(context))

def dataconsulting(request):
    t = get_template("committees/dc.html")
    context = {}
    return HttpResponse(t.render(context))

def education(request):
    t = get_template("committees/education.html")
    context = {}
    return HttpResponse(t.render(context))

def community(request):
    t = get_template("community.html")
    context = {}
    return HttpResponse(t.render(context))

def mtc_map(request):
    t = get_template("dc/fa18/mtc_map.html")
    context = {}
    return HttpResponse(t.render(context))

#########################################
###### WEB DEV TUTORIAL BLOG POSTS ######
#########################################

def website_tutorial_0(request):
    t = get_template("blog/education/website-tutorial-0.html")
    context = {}
    return HttpResponse(t.render(context))

def website_tutorial_1(request):
    t = get_template("blog/education/website-tutorial-1.html")
    context = {}
    return HttpResponse(t.render(context))

def website_tutorial_2(request):
    t = get_template("blog/education/website-tutorial-2.html")
    context = {}
    return HttpResponse(t.render(context))

def website_tutorial_3(request):
    t = get_template("blog/education/website-tutorial-3.html")
    context = {}
    return HttpResponse(t.render(context))

def anatomy_of_a_basic_fullstack(request):
    t = get_template("blog/education/anatomy-of-a-basic-fullstack.html")
    context = {}
    return HttpResponse(t.render(context))

def basic_web_architecture(request):
    t = get_template("blog/education/basic-web-architecture.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### SPRING 2020 DC PROJECTS ######
#####################################

def uizard_sp20(request):
    t = get_template("blog/dc/sp20/uizard.html")
    context = {}
    return HttpResponse(t.render(context))

def concha_labs(request):
    t = get_template("blog/dc/sp20/concha-labs.html")
    context = {}
    return HttpResponse(t.render(context))

def ailanthus(request):
    t = get_template("blog/dc/sp20/ailanthus.html")
    context = {}
    return HttpResponse(t.render(context))

def pillar_learning(request):
    t = get_template("blog/dc/sp20/pillar-learning.html")
    context = {}
    return HttpResponse(t.render(context))

def pinxuan(request):
    t = get_template("blog/dc/sp20/pinxuan.html")
    context = {}
    return HttpResponse(t.render(context))

def indeed(request):
    t = get_template("blog/dc/sp20/indeed.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### FALL 2019 DC PROJECTS ######
#####################################

def trace_data(request):
    t = get_template("blog/dc/fa19/trace-data.html")
    context = {}
    return HttpResponse(t.render(context))

def data_secrets(request):
    t = get_template("blog/dc/fa19/data-secrets.html")
    context = {}
    return HttpResponse(t.render(context))

def grandmark(request):
    t = get_template("blog/dc/fa19/grandmark.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### SPRING 2019 DC PROJECTS ######
#####################################

def express_scripts(request):
    t = get_template("blog/dc/sp19/express-scripts.html")
    context = {}
    return HttpResponse(t.render(context))

def minted(request):
    t = get_template("blog/dc/sp19/minted.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### FALL 2018 DC PROJECTS ########
#####################################

def taco_bell(request):
    t = get_template("blog/dc/fa18/taco-bell.html")
    context = {}
    return HttpResponse(t.render(context))

def mtc(request):
    t = get_template("blog/dc/fa18/mtc.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### SPRING 2018 DC PROJECTS ######
#####################################

def tutorfly(request):
    t = get_template("blog/dc/sp18/tutorfly.html")
    context = {}
    return HttpResponse(t.render(context))

def facial_emotion_recognition(request):
    t = get_template("blog/dc/sp18/facial-emotion-recognition.html")
    context = {}
    return HttpResponse(t.render(context))

def data_good(request):
    t = get_template("blog/dc/sp18/data-for-good-proposal.html")
    context = {}
    return HttpResponse(t.render(context))

def uizard(request):
    t = get_template("blog/dc/sp18/uizard.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
####### FALL 2017 DC PROJECTS #######
#####################################
def population_modeling(request):
    t = get_template("blog/dc/fa17/population-modeling.html")
    context = {}
    return HttpResponse(t.render(context))

def food_insecurity(request):
    t = get_template("blog/dc/fa17/food-insecurity.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### FALL 2019 R&P PROJECTS ######
#####################################

def fighter_values(request):
    t = get_template("blog/rp/fa19/the-values-of-a-fighter.html")
    context = {}
    return HttpResponse(t.render(context))

def personalized_movie_rating(request):
    t = get_template("blog/rp/fa19/personalized-movie-rating.html")
    context = {}
    return HttpResponse(t.render(context))

def political_bias_digital_media(request):
    t = get_template("blog/rp/fa19/Fiat-Lux-Illuminating-Political-Bias-in-Digital-Media.html")
    context = {}
    return HttpResponse(t.render(context))
                        
def yelp(request):
    t = get_template("blog/rp/fa19/yelp.html")
    context = {}
    return HttpResponse(t.render(context))

def stock_prediction(request):
    t = get_template("blog/rp/fa19/stock-prediction.html")
    context = {}
    return HttpResponse(t.render(context))

###################################
### SPRING 2019 R&P PROJECTS ########
###################################
def predicting_horse_races(request):
    t = get_template("blog/rp/sp19/predicting-horse-races.html")
    context = {}
    return HttpResponse(t.render(context))

def women_in_government(request):
    t = get_template("blog/rp/sp19/women-in-government.html")
    context = {}
    return HttpResponse(t.render(context))

def winning(request):
    t = get_template("blog/rp/sp19/winning-the-mlb-world-series.html")
    context = {}
    return HttpResponse(t.render(context))

def machinelearning_and_finance(request):
    t = get_template("blog/rp/sp19/machinelearning-and-finance.html")
    context = {}
    return HttpResponse(t.render(context))

def identifying_art_styles(request):
    t = get_template("blog/rp/sp19/identifying-art-styles.html")
    context = {}
    return HttpResponse(t.render(context))

def eurovision(request):
    t = get_template("blog/rp/sp19/the-musical-chairs-of-eurovision.html")
    context = {}
    return HttpResponse(t.render(context))

def personality(request):
    t = get_template("blog/rp/sp19/personality.html")
    context = {}
    return HttpResponse(t.render(context))

def fakenews(request):
    t = get_template("blog/rp/sp19/political-bias-in-mainstream-news-media.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### FALL 2018 R&P PROJECTS ######
#####################################
def music_moods(request):
	t = get_template("blog/rp/fa18/music-moods.html")
	context = {}
	return HttpResponse(t.render(context))

def polls(request):
	t = get_template("blog/rp/fa18/polls.html")
	context = {}
	return HttpResponse(t.render(context))

def league_of_legends(request):
	t = get_template("blog/rp/fa18/league-of-legends.html")
	context = {}
	return HttpResponse(t.render(context))

def toxic_social_media(request):
    t = get_template("blog/rp/fa18/toxic-social-media.html")
    context = {}
    return HttpResponse(t.render(context))

def meaning_of_probabilities_in_social_sciences(request):
    t = get_template("blog/rp/fa18/meaning-of-probabilities-in-social-sciences.html")
    context = {}
    return HttpResponse(t.render(context))

def schooling(request):
    t = get_template("blog/rp/fa18/schooling.html")
    context = {}
    return HttpResponse(t.render(context))

def DIJA(request):
    t = get_template("blog/rp/fa18/DIJA.html")
    context = {}
    return HttpResponse(t.render(context))

#####################################
###### SPRING 2018 R&P PROJECTS ######
#####################################
def bart_ridership_data(request):
    t = get_template("blog/rp/sp18/bart-ridership-data.html")
    context = {}
    return HttpResponse(t.render(context))

def capsim(request):
	t = get_template("blog/rp/sp18/capsim.html")
	context = {}
	return HttpResponse(t.render(context))

def SteinerTreeProblem(request):
	t = get_template("blog/rp/spr18/SteinerTreeProblem.html")
	context = {}
	return HttpResponse(t.render(context))

def college_vs_nba_success(request):
	t = get_template("blog/rp/sp18/college-vs-nba-success.html")
	context = {}
	return HttpResponse(t.render(context))

def number_concept(request):
	t = get_template("blog/rp/sp18/num-concept.html")
	context = {}
	return HttpResponse(t.render(context))

def suicide(request):
    t = get_template("blog/rp/sp18/suicide.html")
    context = {}
    return HttpResponse(t.render(context))

##################################
###### FALL 2017 R&P PROJECTS ######
##################################

def shallow_dive(request):
    t = get_template("blog/rp/a-shallow-dive-into-time-series-analysis-of-local-restaurant-data-using-r.html")
    context = {}
    return HttpResponse(t.render(context))

def tobacco_heart_disease(request):
    t = get_template("blog/rp/a-spatial-investigation-into-heart-disease-mortality-rates-and-youth-tobacco-rates.html")
    context = {}
    return HttpResponse(t.render(context))

def alphago(request):
    t = get_template("blog/rp/an-introduction-to-go-alphago-and-quantifying-go-gameplay.html")
    context = {}
    return HttpResponse(t.render(context))

def rapnet(request):
    t = get_template("blog/rp/rapnet-machine-learning-for-hip-hop-artist-classification.html")
    context = {}
    return HttpResponse(t.render(context))

def evol_lyrics(request):
    t = get_template("blog/rp/the-evolution-of-lyrics.html")
    context = {}
    return HttpResponse(t.render(context))

def ucb_ug_mental(request):
    t = get_template("blog/rp/uc-berkeley-undergraduates-general-mental-health-and-use-of-mental-health-services.html")
    context = {}
    return HttpResponse(t.render(context))

def world_happiness(request):
    t = get_template("blog/rp/world-happiness-report-eda.html")
    context = {}
    return HttpResponse(t.render(context))

def yelp_review(request):
    t = get_template("blog/rp/yelp-review-and-rating-analysis.html")
    context = {}
    return HttpResponse(t.render(context))

###################################
######### WEB DEV #################
###################################
def ucpd_crime(request):
    t = get_template("webdev/dataviz/sp19/ucpd-crime.html")
    context = {}
    return HttpResponse(t.render(context))

def montyhall(request):
    t = get_template("webdev/montyhall.html")
    context = {}
    return HttpResponse(t.render(context))

def hallofmemes(request):
    t = get_template("webdev/hallofmemes.html")
    context = {}
    return HttpResponse(t.render(context))


###################################
########## CRASH COURSES ##########
###################################
def r0(request):
    t = get_template("blog/education/r0.html")
    context = {}
    return HttpResponse(t.render(context))

def r1(request):
    t = get_template("blog/education/r1.html")
    context = {}
    return HttpResponse(t.render(context))

def r2(request):
    t = get_template("blog/education/r2.html")
    context = {}
    return HttpResponse(t.render(context))

def p0(request):
    t = get_template("blog/education/p0.html")
    context = {}
    return HttpResponse(t.render(context))

def bias_variance(request):
    t = get_template("blog/education/bias-variance-decision-trees-ensemble-learning.html")
    context = {}
    return HttpResponse(t.render(context))

def ml_classification(request):
    t = get_template("blog/education/MLclassification.html")
    context = {}
    return HttpResponse(t.render(context))

###################################
######### INTERVIEWS ###########
###################################

def lily_bhattacharjee_interview(request):
    t = get_template("interviews/sp19/lily-bhattacharjee-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def megan_zhu_interview(request):
    t = get_template("interviews/sp19/megan-zhu-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def rachel_li_interview(request):
    t = get_template("interviews/sp19/rachel-li-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def irene_wang_interview(request):
    t = get_template("interviews/sp19/irene-wang-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def joyce_zheng_interview(request):
    t = get_template("interviews/sp19/joyce-zheng-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def calvin_chen_interview(request):
    t = get_template("interviews/sp19/calvin-chen-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def oscar_syu_interview(request):
    t = get_template("interviews/sp19/oscar-syu-interview.html")
    context = {}
    return HttpResponse(t.render(context))

def zoe_liu_interview(request):
    t = get_template("interviews/sp19/zoe-liu-interview.html")
    context = {}
    return HttpResponse(t.render(context))


##################################
###### NEWSLETTERS ###############
##################################

def march_2019(request):
    t = get_template("newsletters/march_2019.html")
    context = {}
    return HttpResponse(t.render(context))

###################################
############# MEME ################
###################################
def housingcRincess(request):
    t = get_template("meme/housingcRincess.html")
    context = {}
    return HttpResponse(t.render(context))

def aDishwasher(request):
    t = get_template("meme/aDishwasher.html")
    context = {}
    return HttpResponse(t.render(context))

def sheepinav(request):
    t = get_template("meme/sheepinav.html")
    context = {}
    return HttpResponse(t.render(context))

###################################
######### MISCELLANEOUS ###########
###################################

def view_post(request, slug):
    return render_to_response('viewPost.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_author(request, author):
    return render_to_response('viewAuthor.html', {
        'posts': Blog.objects.all()
    })

def susawebapp(request):
    t = get_template("webapp/index.html")
    context = {}
    return HttpResponse(t.render(context))

def housingcrisis(request):
    t = get_template("housingcrisis/index.html")
    context = {}
    return HttpResponse(t.render(context))

def textboxio(request):
    t = get_template("textboxio/textboxio.js")
    context = {}
    return HttpResponse(t.render(context))


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = "-".join(post.title.split(" "))
            post.save()
            return redirect('/blog/view/' + post.slug + ".html")
    else:
        form = PostForm()

    return render(request, 'unused/submit.html', {'form': form})

def convert_csv(request):
    t= get_template("webapp/convert_csv.py")
    context = Context({})
    return HttpResponse(t.render(context))

class AttendanceView(TemplateView):
    #Please view /usa_website/utils/attendance.py to understand GetAttendanceHeader + Details
    template_name = "attendance.html"

    def get(self, request):
        form = AttendanceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AttendanceForm(request.POST)
        if form.is_valid():
            SID = form.cleaned_data['post']
            if SID == '0':
                text = "Error: Please Submit A Valid SID"
                form = AttendanceForm()
                args = {'form': form, 'text': text}
                return render(request, self.template_name, args)
            else:
                #text = "Points Summary for SID - " + form.cleaned_data['post'] +": "
                text = form.cleaned_data['post']
                #values = LookupSIDs()
                #head_list = GetAttendanceHeader(SID)
                #det_list = GetAttendanceDetails(SID, values)
                exists = attendance.check_sid_exists(SID);
                if exists:
                    points = attendance.get_points(SID)
                    attended_events = attendance.get_events(SID)
                    args = {'form': form, 'text': text, 'points': points, 'attended_events': attended_events}
                    return render(request, self.template_name, args)
                else:
                    text = "Your SID does not appear in our records, please check if you have made an error or email us at execs@saas.berkeley.edu."
                    form = AttendanceForm()
                    args = {'form': form, 'text': text}
                    return render(request, self.template_name, args)
        else:
            text = "Error: Please Submit A Valid SID"

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def blog(request):
    return render_to_response('blog/blog.html', {
        'posts': Blog.objects.all()#[-1:-6:-1]
    })

    #t = get_template("blog/blog.html")
    #context = Context({})
    #return HttpResponse(t.render(context))
