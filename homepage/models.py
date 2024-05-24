from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField, EmailField
from django.db.models.query import FlatValuesListIterable
from django.http import request
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class CallSign(models.Model):
    callsignid = models.AutoField(primary_key=True)
    callsignorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    frame = models.CharField(max_length=250, null=True)
    exrequired = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'CallSign'

class Account(models.Model):
    accountid = models.AutoField(primary_key=True)
    callsignid = models.ForeignKey(CallSign, on_delete=models.CASCADE, blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    avatar = models.CharField(max_length=250, null=True)
    experience = models.IntegerField(default=0, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.username
    
    class Meta:
        managed = True
        db_table = 'Account'

class UserDetail(models.Model):
    userdetailid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    lastname = models.CharField(max_length=10, blank=True, null=True)
    firstname = models.CharField(max_length=10, blank=True, null=True)
    yearofbirth = models.IntegerField(default=0, blank=True, null=True)
    userobject = models.CharField(max_length=10, blank=True, null=True)
    grade = models.IntegerField(default=0, blank=True, null=True)
    guardian = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    # def __str__(self):
    #     return self.username
    
    class Meta:
        managed = True
        db_table = 'UserDetail'

# Module 1

class TopicLesson(models.Model):
    topiclessonid = models.AutoField(primary_key=True)
    topicorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        managed = True
        db_table = 'TopicLesson'

class Lesson(models.Model):
    lessonid = models.AutoField(primary_key=True)
    topiclessonid = models.ForeignKey(TopicLesson, on_delete=models.CASCADE, blank=True, null=True)
    lessonorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    # tracking = models.ManyToManyField(Account)

    def __str__(self):
        return self.name 
    
    class Meta:
        managed = True
        db_table = 'Lesson'

class Activity(models.Model):
    activityid = models.AutoField(primary_key=True)
    topiclessonid = models.ForeignKey(TopicLesson, on_delete=models.CASCADE, blank=True, null=True)
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    activityorder = models.IntegerField(blank=True, null=True)
    name  = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        managed = True
        db_table = 'Activity'

class TrackingActivity(models.Model):
    trackingactivityid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    topiclessonid = models.ForeignKey(TopicLesson, on_delete=models.CASCADE, blank=True, null=True)
    lessonid = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    activityid = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'TrackingActivity'

class LessonBadge(models.Model):
    lessonbadgeid = models.AutoField(primary_key=True)
    topiclessonid = models.ForeignKey(TopicLesson, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'LessonBadge'

class OwnLessonBadge(models.Model):
    ownlessonbadgeid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    lessonbadgeid = models.ForeignKey(LessonBadge, on_delete=models.CASCADE, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'OwnLessonBadge'

# Module 2

class TopicPractice(models.Model):
    topicpracticeid = models.AutoField(primary_key=True)
    topicorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        managed = True
        db_table = 'TopicPractice'

class Game(models.Model):
    gameid = models.AutoField(primary_key=True)
    topicpracticeid = models.ForeignKey(TopicPractice, on_delete=models.CASCADE, blank=True, null=True)
    gameorder = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Game'

class GameLevel(models.Model):
    levelid = models.AutoField(primary_key=True)
    topicpracticeid = models.ForeignKey(TopicPractice, on_delete=models.CASCADE, blank=True, null=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    levelorder = models.IntegerField(blank=True, null=True)
    name = models.TextField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    stars = models.IntegerField(default = 3, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'GameLevel'

class TrackingLevelGame(models.Model):
    trackinglevelid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    topicpracticeid = models.ForeignKey(TopicPractice, on_delete=models.CASCADE, blank=True, null=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    levelid = models.ForeignKey(GameLevel, on_delete=models.CASCADE, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'TrackingLevelGame'

class PracticeBadge(models.Model):
    practicebadgeid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'PracticeBadge'

class OwnPracticeBadge(models.Model):
    ownpracticebadgeid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    practicebadgeid = models.ForeignKey(PracticeBadge, on_delete=models.CASCADE, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'OwnPracticeBadge'

# Module 3

class Competition(models.Model):
    competitionid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'Competition'

class TrackingCompetition(models.Model):
    trackingcompetitionid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    competitionid = models.ForeignKey(Competition, on_delete=models.CASCADE, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    timedone = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'TrackingCompetition'

class CompetitionBadge(models.Model):
    competitionbadgeid = models.AutoField(primary_key=True)
    competitionid = models.ForeignKey(Competition, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    logo = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'CompetitionBadge'

class OwnCompetitionBadge(models.Model):
    ownlcompbadgeid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    competitionbadgeid = models.ForeignKey(CompetitionBadge, on_delete=models.CASCADE, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'OwnCompetitionBadge'

class TimeTest(models.Model):
    timetestid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'TimeTest'

class ContentTest(models.Model):
    contenttestid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'ContentTest'

class TrackingTimeTest(models.Model):
    trackingtimetestid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    timetestid = models.ForeignKey(TimeTest, on_delete=models.CASCADE, blank=True, null=True)
    max_wpm = models.IntegerField(blank=True, null=True)
    max_cpm = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'TrackingTimeTest'

class TrackingContentTest(models.Model):
    trackingcontenttestid = models.AutoField(primary_key=True)
    accountid = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    contenttestid = models.ForeignKey(ContentTest, on_delete=models.CASCADE, blank=True, null=True)
    max_wpm = models.IntegerField(blank=True, null=True)
    max_cpm = models.IntegerField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'TrackingContentTest'

# Module 4

class DocCategory(models.Model):
    doccategoryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'DocCategory'

class Document(models.Model):
    documentid = models.AutoField(primary_key=True)
    doccategoryid = models.ForeignKey(DocCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = RichTextUploadingField()
    author = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    pdf = models.CharField(max_length=250, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        db_table = 'Document'

class News(models.Model):
    newsid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    # author là khóa ngoại liên kết đến account
    author = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        db_table = 'News'

class FAQ(models.Model):
    faqid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250)
    answer = models.TextField(blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question
    
    class Meta:
        managed = True
        db_table = 'FAQ'

STATUS_CONTACT = (
    ('WAIT', 'CHỜ XỬ LÝ'),
    ('SPAM', 'SPAM'),
    ('COMPLETED', 'HOÀN TẤT')
)

class Contact(models.Model):
    contactid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True) 
    phone = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(choices=STATUS_CONTACT,default='WAIT', max_length=50, blank=True, null=True)
    createdate  = models.DateField(auto_now_add=True, blank=True, null=True)
    editdate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isenable = models.BooleanField(default=True, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.contactid
    
    class Meta:
        managed = True
        db_table = 'Contact'