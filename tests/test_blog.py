from app.models import Blog , User
from app import db

def setUp(self):
        self.user_Gerald = User(username = 'Gerald',password = 'potato', email = 'geerockface4@gmail.com')
        self.new_blog = Blog(id=12345,title='Full stack development',content='Is it safe to go the full-stack way or better the Android path',category= "technology" , date = 1-12-2019, time = 16:04 ,user = self.user_Gerald )


def tearDown(self):
        Blog.query.delete()
        User.query.delete()


def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,12345)
        self.assertEquals(self.new_blog.title,'Full stack development')
        self.assertEquals(self.new_blog.content,"Is it safe to go the full-stack way or better the Android path")
        self.assertEquals(self.new_blog.category,'technology')
        self.assertEquals(self.new_blog.date, 1-12-2019)
        self.assertEquals(self.new_blog. time,16:04)
        self.assertEquals(self.new_blog.user,self.user_Gerald)

def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Review.query.all())>0)