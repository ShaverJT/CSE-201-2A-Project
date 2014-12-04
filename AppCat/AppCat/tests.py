from django.test import TestCase
from Applications.models import App, Review

class AppTestCase(TestCase):
	def setUp(self):
            App.objects.create(app_name="test1",developers="Testers1",description="A test number 1",link="http://www.test1.com")
            App.objects.create(app_name="test2",developers="Testers2",description="A test number 2",link="http://www.test2.com")
            App.objects.create(app_name="test3",developers="Testers3",description="A test number 3",link="http://www.test3.com")
            App.objects.create(app_name="test4",developers="Testers4",description="A test number 4",link="http://www.test4.com")
            App.objects.create(app_name="test5",developers="Testers5",description="A test number 5",link="http://www.test5.com")

        def test_name1(self):
            test1 = App.objects.get(app_name="test1")
            self.assertEqual(str(test1),test1.app_name)
        
        def test_name2(self):
            test2 = App.objects.get(app_name="test2")
            self.assertEqual(str(test2),test2.app_name)
        
        def test_name3(self):
            test3 = App.objects.get(app_name="test3")
            self.assertEqual(str(test3),test3.app_name)
        
        def test_name4(self):
            test4 = App.objects.get(app_name="test4")
            self.assertEqual(str(test4),test4.app_name)
        
        def test_name5(self):
            test5 = App.objects.get(app_name="test5")
            self.assertEqual(str(test5),test5.app_name)
            
        def test_rating1(self):
            test1 = App.objects.get(app_name="test1")
            Review.objects.create(app=test1,review_name="Name1",description="Description1",rating=3)
            Review.objects.create(app=test1,review_name="Name2",description="Description2",rating=3)
            Review.objects.create(app=test1,review_name="Name3",description="Description3",rating=3)
            Review.objects.create(app=test1,review_name="Name4",description="Description4",rating=3)
            Review.objects.create(app=test1,review_name="Name5",description="Description5",rating=3)
            self.assertEqual(test1.rating,3)
        
        def test_rating2(self):
            test2 = App.objects.get(app_name="test2")
            Review.objects.create(app=test2,review_name="Name1",description="Description1",rating=3)
            Review.objects.create(app=test2,review_name="Name2",description="Description2",rating=3)
            Review.objects.create(app=test2,review_name="Name3",description="Description3",rating=4)
            Review.objects.create(app=test2,review_name="Name4",description="Description4",rating=4)
            Review.objects.create(app=test2,review_name="Name5",description="Description5",rating=4)
            self.assertEqual(float(test2.rating), 3.6)
        
        def test_rating3(self):
            test3 = App.objects.get(app_name="test3")
            self.assertEqual(test3.rating,"Not Rated")