from django.urls import path
from homepage import views
from homepage import ajax
from django.contrib.auth import views as auth_views
app_name = 'homepage'

urlpatterns = [
    # giới thiệu
    path('', views.index, name='index'),
    path('gioi-thieu', views.about, name='about'),
    path('xem-them', views.aboutbee, name="aboutbee"),

    # dang ky - dang nhap - trang ca nhan
    path('dang-ki', views.myregister, name='register'),
    path('dang-nhap',  views.mylogin, name="login"),
    path('dang-xuat', views.mylogout, name="logout"),
    path('trang-ca-nhan/<int:id>', views.dashboard, name='dashboard'),
    path('cap-nhat-thong-tin-ca-nhan', views.updateinfo, name='updateinfo'),
    path('thanh-tuu', views.achievement, name='achievement'),

    # path('reset_password/',
    #  auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    #  name="reset_password"),

    # path('reset_password_sent/', 
    #     auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
    #     name="password_reset_done"),

    # path('reset/<uidb64>/<token>/',
    #  auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
    #  name="password_reset_confirm"),

    # path('reset_password_complete/', 
    #     auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
    #     name="password_reset_complete"),

    # bài học
    path('danh-sach-bai-hoc', views.lesson, name='lesson'),
    path('chu-de-bai-hoc-<int:id1>/bai-hoc-<int:id2>', views.lessondetail, name='lessondetail'),
    path('chu-de-bai-hoc-<int:id1>/bai-hoc-<int:id2>/hoat-dong-<int:id3>', views.activitydetail, name='activitydetail'),
    path('ajaxtrackcompleteactivity', ajax.ajaxtrackcompleteactivity, name="ajaxtrackcompleteactivity"),

    # game luyện tập
    path('luyen-tap', views.practice, name="practice"),
    path('luyen-tap/tro-choi-<int:id>', views.practicelevel, name="practicelevel"),
    path('luyen-tap/tro-choi-<int:id1>/level-<int:id2>', views.practicedetail, name="practicedetail"),
    path('ajaxtrackcompletelevelgame', ajax.ajaxtrackcompletelevelgame, name="ajaxtrackcompletelevelgame"),

    # kiểm tra - cuộc thi
    path('kiem-tra', views.test, name="test"),
    path('kiem-tra-thoi-gian/<int:id>', views.timetestdetail, name="timetestdetail"),
    path('kiem-tra-van-ban/<int:id>', views.contenttestdetail, name="contenttestdetail"),
    path('ajaxtrackcompletetimetest', ajax.ajaxtrackcompletetimetest, name="ajaxtrackcompletetimetest"),
    path('ajaxtrackcompletecontenttest', ajax.ajaxtrackcompletecontenttest, name="ajaxtrackcompletecontenttest"),

    path('cuoc-thi', views.competition, name="competition"),
    path('cuoc-thi-dinh-ky/<int:id>', views.competitiondetail, name="competitiondetail"),
    path('ajaxtrackcompletecompetition', ajax.ajaxtrackcompletecompetition, name="ajaxtrackcompletecompetition"),
    
    # tin tức - tài liệu
    path('tin-tuc', views.news, name='news'),
    path('tin-tuc-<int:id>', views.newsdetail, name='newsdetail'),
    path('tai-lieu', views.document, name='document'),
    path('tai-lieu-<int:id>', views.docdetail, name='docdetail'),

    # hỗ trợ
    path('cau-hoi-thuong-gap', views.faq, name='faq'),
    path('lien-he', views.contact, name='contact'),
]
