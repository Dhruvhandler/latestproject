from django.contrib import admin
from DataApp.models import Person
from DataApp.models import category
from DataApp.models import structure
from DataApp.models import article
from DataApp.models import initiative
from DataApp.models import video
from DataApp.models import faq
from DataApp.models import contactus
from DataApp.models import helpnsupport
from DataApp.models import userregister
from DataApp.models import ChatMessage
from DataApp.models import jobsearch


#from Dataapp.models import review

# Register your models here.
admin.site.register(Person)
admin.site.register(category)
admin.site.register(structure)
admin.site.register(article)
admin.site.register(initiative)
admin.site.register(video)
admin.site.register(faq)
admin.site.register(contactus)
admin.site.register(userregister)
admin.site.register(ChatMessage)
admin.site.register(helpnsupport)
admin.site.register(jobsearch)
#admin.site.register(review)


