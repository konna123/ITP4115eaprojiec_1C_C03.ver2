from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, JobPost, JobPostCategory, User, UserRole
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from wtforms.fields import DateTimeField

from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)
    


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']
# New ModelViews
class JobPostView(ModelView):
    datamodel = SQLAInterface(JobPost)
    list_columns = ['title', 'description', 'date_posted', 'jobpost_category.name']

class JobPostCategoryView(ModelView):
    datamodel = SQLAInterface(JobPostCategory)
    list_columns = ['name']

class UserView(ModelView):
    datamodel = SQLAInterface(User)
    list_columns = ['username', 'email', 'user_role.name']

class UserRoleView(ModelView):
    datamodel = SQLAInterface(UserRole)
    list_columns = ['name']

# ...

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = '新聞頻道'
        self.update_redirect()
        return self.render_template('news3.html', param1 = param1)

    @expose('/instant_news/')
    def instant_news(self):
        param1 = '即時財經主页'
        self.update_redirect()
        return self.render_template('news1.html',  param1=param1)
        
    @expose('/global_news/')
    def global_news(self):
        param1 = '國際'
        self.update_redirect()
        return self.render_template('news2.html', param1=param1)
        
    @expose('/test1_news/')
    def test1_news(self):
        param1 = '「香港經濟日報企業大獎」　匯聚各界優秀企業　齊心同創新機遇' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news.html', param1=param1, date=datetime)
    @expose('/test2_news/')
    def test2_news(self):
        param1 = '【港股市況】騰訊午後曾跌3%　車股個別發展　恒生指數跌逾200點（不斷更新）' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news10.html', param1=param1, date=datetime)
    @expose('/test3_news/')
    def test3_news(self):
        param1 = '筲箕灣規劃 百年阿公岩村擬清拆重建 房屋署擬建成1500伙公營房屋' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news11.html', param1=param1, date=datetime)
    @expose('/test4_news/')
    def test4_news(self):
        param1 = '【名人家居】單身貴族張可頤家中開十人派對 元朗獨立屋擁私人花園BBQ' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news12.html', param1=param1, date=datetime)
    @expose('/test5_news/')
    def test5_news(self):
        param1 = '【俄烏戰爭】洩密文件爆烏軍圖襲莫斯科 遭美國阻止' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news13.html', param1=param1, date=datetime)
    @expose('/test6_news/')
    def test6_news(self):
        param1 = '【俄烏戰爭】俄徵「真男人」入伍 收入為俄平均月薪四倍起跳' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news14.html', param1=param1, date=datetime)
    @expose('/test7_news/')
    def test7_news(self):
        param1 = '【新股IPO】綠竹生物2480怡俊集團2442首日孖展　均未足額認購' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news15.html', param1=param1, date=datetime)
    @expose('/test8_news/')
    def test8_news(self):
        param1 = '「哥哥迷」炮製地產新潮文 大玩「風繼續吹」歌詞勁生鬼' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news16.html', param1=param1, date=datetime)
    @expose('/test9_news/')
    def test9_news(self):
        param1 = '【騰訊700】騰訊據報加快海外投資遊戲資產的步伐　以減低對中國地區的倚賴' 
        datetime = '2023/4/22'
        self.update_redirect()
        return self.render_template('news17.html', param1=param1, date=datetime)


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'local_news', category="News")
appbuilder.add_link("財經", href="/newspageview/instant_news/", category="")
appbuilder.add_link("即時新聞", href="/newspageview/local_news/", category="")
appbuilder.add_link("國際", href="/newspageview/global_news/", category="")
""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
# Add the new views to AppBuilder
appbuilder.add_view(JobPostView, "JobPost", icon="fa-briefcase", category="Admin")
appbuilder.add_view(JobPostCategoryView, "JobPostCategory", icon="fa-tags", category="Admin")
appbuilder.add_view(UserView, "User", icon="fa-user", category="Admin")
appbuilder.add_view(UserRoleView, "UserRole", icon="fa-users-cog", category="Admin")

