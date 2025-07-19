from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import re
from kivymd.uix.card import MDCardSwipe
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sqlite3
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime, timedelta, date
from kivy.config import Config
#Config.set('graphics', 'fullscreen', 'auto')
Window.size = (450, 780)
helpstr = '''
ScreenManager:  
    SplashScreen:
    LoginScreen:
    SignupScreen:
    TodoTaskScreen:
<SplashScreen>
    name: "pre-splash"
    MDFloatLayout:
        md_bg_color: 226/255, 0, 48/255, 1
        Image:
            source: "assets/logo.png"
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5,'center_y': 0.55}
            canvas.before:
                Color:
                    rgb: 1,1,1,1
<LoginScreen>
    name: "loginscreen"
    MDFloatLayout:
        md_bg_color: 226/255, 0, 48/255, 1
        
        Image:
            source: "assets/logo.png"
            size_hint: 0.7, 0.7
            pos_hint: {'center_x': 0.22,'center_y': 0.82}
        
        MDLabel:
            text: "Please Enter your credentials to"
            font_size: "18sp"
            color: 1,1,1,1
            pos_hint: {'center_x': .6,'center_y': 0.65}
        MDLabel:
            text: "Login"
            font_size: "28sp"
            bold: True
            color: 1,1,1,1
            pos_hint: {'center_x': .6,'center_y': 0.58}
        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {'center_x': 0.5,'center_y': 0.42}
            MDLabel:
                text: "Username"
                font_size: "14sp"
                color: 1,1,1,1
                pos_hint: {'center_x': 0.5,'center_y': 0.9}
            TextInput:
                id: login_user
                size_hint_y: .75
                hint_text: "Please enter username"
                pos_hint: {'center_x': .49,'center_y': 0.4}
                background_color: 0,0,0,0
                cursor_color: 1,1,1,1
                cursor_width: "2sp"
                foreground_color: 1,1,1,1
                font_size:"17sp"
                multiline: False
        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {'center_x': 0.5,'center_y': 0.28}
            MDLabel:
                text: "Password"
                font_size: "14sp"
                color: 1,1,1,1
                pos_hint: {'center_x': 0.5,'center_y': 0.9}
            TextInput:
                id: login_pass
                size_hint_y: .75
                hint_text: "Please enter password"
                pos_hint: {'center_x': .49,'center_y': 0.4}
                background_color: 230,230,230,0
                cursor_color: 1,1,1,1
                cursor_width: "2sp"
                foreground_color: 1,1,1,1
                font_size:"17sp"
                multiline: False
                password: True
    Button:
        text: "Click Me"
        background_color: 1,1,1,1
        size_hint: .79, .08
        pos_hint: {'center_x': 0.5,'center_y': .15}
        bold: True
        font_size:"24sp"
        on_press: app.login()
    Button:
        text: "Sign Up"
        background_color: 0,0,0,0
        size_hint: .79, .08
        pos_hint: {'center_x': 0.5,'center_y': .05}
        font_size:"15sp"
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "signupscreen"

<SignupScreen>
    name: "signupscreen"
    MDFloatLayout:
        md_bg_color: 226/255, 0, 48/255, 1
        
        Image:
            source: "assets/logo.png"
            size_hint: 0.7, 0.7
            pos_hint: {'center_x': 0.22,'center_y': 0.82}
        MDIconButton:
            icon: "chevron-left"
            user_font_size: "35sp"
            pos_hint: {'center_y': 0.95}
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "loginscreen"
        MDLabel:
            text:"Back"
            color: 1,1,1,1
            font_size:"18sp"
            pos_hint: {'center_x': 0.615,'center_y': 0.949}
        MDLabel:
            text: "Please Enter your credentials to"
            font_size: "18sp"
            color: 1,1,1,1
            pos_hint: {'center_x': .6,'center_y': 0.65}
        MDLabel:
            text: "Registration"
            font_size: "28sp"
            bold: True
            color: 1,1,1,1
            pos_hint: {'center_x': .6,'center_y': 0.58}
        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {'center_x': 0.5,'center_y': 0.42}
            MDLabel:
                text: "Username"
                font_size: "14sp"
                color: 1,1,1,1
                pos_hint: {'center_x': 0.5,'center_y': 0.9}
            TextInput:
                id: signup_user
                size_hint_y: .75
                hint_text: "Please enter username"
                pos_hint: {'center_x': .49,'center_y': 0.4}
                background_color: 0,0,0,0
                cursor_color: 1,1,1,1
                cursor_width: "2sp"
                foreground_color: 1,1,1,1
                font_size:"17sp"
                multiline: False
        MDFloatLayout:
            size_hint: .79, .08
            pos_hint: {'center_x': 0.5,'center_y': 0.28}
            MDLabel:
                text: "Password"
                font_size: "14sp"
                color: 1,1,1,1
                pos_hint: {'center_x': 0.5,'center_y': 0.9}
            TextInput:
                id: signup_pass
                size_hint_y: .75
                hint_text: "Please enter password"
                pos_hint: {'center_x': .49,'center_y': 0.4}
                background_color: 230,230,230,0
                cursor_color: 1,1,1,1
                cursor_width: "2sp"
                foreground_color: 1,1,1,1
                font_size:"17sp"
                multiline: False
    Button:
        text: "Click to Sign Up"
        background_color: 1,1,1,1
        size_hint: .79, .08
        pos_hint: {'center_x': 0.5,'center_y': .15}
        bold: True
        font_size:"24sp"
        on_press: app.printSignup()

<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "check"
            theme_icon_color: "Custom"
            icon_color: "orange"
            pos_hint: {"center_y": .5}
            on_release: app.remove_item(root)

    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True

<TodoTaskScreen>
    name: "todotaskscreen"
    on_enter: app.get_current_week()
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout: 
            line_color: 1,1,1,1
            size_hint: 1, .5
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: "orange"
                icon_size: "24sp"
                halign: 'center'
                valign: 'center'
                on_release: app.get_previous_week()
            MDLabel:
                id: current_week_date_range_label
                text: "2024-02-02"
                color: "white"
                text_size: self.size
                line_color: 1,1,1,1
                halign: 'center'
                valign: 'center'

            MDIconButton:
                icon: "arrow-right"
                theme_icon_color: "Custom"
                icon_color: "orange"
                icon_size: "24sp"
                on_release: app. get_next_week()
        MDBoxLayout: 
            orientation: "vertical"
            iine_color: 1,1,1,1
            size_hint: 1, .7
            MDBoxLayout: 
                iine_color: 1,1,1,1
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_monday
                            text: "Monday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_monday_date_label
                            text: "2024-02-02"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_monday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            id: todo_monday_addtask_button
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon: "plus"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_monday_date_label,todo_monday,todo_monday_text,md_list1)
                MDScrollView:
                    MDList:
                        id: md_list1
                        text: md_list1
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_tuesday
                            text: "Tuesday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_tuesday_date_label
                            text: "2024-02-023"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_tuesday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_tuesday_date_label,todo_tuesday,todo_tuesday_text,md_list2)
                MDScrollView:
                    MDList:
                        id: md_list2
                        text: md_list2
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_wednesday
                            text: "Wednesday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_wednesday_date_label
                            text: "2024-02-04"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_wednesday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_wednesday_date_label,todo_wednesday,todo_wednesday_text,md_list3)
                MDScrollView:
                    MDList:
                        id: md_list3
                        text: md_list3
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_thursday
                            text: "Thursday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_thursday_date_label
                            text: "2024-02-05"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_thursday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_thursday_date_label,todo_thursday,todo_thursday_text,md_list4)
                MDScrollView:
                    MDList:
                        id: md_list4
                        text: md_list4
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_friday
                            text: "Friday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_friday_date_label
                            text: "2024-02-06"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_friday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_friday_date_label,todo_friday,todo_friday_text,md_list5)
                MDScrollView:
                    MDList:
                        id: md_list5
                        text: md_list5
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_saturday
                            text: "Saturday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_saturday_date_label
                            text: "2024-02-07"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_saturday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_saturday_date_label,todo_saturday,todo_saturday_text,md_list6)
                MDScrollView:
                    MDList:
                        id: md_list6
                        text: md_list6
                        padding: 0
        MDBoxLayout: 
            orientation: "vertical"
            size_hint: 1, .7
            iine_color: 1,1,1,1
            MDBoxLayout: 
                size_hint: 1, .05
                MDBoxLayout:
                    orientation: "vertical"
                    MDBoxLayout: 
                        MDLabel:
                            id: todo_sunday
                            text: "Sunday"
                            color: "white"
                            bold: True
                        MDLabel:
                            id: todo_sunday_date_label
                            text: "2024-02-08"
                            color: "white"
                    MDBoxLayout:
                        MDTextField:
                            id: todo_sunday_text
                            hint_text: "Please enter your task"
                        MDIconButton:
                            icon: "plus"
                            theme_icon_color: "Custom"
                            icon_color: "orange"
                            icon_size: "24sp"
                            on_release:app.addTask(todo_sunday_date_label,todo_sunday,todo_sunday_text,md_list7)
                MDScrollView:
                    MDList:
                        id: md_list7
                        text: md_list7
                        padding: 0   
                           
'''
class SplashScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class TodoTaskScreen(Screen):
    pass
class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    s_date = StringProperty()
    s_day = StringProperty()
    listid = ObjectProperty()

sm = ScreenManager()
sm.add_widget(SplashScreen(name = 'pre-splash'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
sm.add_widget(TodoTaskScreen(name = 'todotaskscreen'))

class NewApp(MDApp):
    dialog = None
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    prev_week_start_date= None
    prev_week_end_date= None
    next_week_start_date=None
    next_week_end_date=None
    current_week_start_date=None
    current_week_end_date=None
    def build(self):
        self.strng = Builder.load_string(helpstr)
        #create a db and connect
        conn = sqlite3.connect("simplan_db.db")
        #cursor
        c = conn.cursor()
        #create a table
        c.execute(""" CREATE TABLE if not exists user(email text, password text)
                  """)
        
        c.execute(""" CREATE TABLE if not exists todo(t_date text, t_day text, label text, finished text,t_details text, email text)
                  """)
        conn.commit()
        conn.close()
        return self.strng
    
    def remove_item(self, instance):
        todo_date_id=instance.s_date
        todo_weekDay_id=instance.s_day
        todo_task_id=instance.text
        listid= instance.listid

        self.finishTask(todo_date_id,todo_weekDay_id,todo_task_id)
        listid.remove_widget(instance)
        

    def on_start(self):
        Clock.schedule_once(self.loginAfterSplash,5)
            
    
    def loginAfterSplash(self, *args):
        self.strng.get_screen('loginscreen').manager.current = "loginscreen"
    
    def printSignup(self):
        email = self.strng.get_screen('signupscreen').ids.signup_user.text
        password = self.strng.get_screen('signupscreen').ids.signup_pass.text
        if(re.fullmatch(self.regex_email, email)):
            conn = sqlite3.connect("simplan_db.db")
            c = conn.cursor()

            #create a table
            sql= ("INSERT INTO user (email,password) VALUES(?,?);")

            mydata = (email,password)
            c.execute(sql,mydata)
            conn.commit()
            conn.close()
            self.show_alert_dialog("Successfully SignUp ")
            self.strng.get_screen('signupscreen').ids.signup_user.text=""
            self.strng.get_screen('signupscreen').ids.signup_pass.text=""
            
        else:
            self.show_alert_dialog("Please enter correct email")

    def login(self):
        email = self.strng.get_screen('loginscreen').ids.login_user.text
        password = self.strng.get_screen('loginscreen').ids.login_pass.text
        if(re.fullmatch(self.regex_email, email)):
            conn = sqlite3.connect("simplan_db.db")
            c = conn.cursor()
            c.execute("SELECT * FROM user")
            records = c.fetchall()
            word=''
            flag=0
            for record in records:
                
                if email==record[0] and password==record[1]:
                    flag=1
                    break
            
            conn.commit()
            conn.close()

            if flag==1:
                self.loginemail=email
                self.strng.get_screen('todotaskscreen').manager.current = "todotaskscreen"

            else:
                self.show_alert_dialog("Login Failed")
                
        else:
            self.show_alert_dialog("Please enter correct email")    
    
    def get_current_week(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        start=self.current_week_start_date
        end=self.current_week_end_date
        
        if(start==None and end==None):
            today = date.today()
            day = today.strftime("%d/%b/%Y")
            dt = datetime.strptime(day, '%d/%b/%Y')
            start = dt - timedelta(days=dt.weekday())
            end = start + timedelta(days=6)
        
            
        secondDay=start + timedelta(days=1)
        secondWeekDay = secondDay.weekday()
        secondDay=secondDay.date()
        self.strng.get_screen('todotaskscreen').ids.todo_tuesday_date_label.text=str(secondDay)
        
        thirdDay=start + timedelta(days=2)
        thirdDay=thirdDay.date()
        self.strng.get_screen('todotaskscreen').ids.todo_wednesday_date_label.text=str(thirdDay)

        fourthDay=start + timedelta(days=3)
        fourthDay=fourthDay.date()
        self.strng.get_screen('todotaskscreen').ids.todo_thursday_date_label.text=str(fourthDay)

        fiveDay=start + timedelta(days=4)
        fiveDay=fiveDay.date()
        self.strng.get_screen('todotaskscreen').ids.todo_friday_date_label.text=str(fiveDay)

        sixDay=start + timedelta(days=5)
        sixDay=sixDay.date()
        self.strng.get_screen('todotaskscreen').ids.todo_saturday_date_label.text=str(sixDay)

        self.prev_week_start_date=start - timedelta(days=7)
        self.prev_week_end_date=start - timedelta(days=1)
        self.next_week_start_date=end + timedelta(days=1)
        self.next_week_end_date=end + timedelta(days=7)
        start = start.date()
        end = end.date()
        
        self.strng.get_screen('todotaskscreen').ids.todo_monday.text="Monday"
        self.strng.get_screen('todotaskscreen').ids.todo_monday_date_label.text=str(start)
        self.strng.get_screen('todotaskscreen').ids.todo_sunday_date_label.text=str(end)

        self.strng.get_screen('todotaskscreen').ids.current_week_date_range_label.text= f"{start} - {end}"
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_monday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_monday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list1)
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_tuesday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_tuesday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list2)

        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_wednesday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_wednesday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list3)
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_thursday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_thursday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list4)
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_friday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_friday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list5)
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_saturday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_saturday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list6)
        
        self.load_task(
            self.strng.get_screen('todotaskscreen').ids.todo_sunday_date_label.text,
            self.strng.get_screen('todotaskscreen').ids.todo_sunday.text,
            self.loginemail,
            self.strng.get_screen('todotaskscreen').ids.md_list7)
        
    def load_task(self,todo_date,todo_weekDay,todo_user,list):
        todo_finished = "No"
        conn = sqlite3.connect("simplan_db.db")
        c = conn.cursor()
        sql= "SELECT t_details FROM todo WHERE t_date=? AND t_day =? AND finished=? AND email=?"
        mydata = (todo_date, todo_weekDay,todo_finished, todo_user)
        c.execute(sql,mydata)
        records = c.fetchall()
        
        for record in records:
            list.add_widget(
                SwipeToDeleteItem(text=f"{record[0]}",s_date=f"{todo_date}",s_day=f"{todo_weekDay}",listid=list)
            )
    
    def get_previous_week(self):
        self.strng.get_screen('todotaskscreen').ids.md_list1.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list2.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list3.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list4.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list5.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list6.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list7.clear_widgets()
        self.current_week_start_date = self.prev_week_start_date
        self.current_week_end_date = self.prev_week_end_date
        self.get_current_week()

    def get_next_week(self):
        self.strng.get_screen('todotaskscreen').ids.md_list1.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list2.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list3.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list4.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list5.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list6.clear_widgets()
        self.strng.get_screen('todotaskscreen').ids.md_list7.clear_widgets()
        self.current_week_start_date = self.next_week_start_date
        self.current_week_end_date = self.next_week_end_date
        self.get_current_week()
    
    def addTask(self,todo_date_id,todo_weekDay_id,todo_task_id,list_id):
        if (todo_task_id.text !=""):
            todo_date= todo_date_id.text
            todo_weekDay = todo_weekDay_id.text
            todo_task = todo_task_id.text
            list_id.add_widget(
                    SwipeToDeleteItem(text=f"{todo_task}",s_date=f"{todo_date}",s_day=f"{todo_weekDay}",listid=list_id)
                )
            
            todo_label="Daily"
            todo_finished = "No"
            todo_user= self.loginemail

            conn = sqlite3.connect("simplan_db.db")
            c = conn.cursor()

            #create a table
            sql= ("INSERT INTO todo (t_date, t_day, label, finished, t_details, email) VALUES(?,?,?,?,?,?);")

            mydata = (todo_date, todo_weekDay, todo_label,todo_finished,todo_task,todo_user)
            c.execute(sql,mydata)
            conn.commit()
            conn.close()
            
            todo_task_id.text=""
        else:
            self.show_alert_dialog("Please fill the task details")


    def finishTask(self,todo_date_id,todo_weekDay_id,todo_task_id):
        todo_date= todo_date_id
        todo_weekDay= todo_weekDay_id
        todo_finished = "Yes"
        todo_user= self.loginemail
        todo_task = todo_task_id
        conn = sqlite3.connect("simplan_db.db")
        c = conn.cursor()
        sql=("UPDATE todo SET finished = ? WHERE t_date = ? AND t_day = ? AND t_details = ? AND email = ?;") 
        mydata = (todo_finished,todo_date,todo_weekDay,todo_task,todo_user)
        c.execute(sql,mydata)
        conn.commit()
        conn.close()

    def show_alert_dialog(self,message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.dialog_close
                    ),
                    # MDFlatButton(
                    #     text="DISCARD",
                    #     theme_text_color="Custom",
                    #     text_color=self.theme_cls.primary_color,
                    #     on_release=self.dialog_close
                    # ),
                ],
            )
        self.dialog.open()

    def dialog_close(self, obj):
        self.dialog.dismiss()
        self.dialog=None
        
NewApp().run()