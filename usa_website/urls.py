"""usa_website URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import sys
import os
sys.path.insert(0, 'schedule_builder')
sys.path.insert(1, '../schedule_builder')
#import urls
from django.conf import settings
from django.conf.urls.static import static
#from schedule_builder import views as extraViews
from usa_website import views
admin.autodiscover()

"""
urlpatterns = [
    url('^$', extraViews.home, name='home'),
    url('aboutus', extraViews.aboutus, name='aboutus'),
    url('index', extraViews.index, name='index'),
        url('stat-133', extraViews.stat133, name="stat133"),
        url('stat-134', extraViews.stat134, name="stat134"),
        url('stat-135', extraViews.stat135, name="stat135"),
        url('people', extraViews.people, name="people"),
        url('course-map', extraViews.courseMap, name="courseMap"),
        url('project', extraViews.project, name="project"),
    url(r'^schedule-builder/', include('schedule_builder.urls')),
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index$', views.index, name = 'index'),
    #url(r'index_new$', views.index_new, name = 'index_new'),
    url(r'home$', views.home, name = 'home'),
    url(r'^$', views.home, name = 'home'),
    #url(r'aboutus$', views.aboutus, name = 'aboutus'),
    url(r'calendar$', views.calendar, name = 'calendar'),
    url(r'attendance', views.AttendanceView.as_view(), name = "attendance"),
    url(r'people$', views.people, name = "people"),
    #url(r'officehours$', views.officehours, name='officehours'),
    # COURSE PAGES
    url(r'data-8$', views.data8, name = "data8"),
    url(r'stat-2$', views.stat2, name = "stat2"),
    url(r'stat-20$', views.stat20, name = "stat20"),
    url(r'stat-88$', views.stat88, name = "stat88"),
    url(r'stat-89a$', views.stat89a, name = "stat89a"),
    url(r'data-100$', views.data100, name = "data100"),
    url(r'data-102$', views.data102, name = "data102"),
    url(r'stat-140$', views.stat140, name = "stat140"),
    url(r'stat-133$', views.stat133, name = "stat133"),
    url(r'stat-134$', views.stat134, name = "stat134"),
    url(r'stat-135$', views.stat135, name = "stat135"),
    url(r'stat-150$', views.stat150, name = "stat150"),
    url(r'stat-151a$', views.stat151a, name = "stat151a"),
    url(r'stat-151b$', views.stat151b, name = "stat151b"),
    url(r'stat-152$', views.stat152, name = "stat152"),
    url(r'stat-153$', views.stat153, name = "stat153"),
    url(r'stat-154$', views.stat154, name = "stat154"),
    url(r'stat-155$', views.stat155, name = "stat155"),
    url(r'stat-157$', views.stat157, name = "stat157"),
    url(r'stat-158$', views.stat158, name = "stat158"),
    url(r'stat-159$', views.stat159, name = "stat159"),
    url(r'course-map$', views.courseMap, name = "courseMap"),
    # COMMITTEES
    url(r'dataconsulting$', views.dataconsulting, name = "dataconsulting"),
    url(r'education$', views.education, name = "education"),
    url(r'webdev$', views.webdev, name="webdev"),
    url(r'careerex$', views.careerex, name="careerex"),
    url(r'research$', views.research, name="research"),
    url(r'community$', views.community, name="community"),
    #url(r'comingSoon$', views.comingSoon, name="comingSoon"),
    url(r'blog/$', views.blog, name="blog"),
    #NEWSLETTERS
    url(r'march_2019.html$', views.march_2019, name="march-2019"),
    url(r'mtc_map$', views.mtc_map, name="mtc-map"),
    # FALL 2019 R&P PROJECTS
    url(r'rp/the-values-of-a-fighter$', views.fighter_values, name='fighter_values'),
    url(r'rp/personalized-movie-rating$', views.personalized_movie_rating, name="personalized_movie_rating"),    
    url(r'political-bias-digital-media',views.political_bias_digital_media, name="political_bias_digital_media"),
    url(r'rp/yelp$', views.yelp, name='yelp'),
    url(r'rp/stock-prediction$', views.stock_prediction, name="stock_prediction"),
    url(r'rp/arima$', views.arima, name="arima"),
    # SPRING 2019 R&P PROJECTS
    url(r'rp/predicting-horse-races$', views.predicting_horse_races, name='predicting_horse_races'),
    url(r'rp/DIJA$', views.DIJA, name='DIJA'),
    url(r'rp/women-in-government$', views.women_in_government, name="women-in-government"),
    url(r'rp/winning-the-mlb-world-series$', views.winning, name="winning-the-mlb-world-series"),
    url(r'rp/machinelearning-and-finance$', views.machinelearning_and_finance, name="machinelearning-and-finance"),
    url(r'rp/identifying-art-styles$', views.identifying_art_styles, name='identifying_art_styles'),
    url(r'rp/eurovision$', views.eurovision, name='eurovision'),
    url(r'rp/personality$', views.personality, name='personality'),

    # FALL 2018 R&P PROJECTS
    url(r'rp/music-moods$', views.music_moods, name="music_moods"),
    url(r'rp/polls$', views.polls, name="polls"),
    url(r'rp/league-of-legends$', views.league_of_legends, name='league_of_legends'),
    url(r'rp/toxic-social-media$', views.toxic_social_media, name='toxic_social_media'),
    url(r'rp/schooling$', views.schooling, name='schooling'),
    url(r'rp/meaning-of-probabilities-in-social-sciences$', views.meaning_of_probabilities_in_social_sciences, name="meaning_of_probabilities_in_social_sciences"),
    url(r'rp-fakenews$', views.fakenews, name = "fake_news_rp"),

    # SPRING 2018 R&P PROJECTS
    url(r'rp/bart-ridership-data$', views.bart_ridership_data, name="bart_ridership_data"),
    url(r'rp/capsim$', views.capsim, name="capsim"),
    url(r'rp/college-vs-nba-success$', views.college_vs_nba_success, name="college_vs_nba_success"),
    url(r'rp/num-concept$', views.number_concept, name="number_concept"),
    url(r'rp/SteinerTreeProblem$', views.SteinerTreeProblem, name="SteinerTreeProblem"),
    url(r'rp/suicide$', views.suicide, name="suicide"),

    # FALL 2017 R&P PROJECTS
    url(r'rp/a-shallow-dive-into-time-series-analysis-of-local-restaurant-data-using-r$', views.shallow_dive, name="shallow_dive"),
    url(r'rp/a-spatial-investigation-into-heart-disease-mortality-rates-and-youth-tobacco-rates$', views.tobacco_heart_disease, name="tobacco_heart_disease"),
    url(r'rp/an-introduction-to-go-alphago-and-quantifying-go-gameplay$', views.alphago, name="alphago"),
    url(r'rp/rapnet-machine-learning-for-hip-hop-artist-classification$', views.rapnet, name="rapnet"),
    url(r'rp/the-evolution-of-lyrics$', views.evol_lyrics, name="evol_lyrics"),
    url(r'rp/uc-berkeley-undergraduates-general-mental-health-and-use-of-mental-health-services$', views.ucb_ug_mental, name="ucb_ug_mental"),
    url(r'rp/world-happiness-report-eda$', views.world_happiness, name="world_happiness"),
    url(r'rp/yelp-review-and-rating-analysis$', views.yelp_review, name="yelp_review"),

    # CRASH COURSES
    url(r'education/installing-r-and-rstudio$', views.r0, name="r0"),
    url(r'education/base-r-and-basic-packages$', views.r1, name="r1"),
    url(r'education/preparing-for-data-analysis$', views.r2, name="r2"),
    url(r'education/bias-variance-decision-trees-ensemble-learning$', views.bias_variance, name="bias_variance"),
    url(r'education/installing-python-and-anaconda$', views.p0, name="p0"),
    url(r'education/ml-classification$', views.ml_classification, name="ml_classification"),
    url(r'education/website-tutorial-0$', views.website_tutorial_0, name="website_tutorial_0"),
    url(r'education/website-tutorial-1$', views.website_tutorial_1, name="website_tutorial_1"),
    url(r'education/website-tutorial-2$', views.website_tutorial_2, name="website_tutorial_2"),
    url(r'education/website-tutorial-3$', views.website_tutorial_3, name="website_tutorial_3"),
    url(r'education/anatomy-of-a-basic-fullstack$', views.anatomy_of_a_basic_fullstack, name="anatomy_of_a_basic_fullstack"),
    url(r'education/basic-web-architecture$', views.basic_web_architecture, name="basic_web_architecture"),

    # SPRING 2020 DC PROJECTS
    url(r'dataconsulting/uizard-sp20$', views.uizard_sp20, name="uizard_sp20"),
    url(r'dataconsulting/concha-labs$', views.concha_labs, name="concha_labs"),
    url(r'dataconsulting/ailanthus$', views.ailanthus, name="ailanthus"),
    url(r'dataconsulting/pillar-learning$', views.pillar_learning, name="pillar_learning"),
    url(r'dataconsulting/pinxuan$', views.pinxuan, name="pinxuan"),
    url(r'dataconsulting/indeed$', views.indeed, name="indeed"),


    #FALLL 2019 DC PROJECTS
    url(r'dataconsulting/trace-data$', views.trace_data, name="trace_data"),
    url(r'dataconsulting/data-secrets$', views.data_secrets, name="data_secrets"),
    url(r'dataconsulting/grandmark$', views.grandmark, name="grandmark"),

    #SPRING 2019 DC PROJECTS
    url(r'dataconsulting/express-scripts$', views.express_scripts, name="express_scripts"),
    url(r'dataconsulting/minted$', views.minted, name="minted"),


    #FALL 2018 DC PROJECTS
     url(r'dataconsulting/taco-bell$', views.taco_bell, name="taco_bell"),
    url(r'dataconsulting/mtc$', views.mtc, name="mtc"),


    #SPRING 2018 DC PROJECTS
    url(r'dataconsulting/tutorfly$', views.tutorfly, name="tutorfly"),
    url(r'dataconsulting/facial-emotion-recognition$', views.facial_emotion_recognition, name="facial_emotion_recognition"),
    url(r'dataconsulting/data-for-good-proposal$', views.data_good, name="data_good"),
    url(r'dataconsulting/uizard$', views.uizard, name="uizard"),


    #FALL 2017 DC PROJECTS
    url(r'dataconsulting/population-modeling$', views.population_modeling, name="population_modeling"),
    url(r'dataconsulting/food-insecurity$', views.food_insecurity, name="food_insecurity"),


    #MISCELLANEOUS
    url(r'textboxio/textboxio.js', views.textboxio, name = "textboxio"),
    # url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'webapp/', views.susawebapp, name = "susawebapp"),
    url(r'population-modeling-webapp/', views.susawebapp, name = "susawebapp"),
    url(r'housingcrisis$', views.housingcrisis, name = "housingcrisis"),
    url(r'housingcrisis/$', views.housingcrisis, name = "housingcrisis"),

    #MEME
    url(r'housingcRincess$', views.housingcRincess, name = "housingcRincess"),
    url(r'aDishwasher$', views.aDishwasher, name = "aDishwasher"),
    url(r'sheepinav$', views.sheepinav, name = "sheepinav"),
    url(r'montyhall$', views.montyhall, name = "montyhall"),
    # Web Dev - Data Viz Spring 2019??
    url(r'webdev/ucpd-crime$', views.ucpd_crime, name="ucpd_crime"),
    url(r'hallofmemes$', views.hallofmemes, name="hallofmemes"),

    #INTERVIEWS
    url(r'interviews/sp19/lily-bhattacharjee-interview$', views.lily_bhattacharjee_interview, name="lily_bhattacharjee_interview"),
    url(r'interviews/sp19/megan-zhu-interview$', views.megan_zhu_interview, name="megan_zhu_interview"),
    url(r'interviews/sp19/rachel-li-interview$', views.rachel_li_interview, name="rachel_li_interview"),
    url(r'interviews/spr19/irene-wang-interview$', views.irene_wang_interview, name="irene_wang_interview"),
    url(r'interviews/sp19/joyce-zheng-interview$', views.joyce_zheng_interview, name="joyce_zheng_interview"),
    url(r'interviews/sp19/calvin-chen-interview$', views.calvin_chen_interview, name="calvin_chen_interview"),
    url(r'interviews/sp19/oscar-syu-interview$', views.oscar_syu_interview, name="oscar_syu_interview"),
    url(r'interviews/sp19/zoe-liu-interview$', views.zoe_liu_interview, name="zoe_liu_interview"),
    url(r'convert_csv.py', views.convert_csv, name = "convert_csv"),
    url(r'yitz/textboxio/textboxio.js', views.textboxio, name = "textboxio"),
    url(r'^post/new/$', views.post_new, name='post_new')


        #url('^', include('schedule_builder.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
