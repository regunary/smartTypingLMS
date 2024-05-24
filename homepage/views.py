from decimal import Context
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
# from django.http import FileResponse
from homepage.models import *
from homepage.homefunction import *
import random
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
import datetime

#sử dụng cho password reset
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import get_template, render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django import template

# introduction
def index(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context = {
            'account': account,
        }
    return render(request, 'homepage/index.html', context)

def about(request):
    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context = {
            'account': account,
        }
    else:
        context = {

        }
    return render(request, 'homepage/about.html', context)

def aboutbee(request):
    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context = {
            'account': account,
        }
    else:
        context = {
            
        }   
    return render(request, 'homepage/aboutbee.html', context)

# login - logout - dashboard
def myregister(request):
    message = ''
    # Nếu đã đăng nhập --> index
    if request.user.is_authenticated:
        return render(request, 'homepage/updateinfo.html')
    else:
        if request.method == 'POST':  
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            avatar = request.FILES.get('avatar')
            
            # Kiểm tra username, password1 và password2 có rỗng hoặc password1 != password2 hay không
            if username == '' or password1 == '' or password2 == '' or password1 != password2:
                return render(request, 'homepage/register.html')
            else:
                try:
                    user = User.objects.get(username=username)
                except:
                    new_user = User()
                    new_user.username = username
                    new_user.set_password(password1)
                    new_user.save()
                    user = authenticate(username=username, password=password1)
                    login(request, user)

                    new_account = Account()
                    new_account.username = new_user
                    new_account.callsignid = CallSign.objects.get(pk = 1)
                    new_account.password = password1
                    new_account.avatar = tokenFile(avatar,'media/users', username ,1)

                    new_account.save()
                    return redirect('homepage:updateinfo')
                                   
                context = {'message':'Tài khoản đã tồn tại'}
                return render(request, 'homepage/register.html',context)
                # return render(request, 'homepage/updateinfo.html')
                
        return render(request, 'homepage/register.html')

def updateinfo(request):
    current_user = request.user
    account = Account.objects.get(username = current_user.id)

    context = {
        'account': account,
        'current_user': current_user,
    }

    check_user_detail = len(UserDetail.objects.filter(accountid = account))
    if check_user_detail != 0:
        userdetail = UserDetail.objects.get(accountid = account)
        context.update({
            'userdetail': userdetail,
        })

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        userobject = request.POST.get('objectchoice')
        grade = request.POST.get('gradelevelchoice')
        yearofbirth = request.POST.get('yearofbirth')
        guardian = request.POST.get('guardian')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        current_user = request.user
        account = Account.objects.get(username = current_user.id)

        if check_user_detail == 0:
            user_detail = UserDetail()
            user = User()
        else:
            user_detail = UserDetail.objects.get(accountid = account)
            user = User.objects.get(username =current_user)
        user.email = email
        user.last_name = lastname
        user.first_name = firstname
        user.save()

        user_detail.accountid = account
        user_detail.lastname = lastname
        user_detail.firstname = firstname
        user_detail.userobject = userobject
        if grade != '':
            user_detail.grade = grade
        if yearofbirth != '':
            user_detail.yearofbirth = yearofbirth 
        user_detail.guardian = guardian 
        user_detail.email = email
        user_detail.phone = phone
        user_detail.save()
        
        return redirect('homepage:index')
    else:
        return render(request, 'homepage/updateinfo.html')
        # return render(request, 'homepage/profile.html', context)

def mylogin(request):
    if request.user.is_authenticated: 
        # print(request.get_full_path)
        # lay id trang hien tai va quay lai sau khi dang nhap -> how
        # return redirect(request.path)
        enurl = 'homepage:index'

        return redirect('homepage:index')
    else:
        print(request.path)
        if request.method == 'POST':
            # Lấy username và password
            username = request.POST.get('username')
            password = request.POST.get('password')  
            # kiểm tra xem username và password có trong dữ liệu không
            user = authenticate(username=username, password=password)
            if user is not None: # Nếu tìm thấy user có username và password đã nhập
                if user.is_active: # Tài khoản có bị vô hiệu chưa - đã/ còn hiệu lực
                    print('active')
                    login(request, user)
                    # trả về trang index
                    enurl = 'homepage:index'
                    # current_path = request.path
                    # url = {
                    #     '/gioi-thieu': 'homepage:about',
                    #     '/danh-sach-bai-hoc': 'homepage:lesson',
                    #     '/luyen-tap': 'homepage:practice',
                    #     '/kiem-tra': 'homepage:test',
                    #     '/cuoc-thi': 'homepage:competition',
                    #     '/tin-tuc': 'homepage:news',
                    #     '/tai-lieu': 'homepage:document',
                    #     '/cau-hoi-thuong-gap': 'homepage:faq',
                    #     '/lien-he': 'homepage:contact',
                    # }
                    # if current_path in url.keys():
                    #     enurl = url[current_path]
                    # print(current_path)
                    
                    return redirect(enurl)
                else:
                    return render(request, 'homepage/login.html', context={'message':'Tài khoản đã bị vô hiệu hóa'})
            else:
                # kiem tra email
                email = UserDetail.objects.filter(email = username)
                # kiem tra sdt
                phone = UserDetail.objects.filter(phone = username)
                if len(email) != 0 or len(phone) != 0:
                    correct_username = email[0] if len(email) != 0 else phone[0]
                    account = Account.objects.get(accountid = correct_username.accountid.pk)
                    current_user = User.objects.get(pk = account.username.pk)
                    check_password = current_user.check_password(password)
                    if check_password:
                        user = authenticate(username=current_user.username, password=password)
                        login(request, user)
                        return redirect('homepage:index')
                    else:
                        return render(request, 'homepage/login.html', context={'message':'Sai mật khẩu hoặc tên đăng nhập'})
                else:
                    return render(request, 'homepage/login.html', context={'message':'Tài khoản không tồn tại'})
        return render(request, 'homepage/login.html')
    
def mylogout(request):
    # Nếu không có tài khoản nào thì không thực hiện hàm đăng xuất
    try:
        logout(request)
    except:
        pass
    # Nếu đăng xuất thành công => trả về trang đăng nhập - login
    # return render(request, 'homepage/login.html')
    enurl = 'homepage:index'
    # current_path = next_path
    # print(current_path)
    url = {
        '/gioi-thieu': 'homepage:about',
        '/danh-sach-bai-hoc': 'homepage:lesson',
        '/luyen-tap': 'homepage:practice',
        '/kiem-tra': 'homepage:test',
        '/cuoc-thi': 'homepage:competition',
        '/tin-tuc': 'homepage:news',
        '/tai-lieu': 'homepage:document',
        '/cau-hoi-thuong-gap': 'homepage:faq',
        '/lien-he': 'homepage:contact',
    }
    # if current_path in url.keys():
    #     enurl = url[current_path]
    # print(current_path)
    
    return redirect(enurl)
    # return redirect('homepage:index')

def resetpassword(request):
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'tuyethuynh2k31@gmail.com',
    #     ['tuyethuynh3036@gmail.com'],
    #     fail_silently=False,
    # )
    return render(request, 'homepage/resetpassword.html')

def dashboard(request, id):
    path = 'HoatDong'
    user = User.objects.get(pk = id)
    account = Account.objects.get(username = id)
    userdetail = UserDetail.objects.get(accountid = account.pk)
    
    if request.method == 'POST': 
        avatar = request.FILES.get('avatar')
        account.avatar = tokenFile(avatar,'media/users', user.username ,1)
        account.save()
 
    ownlessonbadges = OwnLessonBadge.objects.filter(accountid = account)
    ownpracticebadges = OwnPracticeBadge.objects.filter(accountid = account)
    owncompetitionbadges = OwnCompetitionBadge.objects.filter(accountid = account)
    badges = len(ownlessonbadges) + len(ownpracticebadges) + len(owncompetitionbadges)

    context = {
        'user': user,
        'account': account,
        'userdetail': userdetail,
        'badges': badges,
        'path': path,
    }
    return render(request, 'homepage/dashboard.html', context)

def achievement(request):
    path = 'ThanhTuu'
    user = request.user
    account = Account.objects.get(username = user.pk)

    # change avatar
    if request.method == 'POST': 
        avatar = request.FILES.get('avatar')
        account.avatar = tokenFile(avatar,'media/users', user.username ,1)
        account.save()

    # practice badges
    ownpracticebadges = OwnPracticeBadge.objects.filter(accountid = account)
    practicebadges = []
    for i in ownpracticebadges:
        practicebadges.append(i.practicebadgeid)
    rest_practicebadges = 6 - len(practicebadges)
    for i in range(rest_practicebadges):
        practicebadges.append('lock')

    # lesson badges
    ownlessonbadges = OwnLessonBadge.objects.filter(accountid = account)
    lessonbadges = []
    for i in ownlessonbadges:
        lessonbadges.append(i.lessonbadgeid)
    rest_lessonbadges = 7 - len(lessonbadges)
    for i in range(rest_lessonbadges):
        lessonbadges.append('lock')

    # competition badges
    owncompetitionbadges = OwnCompetitionBadge.objects.filter(accountid = account)
    competitionbadges = []
    for i in owncompetitionbadges:
        competitionbadges.append(i.competitionbadgeid)

    context = {
        'user': user,
        'account': account,
        'practicebadges': practicebadges,
        'lessonbadges': lessonbadges,
        'competitionbadges': competitionbadges,
        'path': path,
    }
    return render(request, 'homepage/achievement.html', context)

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data)|Q(username=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					plaintext = template.loader.get_template('homepage/password_message.txt')
					htmltemp = template.loader.get_template('homepage/password_message.html')
					c = { 
                        "email": user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'SmartTying',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
					}
					text_content = plaintext.render(c)
					html_content = htmltemp.render(c)
					try:
						msg = EmailMultiAlternatives(subject, text_content, '', [user.email], headers = {'Reply-To': 'admin@example.com'})
						msg.attach_alternative(html_content, "text/html")
						msg.send()
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.info(request, "Password reset instructions have been sent to the email address entered.")
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="homepage/password_reset.html", context={"password_reset_form":password_reset_form})

# lessons
def lesson(request):
    topiclessons = {}
    topics = TopicLesson.objects.filter(isenable = 1).order_by('topicorder')
    for i in topics:
        topiclessons[i] = Lesson.objects.filter(topiclessonid=i)
    context = {
        'topiclessons': topiclessons,
    }

    # dang nhap -> ktra tracking theo user, lesson -> dung filter trackingactivity

    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

        # tracking theo lesson -> thanh tien do lesson hoac mo khoa lesson on tap trong chu de do
        # tracking theo chu de -> mo khoa chu de tiep theo

        previous_topic = 0
        for topic in topiclessons:
            # tracking by topic -> 3/4 topic -> unlock next topic
            topic_tracking = TrackingActivity.objects.filter(accountid = account, topiclessonid__topicorder = topic.topicorder - 1)
            
            if len(topic_tracking) >= previous_topic or topic.topicorder <= 2:
                topic.lock = False
                previous_topic = int(len(topiclessons[topic])*0.75)

                # for lesson in lessons:
                for lesson in topiclessons[topic]: 
                    activities = Activity.objects.filter(lessonid = lesson)
                    tracking = TrackingActivity.objects.filter(accountid = account, lessonid = lesson)
                    if len(tracking) != 0:
                        lesson.percent = int(len(tracking)/len(activities)*100)
                    else:
                        lesson.percent = 0

                # badge
                if topic.topicorder > 1:
                    topic_activities = Activity.objects.filter(topiclessonid = topic)
                    topic_activities_tracking = TrackingActivity.objects.filter(accountid = account, topiclessonid = topic)
                    if (len(topic_activities) == len(topic_activities_tracking)):
                        badge = LessonBadge.objects.get(topiclessonid = topic)
                        has_badge = OwnLessonBadge.objects.filter(accountid = account, lessonbadgeid = badge)
                        if len(has_badge) == 0:
                            new_own_badge = OwnLessonBadge(accountid = account, lessonbadgeid = badge)
                            new_own_badge.save()
                        topic.has_badge = True
                        # print(topic.topicorder, len(topic_activities), len(topic_activities_tracking))
                    else:
                        topic.has_badge = False
                else:
                    topic.has_badge = False   
            else:
                topic.lock = True
                for lesson in topiclessons[topic]: 
                    lesson.percent = 0
    else:
        for topic in topiclessons:
            for lesson in topiclessons[topic]: 
                lesson.percent = 0

    return render(request, 'homepage/lesson.html', context)

def lessondetail(request, id1, id2):
    topiclesson = TopicLesson.objects.get(pk=id1)
    lesson = Lesson.objects.get(pk=id2)
    activities = Activity.objects.filter(lessonid=id2).order_by('activityorder')
    context = {}
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account
        
        # tracking lessson
        tracking = TrackingActivity.objects.filter(accountid = account, lessonid = lesson)
        if len(tracking) != 0:
            lesson.percent = int(len(tracking)/len(activities)*100)
        else:
            lesson.percent = 0

        # tracking activity
        for activity in activities:
            tracking_activity = TrackingActivity.objects.filter(accountid = account, activityid = activity)
            if len(tracking_activity) != 0:
                activity.set_stars = True
            else:
                activity.set_stars = False
    else:
        lesson.percent = 0
        for activity in activities:
            activity.set_stars = False

    context.update({
        'topiclesson': topiclesson,
        'lesson': lesson,
        'activities': activities,
    })
    return render(request, 'homepage/lessondetail.html', context)

def activitydetail(request, id1, id2, id3):
    topiclesson = TopicLesson.objects.get(pk=id1)
    lesson = Lesson.objects.get(pk=id2)    
    activity = Activity.objects.get(activityid=id3)

    # id instruction video
    activity_order = activity.activityorder
    video = {
        1: 'mlAY5oR5Q7Q',
        2: 'WN0E5rgvmIA',
        3: 'vvqAAXLfuig',
        4: '6CXmIMIsBgA',
        5: 'fClo5beoTII',
    }

    context = {
        'topiclesson': topiclesson,
        'lesson': lesson,
        'activity': activity,
        'video': video[activity_order],
    }
    return render(request, 'homepage/activitydetail.html', context)

# game practices
def practice(request):
    context = {}
    topicpractices = {}
    
    for i in TopicPractice.objects.all():
        topicpractices[i] = Game.objects.filter(topicpracticeid=i)

    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account
        
        tracking = []

        sum_tracks_topic = len(GameLevel.objects.filter(topicpracticeid = 1))
        tracking_topic = len(TrackingLevelGame.objects.filter(accountid = account, topicpracticeid = 1))

        for i in topicpractices:
            tracking.append(TrackingLevelGame.objects.filter(accountid = account, topicpracticeid = i))
            order = i.topicorder

            if sum_tracks_topic == tracking_topic:
                for game in topicpractices[i]:
                    game.lock = False
            else:
                for game in topicpractices[i]:
                    game.lock = True
            sum_tracks_topic = len(GameLevel.objects.filter(topicpracticeid = i))
            tracking_topic = len(TrackingLevelGame.objects.filter(accountid = account, topicpracticeid = i))
            # print(sum_tracks_topic, tracking_topic)

            for game in topicpractices[i]:
                if order == 1:  # topic 1
                    game.lock = False
                # check star to set practicebadge
                stars = len(GameLevel.objects.filter(gameid = game)) * 3
                tracking_games = TrackingLevelGame.objects.filter(accountid = account, gameid = game)
                tracking_stars = 0
                for i in tracking_games:
                    tracking_stars += i.stars
                if tracking_stars == stars:
                    # set new practice if user does not have badge
                    badge = PracticeBadge.objects.get(gameid = game)
                    has_badge = OwnPracticeBadge.objects.filter(accountid = account, practicebadgeid = badge)
                    # print('no badge')
                    if len(has_badge) == 0:
                        new_own_badge = OwnPracticeBadge(accountid = account, practicebadgeid = badge)
                        new_own_badge.save()
                    else:
                        game.has_badge = True
                        # print(tracking_stars, stars)

    context.update({
        'topicpractices': topicpractices,
    })
    return render(request, 'homepage/practice.html', context)

def practicelevel(request, id):
    context = {}
    game = Game.objects.get(pk=id)
    levels = GameLevel.objects.filter(gameid=id).order_by('levelorder')
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)

        tracking = TrackingLevelGame.objects.filter(accountid = account, gameid = game)
        level_tracking = []
        star = []
        for i in tracking:
            level_tracking.append(i.levelid)
            star.append(i.stars)

        # check lock level
        for level in levels:
            if level.levelorder == 1:
                level.lock = False
            else:
                level.lock = True

        for i in range(len(levels) - 1):
            if levels[i] in level_tracking and star[i] == 3:
                levels[i+1].lock = False

        # check if level has tracking
        for level in levels:
            if level in level_tracking:
                stars = tracking.get(levelid = level).stars
                new_link = level.image.split('.')
                level.image = new_link[0] + '_' + str(stars) + '.' + new_link[1]
            elif level.lock:
                new_link = level.image.split('.')
                if level.levelorder != 1:
                    level.image = new_link[0] + '_' + '0' + '.' + new_link[1]
                else:
                    level.lock = False
                    level.image = new_link[0] + '.' + new_link[1]

        context['account'] = account
    else:
        if game.gameorder == 1:
            for level in levels:
                level.lock = False

    context.update({
        'game': game,
        'levels': levels,
    })
    return render(request, 'homepage/practicelevel.html', context)

def practicedetail(request, id1, id2):
    game = Game.objects.get(pk=id1)
    level = GameLevel.objects.get(pk=id2)
    
    # id instruction video
    game_order = game.gameorder
    video = {
        1: '1w0GZKELfJI',
        2: 'YWjg8vcIzq4',
        3: 'V0AOwLM3y9w',
        4: 'wyglDv7il8Q',
        5: 'K1LEgCoAd0U',
        6: 'ERQDfPlU0qs',
    }

    hidemenu = True
    context = {
        'game': game,
        'level': level,
        'video': video[game_order],
    }
    return render(request, 'homepage/practicedetail.html', context)

# test
def test(request):
    # timetest = TimeTest.objects.all()
    timetest1 = TimeTest.objects.filter(isenable = 1)[:3]
    timetest2 = TimeTest.objects.filter(isenable = 1)[3:]
    contenttest = ContentTest.objects.all()
    context = {
        'timetest1': timetest1,
        'timetest2': timetest2,
        'contenttest': contenttest,
    }

    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    return render(request, 'homepage/test.html', context)

def timetestdetail(request, id):
    test = TimeTest.objects.get(pk=id)
    context = {
        'test': test,
    }

    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account
        
    return render(request, 'homepage/timetestdetail.html', context)

def contenttestdetail(request, id):
    test = ContentTest.objects.get(pk=id)
    print(test.link)
    context = {
        'test': test,
    }
    return render(request, 'homepage/contenttestdetail.html', context)

# competition
def competition(request):
    # get all competitions
    competitions = Competition.objects.filter(isenable=1).order_by('startdate')

    # get top 4 of latest competition
    current_competition = Competition.objects.get(startdate__month = datetime.datetime.now().month, startdate__year = datetime.datetime.now().year)
    top_examiners = TrackingCompetition.objects.filter(competitionid = current_competition).order_by('-score', 'timedone')[:4]
    examiners = []
    for i in top_examiners:
        account = Account.objects.get(pk = i.accountid.pk)
        account.score = i.score
        examiners.append(account)
    while len(examiners) < 4:
        examiners.append('?')

    context = {
        'competitions': competitions,
        'time': datetime.datetime.now(),
        'examiners': examiners,
        'examiner1': examiners[0],
        'examiner2': examiners[1],
        'examiner3': examiners[2],
        'examiner4': examiners[3],
    }
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

        # competition badge
        for competition in competitions:
            badge = CompetitionBadge.objects.get(competitionid = competition)
            print(badge)
            has_badge = OwnCompetitionBadge.objects.filter(accountid = account, competitionbadgeid = badge)
            if len(has_badge) == 0:
                competition.badge = False
            else:
                competition.badge = badge

    return render(request, 'homepage/competition.html', context)

def competitiondetail(request, id):
    competition = Competition.objects.get(pk=id)
    context = {
        'competition': competition,
    }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    return render(request, 'homepage/competitiondetail.html', context)

def news(request):
    news = News.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        posts=News.objects.filter(title__icontains=q)
    else:
        posts=News.objects.all().order_by("-createdate")
    # Pagintion
    paginator=Paginator(posts,12)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    context = {
       # 'blogcategorylist': blogcategorylist,
        'page_obj':page_obj,
        'news': news,        
    }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account
    
    return render(request, 'homepage/news.html', context)

def newsdetail(request, id):
    news = News.objects.get(pk=id)
    context = {
        'news': news
    }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    return render(request, 'homepage/newsdetail.html', context)

def document(request):
    context = {}

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    documents = Document.objects.all()
    categories = DocCategory.objects.all()

    if 'q' in request.GET:
        q=request.GET['q']
        posts=Document.objects.filter(title__icontains=q)
    else:
        posts=Document.objects.all().order_by("-createdate")
    # Pagintion
    paginator=Paginator(posts, 10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context.update({
        'page_obj':page_obj,
        'documents': documents,
        'categories': categories,
    }) 

    return render(request, 'homepage/document.html', context)

def docdetail(request, id):
    document = Document.objects.get(pk=id)
    context = {
        'document': document
    }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account
        
    return render(request, 'homepage/docdetail.html', context)

def faq(request):
    questions = FAQ.objects.all()
    context = {
        'questions':questions,
    }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    return render(request, 'homepage/faq.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['messages']
            date = timezone.now()
            obj = Contact()
            obj.date = date
            obj.name = name
            obj.email = email
            obj.messages = message
            obj.save()
            contact ={
                'message': 'Cảm ơn phản hồi của bạn'}
            return render(request,'homepage/index.html',contact)
    context = {'form' :form }

    if request.user.is_authenticated:
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        context['account'] = account

    return render(request,'homepage/contact.html',context)