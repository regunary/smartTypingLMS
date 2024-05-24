from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from homepage.models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

def ajaxtrackcompleteactivity(request):
    flag = True
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        topiclessonid = request.GET.get('topiclessonid')
        lessonid = request.GET.get('lessonid')
        activityid = request.GET.get('activityid')
        
        # Cộng 10 điểm kinh nghiệm
        account.experience += 100

        # Xét danh hiệu
        current_callsign = CallSign.objects.get(callsignid = account.callsignid.pk).callsignorder
        if current_callsign != 6:   # Xét nếu không phải cấp bậc lớn nhất
            next_callsign = CallSign.objects.get(callsignorder = current_callsign + 1)
            if account.experience >= next_callsign.exrequired:
                account.callsignid = next_callsign

        account.save()

        tracking = TrackingActivity.objects.filter(accountid = account, activityid = activityid, topiclessonid = topiclessonid, lessonid = lessonid)
        if (len(tracking) == 0):
            print ('no tracking exist')
            new_tracking = TrackingActivity()
            new_tracking.accountid = account
            new_tracking.topiclessonid = TopicLesson.objects.get(pk = topiclessonid)
            new_tracking.lessonid = Lesson.objects.get(pk = lessonid)
            new_tracking.activityid = Activity.objects.get(pk = activityid)
            new_tracking.save()
        else:
            print ('tracking exist')

    data = {
        'flag': flag,
    }
    return JsonResponse(data)

def ajaxtrackcompletelevelgame(request):
    flag = True
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        gameid = request.GET.get('gameid')
        topicid = request.GET.get('topicid')
        levelid = request.GET.get('levelid')
        stars = request.GET.get('stars')

        print(stars)

        # Cộng 10 điểm kinh nghiệm
        account.experience += 10

        # Xét danh hiệu
        current_callsign = CallSign.objects.get(callsignid = account.callsignid.pk).callsignorder
        if current_callsign != 6:   # Xét nếu không phải cấp bậc lớn nhất
            next_callsign = CallSign.objects.get(callsignorder = current_callsign + 1)
            if account.experience >= next_callsign.exrequired:
                account.callsignid = next_callsign
        account.save()

        # Xét lưu vết
        # if tracking đã tồn tại -> ghi đè tracking -> how to check tracking was exist?
        # 1 tracking thuộc về 1 account và 1 game, 1 level (qhe 1-1)
        # 1 account có 1 tracking đối với 1 game -> need creat model trackinggame ?
        # 1 account có 1 tracking đối với 1 level game (1-1)
        # check if tracking exists
        tracking = TrackingLevelGame.objects.filter(accountid = account, gameid = gameid, levelid = levelid)
        if (len(tracking) != 0):
            print ('tracking exist')
            if int(stars) > tracking[0].stars:
                tracking[0].stars = int(stars)
            tracking[0].save()            
        # else create new tracking
        else:
            print ('no tracking exist')
            new_tracking = TrackingLevelGame()
            new_tracking.accountid = account
            new_tracking.gameid = Game.objects.get(pk = gameid)
            new_tracking.levelid = GameLevel.objects.get(pk = levelid)
            new_tracking.topicpracticeid = TopicPractice.objects.get(pk = topicid)
            new_tracking.stars = stars
            new_tracking.save()

    data = {
        'flag': flag,
    }
    return JsonResponse(data)

def ajaxtrackcompletecompetition(request):
    flag = True
    if request.user.is_authenticated: 
        current_user = request.user
        account = Account.objects.get(username = current_user.id)
        competitionid = request.GET.get('competitionid')
        score = request.GET.get('score')
        timedone = request.GET.get('sumtime')
        own_badge = request.GET.get('own_badge')
        # print(score, timedone)

        # Cộng 10 điểm kinh nghiệm
        account.experience += 10

        # Xét danh hiệu
        current_callsign = CallSign.objects.get(callsignid = account.callsignid.pk).callsignorder
        if current_callsign != 6:   # Xét nếu không phải cấp bậc lớn nhất
            next_callsign = CallSign.objects.get(callsignorder = current_callsign + 1)
            if account.experience >= next_callsign.exrequired:
                account.callsignid = next_callsign
        account.save()

        # Xét lưu vết
        # if tracking đã tồn tại -> so sánh và ghi đè tracking -> how to check tracking was exist?
        # 1 tracking thuộc về 1 account và 1 cuộc thi (qhe 1-1)
        # check if tracking exists
        tracking = TrackingCompetition.objects.filter(accountid = account, competitionid = competitionid)
        if (len(tracking) != 0):
            print ('tracking exist')
            if int(score) > tracking[0].score:
                tracking[0].score = int(score)
                tracking[0].timedone = int(timedone)
            elif int(score) == tracking[0].score and int(timedone) < tracking[0].timedone:
                tracking[0].timedone = int(timedone)
            tracking[0].save()            
        # else create new tracking
        else:
            print ('no tracking exist')
            new_tracking = TrackingCompetition()
            new_tracking.accountid = account
            new_tracking.competitionid = Competition.objects.get(pk = competitionid)
            new_tracking.score = score
            new_tracking.timedone = timedone
            new_tracking.save()

        # Xét sở hữu huy hiệu
        if own_badge:
            # Xét xem đã sở hữu huy hiệu chưa, nếu chưa thì tạo mới
            badge = CompetitionBadge.objects.get(competitionid = competitionid)
            owned_badge = OwnCompetitionBadge.objects.filter(accountid = account, competitionbadgeid = badge)
            if len(owned_badge) == 0:
                new_badge = OwnCompetitionBadge(accountid = account, competitionbadgeid = badge)
                new_badge.save()

    data = {
        'flag': flag,
    }
    return JsonResponse(data)

def ajaxtrackcompletetimetest(request):
    flag = True
    # if request.user.is_authenticated: 
        # current_user = request.user
        # account = Account.objects.get(username = current_user.id)
        # gameid = request.GET.get('gameid')
        # topicid = request.GET.get('topicid')
        # levelid = request.GET.get('levelid')
        # stars = request.GET.get('stars')

        # print(stars)

        # # Cộng 10 điểm kinh nghiệm
        # account.experience += 10

        # # Xét danh hiệu
        # current_callsign = CallSign.objects.get(callsignid = account.callsignid.pk).callsignorder
        # if current_callsign != 6:   # Xét nếu không phải cấp bậc lớn nhất
        #     next_callsign = CallSign.objects.get(callsignorder = current_callsign + 1)
        #     if account.experience >= next_callsign.exrequired:
        #         account.callsignid = next_callsign
        # account.save()

        # # Xét lưu vết
        # # if tracking đã tồn tại -> ghi đè tracking -> how to check tracking was exist?
        # # 1 tracking thuộc về 1 account và 1 game, 1 level (qhe 1-1)
        # # 1 account có 1 tracking đối với 1 game -> need creat model trackinggame ?
        # # 1 account có 1 tracking đối với 1 level game (1-1)
        # # check if tracking exists
        # tracking = TrackingLevelGame.objects.filter(accountid = account, gameid = gameid, levelid = levelid)
        # if (len(tracking) != 0):
        #     print ('tracking exist')
        #     if int(stars) > tracking[0].stars:
        #         tracking[0].stars = int(stars)
        #     tracking[0].save()            
        # # else create new tracking
        # else:
        #     print ('no tracking exist')
        #     new_tracking = TrackingLevelGame()
        #     new_tracking.accountid = account
        #     new_tracking.gameid = Game.objects.get(pk = gameid)
        #     new_tracking.levelid = GameLevel.objects.get(pk = levelid)
        #     new_tracking.topicpracticeid = TopicPractice.objects.get(pk = topicid)
        #     new_tracking.stars = stars
        #     new_tracking.save()

    data = {
        'flag': flag,
    }
    return JsonResponse(data)

def ajaxtrackcompletecontenttest(request):
    flag = True
    # if request.user.is_authenticated: 
        # current_user = request.user
        # account = Account.objects.get(username = current_user.id)
        # gameid = request.GET.get('gameid')
        # topicid = request.GET.get('topicid')
        # levelid = request.GET.get('levelid')
        # stars = request.GET.get('stars')

        # print(stars)

        # # Cộng 10 điểm kinh nghiệm
        # account.experience += 10

        # # Xét danh hiệu
        # current_callsign = CallSign.objects.get(callsignid = account.callsignid.pk).callsignorder
        # if current_callsign != 6:   # Xét nếu không phải cấp bậc lớn nhất
        #     next_callsign = CallSign.objects.get(callsignorder = current_callsign + 1)
        #     if account.experience >= next_callsign.exrequired:
        #         account.callsignid = next_callsign
        # account.save()

        # # Xét lưu vết
        # # if tracking đã tồn tại -> ghi đè tracking -> how to check tracking was exist?
        # # 1 tracking thuộc về 1 account và 1 game, 1 level (qhe 1-1)
        # # 1 account có 1 tracking đối với 1 game -> need creat model trackinggame ?
        # # 1 account có 1 tracking đối với 1 level game (1-1)
        # # check if tracking exists
        # tracking = TrackingLevelGame.objects.filter(accountid = account, gameid = gameid, levelid = levelid)
        # if (len(tracking) != 0):
        #     print ('tracking exist')
        #     if int(stars) > tracking[0].stars:
        #         tracking[0].stars = int(stars)
        #     tracking[0].save()            
        # # else create new tracking
        # else:
        #     print ('no tracking exist')
        #     new_tracking = TrackingLevelGame()
        #     new_tracking.accountid = account
        #     new_tracking.gameid = Game.objects.get(pk = gameid)
        #     new_tracking.levelid = GameLevel.objects.get(pk = levelid)
        #     new_tracking.topicpracticeid = TopicPractice.objects.get(pk = topicid)
        #     new_tracking.stars = stars
        #     new_tracking.save()

    data = {
        'flag': flag,
    }
    return JsonResponse(data)