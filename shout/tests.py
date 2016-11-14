from django.test import TestCase
from models import UserProfile
# Create your tests here.


from django.test import Client
class UserTestCase(TestCase):
    
    def test_registration(self):
        c = Client()
        response = c.post('/register/', {'username': '','email' :'' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        print "Register: "+response.reason_phrase
        self.assertEqual(response.status_code,200)

    def test_login(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        response = c.post('/login/', {'username':'johnDoe', 'password' : 'smith'})
        val = False
        if "Invalid username" not in response.content:
            val = True
        self.assertEqual(val, True)

    def test_loginfail(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        response = c.post('/login/', {'username':'john', 'password' : '123'})
        val = False
        if "Invalid username" in response.content:
            val = True
        self.assertEqual(val,True)
    
    def test_shoutPass(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        c.post('/login/', {'username':'johnDoe', 'password' : '123'})
        response = c.post('/shout/', {'shout':'Aenean finibus ac neque ac feugiat. Aliquam ut mi ac leo cursus auctor. Vivamus in felis eu urna cursus dictum. Sed eget dolor finibus massa dapibus.'})
        
        self.assertEqual(response.status_code,200)

    
    def test_shoutfail(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        c.post('/login/', {'username':'johnDoe', 'password' : '123'})
        response = c.post('/shout/', {'shout':'Aenean finibus ac neque ac feugiat. Aliquam ut mi ac leo cursus auctor. Vivamus in felis eu urna cursus dictum. Sed eget dolor finibus massa dapibus gravida. Nulla eget dapibus leo, ac tempor magna.'})
        
        self.assertEqual(response.status_code,200)
    
    def test_eventspass(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'k@gmail.com' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        c.post('/login/', {'username':'johnDoe', 'password' : 'smith'})
        response = c.post('/createEvent/',{'eventName':'bday','eventDescription':'everybody is invited','startDate':'11/07/2016','endDate':'11/08/2016','startTime':'4:45 AM','endTime':'5:45 PM','location':'charlotte', 'invitees':'johnDoe'})
        self.assertEqual(response.status_code,200)
        
   def test_profile_view_pass(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'k@gmail.com' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        c.post('/login/', {'username':'johnDoe', 'password' : 'smith'})
        c.post('/shout/', {'shout':'Aenean finibus ac neque ac feugiat. Aliquam ut mi ac leo cursus auctor. Vivamus in felis eu urna cursus dictum. Sed eget dolor finibus massa dapibus.','pageName':'home'})
        response = c.post('/profile/',{})
        self.assertEqual(response.status_code,200)

   def test_notify_pass(self):
        c = Client()
        c.post('/register/', {'username': 'johnDoe','email' :'k@gmail.com' ,'first_name' : 'john' , 'last_name' : 'kennedy', 'password': ' smith','dateOfBirth' : '2016-10-29', 'bio' : 'ggg'})
        c.post('/login/', {'username':'johnDoe', 'password' : 'smith'})
        c.post('/createEvent/',{'eventName':'bday','eventDescription':'everybody is invited','startDate':'11/07/2016','endDate':'11/08/2016','startTime':'4:45 AM','endTime':'5:45 PM','location':'charlotte', 'invitees':'johnDoe'})
        response = c.post('/notify/',{})
        self.assertEqual(response.status_code,200)    
