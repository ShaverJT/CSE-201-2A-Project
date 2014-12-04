from django.test import TestCase
from AppCat.models import app

class AppTestCase(TestCase)
	def setUp(self):
	app.objects.Create(name="test1",description="first test",link="www.test.com",rating=3,approved=False)
	app.objects.Create(name="test2",description="our project",link="www.tst2.org",rating=1, approved=False)
	app.objects.Create(name="test3",description="second",link="www.tst3.org",rating=4, approved=True)
	app.objects.Create(name="test4",description="best",link="www.tst4.org",rating=5, approved=True)
	app.objects.Create(name="test5",description="ok",link="www.tst5.org",rating=2,approved=False)
	app.objects.Create(name="test6",description="none",link="www.tst6.org",rating=3,approved=False)

class test_apps_exist(self)
	test1 = app.objects.get(name="test1")
	test2 = app.objects.get(name="demo2")
	test3 = app.objects.get(name="demo2")
	test4 = app.objects.get(name="demo2")
	test5 = app.objects.get(name="demo2")
	test6 = app.objects.get(name="demo2")

	self.assertEqual(test1.approved, False)
	self.assertEqual(test2.approved, False)
	self.assertEqual(test3.approved, True)
	self.assertEqual(test4.approved, True)
	self.assertEqual(test5.approved, False)
	self.assertEqual(test6.approved, False)
	
# Create your tests here.
