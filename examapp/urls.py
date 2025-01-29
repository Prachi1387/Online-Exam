from django.urls import path

from . import views

urlpatterns=[

    path('search/<pageno>',views.search),
    
    path('giveMePage1/',views.giveMePage1),

    path('giveMePage2/',views.giveMePage2),

    path('giveMePage3/',views.giveMePage3),


    path('startTest/',views.startTest),

    path('nextQuestion/',views.nextQuestion),

    path('previousQuestion/',views.previousQuestion),

    path('endexam/',views.endexam),

    path('addQuestion/',views.addQuestion),
    path('viewQuestion/',views.viewQuestion),
    path('updateQuestion/',views.updateQuestion),
    path('deleteQuestion/',views.deleteQuestion)
    

]