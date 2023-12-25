from django.contrib import admin

# Register your models here.

from .models import *
from .client_models import *

admin.site.register(Cities)

admin.site.register(Nationalities)

admin.site.register(Specializations)

admin.site.register(Clients)

admin.site.register(Client_Courses)

admin.site.register(Client_Educations)

admin.site.register(Client_Experiences)

admin.site.register(Client_Skills)

admin.site.register(Jobs)

admin.site.register(Job_Applied)

admin.site.register(Partners)

admin.site.register(Client_CV)

admin.site.register(Client_CV_Courses)

admin.site.register(Client_CV_Educations)

admin.site.register(Client_CV_Experiences)

admin.site.register(Client_CV_Skills)