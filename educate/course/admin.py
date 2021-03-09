from django.contrib import admin
from .models import Course,Topic,Lesson,WhatWillYouLearn,WhatToKnow, ContentType

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(WhatWillYouLearn)
admin.site.register(WhatToKnow)
admin.site.register(ContentType)
