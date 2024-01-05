from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db, dao
from app.models import LoaiPhong, Phong
from flask_login import logout_user, current_user
from flask import redirect
from app.models import UserRoleEnum



admin = Admin(app=app, name='KHÁCH SẠN MÂY TRẮNG', template_mode='bootstrap4')


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated



class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyProductView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    can_export = True
    can_view_details = True


    def is_accessible(self):
        return current_user.is_authenticated



class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']

class MyStatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')



class MyLogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


    
admin.add_view(MyCategoryView(LoaiPhong, db.session))
admin.add_view(MyProductView(Phong, db.session))
admin.add_view(MyStatsView(name='Thong Ke Bao Cao'))
admin.add_view(MyLogoutView(name='Dang Xuat'))