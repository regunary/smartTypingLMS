from django.contrib import admin
from .models import *

# General system
@admin.register(CallSign)
class CallSignAdmin(admin.ModelAdmin):
    list_display = ('callsignid', 'callsignorder', 'name', 'frame' , 'exrequired')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('accountid', 'username', 'experience', 'callsignid')

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('userdetailid', 'lastname', 'firstname', 'phone', 'email', 'accountid')

# Module 1
@admin.register(TopicLesson)
class TopicLessonAdmin(admin.ModelAdmin):
    list_display = ('topiclessonid', 'topicorder', 'name')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lessonid', 'lessonorder', 'name', 'topiclessonid')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activityid', 'activityorder', 'name', 'lessonid', 'topiclessonid')

@admin.register(TrackingActivity)
class TrackingActivityAdmin(admin.ModelAdmin):
    list_display = ('trackingactivityid', 'accountid', 'topiclessonid', 'lessonid', 'activityid')

@admin.register(LessonBadge)
class LessonBadgeAdmin(admin.ModelAdmin):
    list_display = ('lessonbadgeid', 'name', 'topiclessonid')

@admin.register(OwnLessonBadge)
class OwnLessonBadgeAdmin(admin.ModelAdmin):
    list_display = ('ownlessonbadgeid', 'accountid', 'lessonbadgeid')

# Module 2
@admin.register(TopicPractice)
class TopicPracticeAdmin(admin.ModelAdmin):
    list_display = ('topicpracticeid', 'topicorder', 'name')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('gameid', 'gameorder', 'name', 'topicpracticeid')

@admin.register(GameLevel)
class GameLevelAdmin(admin.ModelAdmin):
    list_display = ('levelid', 'levelorder', 'name', 'link', 'gameid', 'topicpracticeid')

@admin.register(TrackingLevelGame)
class TrackingLevelGameAdmin(admin.ModelAdmin):
    list_display = ('trackinglevelid', 'stars', 'accountid', 'topicpracticeid', 'gameid', 'levelid')

@admin.register(PracticeBadge)
class PracticeBadgeAdmin(admin.ModelAdmin):
    list_display = ('practicebadgeid', 'name', 'gameid')

@admin.register(OwnPracticeBadge)
class OwnPracticeBadgeAdmin(admin.ModelAdmin):
    list_display = ('ownpracticebadgeid', 'accountid', 'practicebadgeid')

# Module 3
@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('competitionid', 'name', 'startdate', 'enddate', 'link')

@admin.register(TrackingCompetition)
class TrackingCompetitionAdmin(admin.ModelAdmin):
    list_display = ('trackingcompetitionid', 'score', 'timedone', 'accountid', 'competitionid')

@admin.register(CompetitionBadge)
class CompetitionBadgeAdmin(admin.ModelAdmin):
    list_display = ('competitionbadgeid', 'name', 'competitionid')

@admin.register(OwnCompetitionBadge)
class OwnCompetitionBadgeAdmin(admin.ModelAdmin):
    list_display = ('ownlcompbadgeid', 'accountid', 'competitionbadgeid')

@admin.register(TimeTest)
class TimeTestAdmin(admin.ModelAdmin):
    list_display = ('timetestid', 'name', 'time', 'link')

@admin.register(ContentTest)
class ContentTestAdmin(admin.ModelAdmin):
    list_display = ('contenttestid', 'name', 'link')

@admin.register(TrackingTimeTest)
class TrackingTimeTestAdmin(admin.ModelAdmin):
    list_display = ('trackingtimetestid', 'max_wpm', 'max_cpm', 'accountid', 'timetestid')

@admin.register(TrackingContentTest)
class TrackingContentTestAdmin(admin.ModelAdmin):
    list_display = ('trackingcontenttestid', 'max_wpm', 'max_cpm', 'accountid', 'contenttestid')

# Module 4
@admin.register(DocCategory)
class DocCategoryAdmin(admin.ModelAdmin):
    list_display = ('doccategoryid', 'name')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('documentid', 'title', 'pdf', 'doccategoryid')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('newsid', 'title', 'author')
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('faqid', 'question', 'answer')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contactid', 'fullname', 'email', 'status')