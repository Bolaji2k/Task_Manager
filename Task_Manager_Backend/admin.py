from flask_admin import Admin
from  flask_admin.contrib.sqla import ModelView

from .models import Task, db

admin = Admin(name='Task Manager',template_mode='bootstrap3')
    
admin.add_view(ModelView(Task, db.session))
