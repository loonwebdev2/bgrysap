from django.urls import resolve
from django.test import TestCase
from MNList.views import MainPage

from MNList.models import Info, IBrgy

from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):
    
   def test_my_mainpage_view(self):
       found = resolve('/')
       self.assertEqual(found.func, MainPage)
      
   def test_correct_view(self):
       request = HttpRequest()
       response = MainPage(request)
       expected_html = render_to_string('BSMS.html')

   
   def test_saves_necessary(self): 
       self.client.get('/')        
       self.assertEqual(Info.objects.count(), 0)
      
class ListViewTest(TestCase):
 
   def test_uses_SInfotemplate(self):
       ibrgy_ = IBrgy.objects.create()        
       response = self.client.get(f'/MNList/{ibrgy_.id}/')
       self.assertTemplateUsed(response, 'SInfo.html')
      
   def test_display_list_item(self):
       correct_ibrgy = IBrgy.objects.create()
       Info.objects.create(textFM='Sasuke Uchiha', ibrgy=correct_ibrgy)
       Info.objects.create(textRS='Father', ibrgy=correct_ibrgy)
       other_ibrgy = IBrgy.objects.create()
       Info.objects.create(textFM='other list item 1', ibrgy=other_ibrgy)
       Info.objects.create(textRS='other list item 2', ibrgy=other_ibrgy)        
      
       response = self.client.get(f'/MNList/{correct_ibrgy.id}/')
      
       self.assertContains(response, 'Sasuke Uchiha')
       self.assertContains(response, 'Father')
       self.assertNotContains(response, 'other list item 1')
       self.assertNotContains(response, 'other list item 2')
   
   def test_displays_all(self):        
       ibrgy_ = IBrgy.objects.create()        
       Info.objects.create(textFM='Sasuke Uchicha', ibrgy=ibrgy_)        
       Info.objects.create(textRS='Father', ibrgy=ibrgy_)
   
   def test_passes_correct_template(self):       
       other_ibrgy = IBrgy.objects.create()        
       correct_ibrgy = IBrgy.objects.create()        
       response = self.client.get(f'/MNList/{correct_ibrgy.id}/')
       self.assertEqual(response.context['ibrgy'], correct_ibrgy)  


class NewListTest(TestCase):   

 
   def test_redirect_POST(self):        
       response = self.client.post('/MNList/new', data={'Brgy': 'Barangay','BrgyID': 'Barangay ID','addFM': 'Name','addRS': 'Relation', 'addadd': 'Address'})                     
       newibrgy_= IBrgy.objects.first()        
       self.assertRedirects(response, f'/MNList/{newibrgy_.id}/')
       
 
 

class InfoTest(TestCase):


  def test_info(self):       
      other_ibrgy = IBrgy.objects.create()        
      correct_ibrgy = IBrgy.objects.create()        
      
      self.client.post(            
          f'/MNList/{correct_ibrgy.id}/add_info',            
          data={'Brgy': 'New Barangay','BrgyID': 'New Barangay ID','addFM': 'New Name','addRS': 'New Relation', 'addadd': 'New Address'}       
      )        
      
      self.assertEqual(Info.objects.count(), 1)        
      new_info= Info.objects.first()        
      self.assertEqual(new_info.textAdd, 'New Address')       
      self.assertEqual(new_info.ibrgy, correct_ibrgy)
      
  def test_redirects_info(self):        
      other_ibrgy = IBrgy.objects.create()        
      correct_ibrgy = IBrgy.objects.create()        
      response = self.client.post(            
          f'/MNList/{correct_ibrgy.id}/add_info',            
         data={'Brgy': 'New Barangay','BrgyID': 'New Barangay ID','addFM': 'New Name','addRS': 'New Relation', 'addadd': 'New Address'}    
      )        
      self.assertRedirects(response, f'/MNList/{correct_ibrgy.id}/')
      
class MyORMandMNList(TestCase):

   def test_save_retrieve_info(self):
      ibrgy_ = IBrgy()        
      ibrgy_.save()
      
      first_info = Info()        
      first_info.textFM = 'The first (ever) list item' 
      first_info.ibrgy = ibrgy_ 
      first_info.save()        
               
      second_info = Info()      
      second_info.textFM = 'Item the second'
      second_info.ibrgy = ibrgy_         
      second_info.save()
       
       
      saved_ibrgy = IBrgy.objects.first()          
      self.assertEqual(saved_ibrgy, ibrgy_)
                 
      saved_infos = Info.objects.all()
      self.assertEqual(saved_infos.count(), 2)
       
      first_saved_info = saved_infos[0]
      second_saved_info = saved_infos[1]      	     
      self.assertEqual(first_saved_info.textFM, 'The first (ever) list item')
      self.assertEqual(first_saved_info.ibrgy, ibrgy_)
      self.assertEqual(second_saved_info.textFM, 'Item the second')
      self.assertEqual(second_saved_info.ibrgy, ibrgy_)

       
''' 

class NewListTest(TestCase):   

 
   def test_redirect_POST(self):        
       response = self.client.post('/MNList/new', data={'Brgy': 'Barangay','BrgyID': 'Barangay ID','addFM': 'Name','addRS': 'Relation', 'addadd': 'Address'})                     
       newibrgy_= IBrgy.objects.first()        
       self.assertRedirects(response, f'/MNList/{newibrgy_.id}/')
       
 
        


class MyORMandMNList(TestCase):

   def test_save_retrieve_info(self):
      ibrgy_ = IBrgy()        
      ibrgy_.save()
      
      first_ibrgy = IBrgy()        
      first_ibrgy.text = 'The first (ever) list item' 
      first_ibrgy.ibrgy = ibrgy_ 
      first_ibrgy.save()        
               
      second_ibrgy = IBrgy()      
      second_ibrgy.text = 'Item the second'
      second_ibrgy.ibrgy = ibrgy_         
      second_ibrgy.save()
       
       
      saved_ibrgy = IBrgy.objects.first()          
      self.assertEqual(saved_ibrgy, ibrgy_)
                 
      saved_ibrgy_ = IBrgy.objects.all()
      self.assertEqual(saved_ibrgy_.count(), 3)
       
      first_saved_ibrgy = saved_ibrgy_[0]
      second_saved_ibrgy= saved_ibrgy_[1]      	     
      self.assertEqual(first_saved_ibrgy.text, '')
      self.assertEqual(first_saved_ibrgy.ibrgy, ibrgy_)
      self.assertEqual(second_saved_ibrgy.text, 'Item the second')
      self.assertEqual(second_saved_ibrgy.ibrgy, ibrgy_)











   def test_uses_list_template(self):        
       response = self.client.get('/MNList/the-only-list-in-the-world/')            
       self.assertTemplateUsed(response, 'my2.html')

   def test_redirects_after_POST(self):        
       response = self.client.post('/MNList/new', data={'itext': 'A new list item'})        
       self.assertEqual(response.status_code, 302)
       self.assertEqual(response['location'], '/MNList/the-only-list-in-the-world/')
   def test_displays_all_list_items(self):        
      Info.objects.create(text='Raymond')        
      Info.objects.create(text='Loon')  
         
      
      self.assertContains(response, 'Raymond')
      self.assertContains(response, 'Loon')
   
  response = self.client.post('/', data={'itext': 'A new list item'})     
     
       
           
    self.assertIn('A new list item', response.content.decode())
    self.assertTemplateUsed(response, 'mynotes.html')
  
   self.assertEqual(response.status_code, 302)
   self.assertEqual(response['location'], '/')
      

      def test_mainpage_can_save_a_POST_request(self):    
      request = HttpRequest()    
      request.method = 'POST'    
      request.POST['itext'] = 'A new list item'  
      
      response = MainPage(request)   
      	  
      self.assertIn('A new list item', response.content.decode())
      expected_html = render_to_string(
          'mynotes.html',
          {'new_itext:  'A new list item'}
      )
      self.assertEqual(response.content.decode(), expected_html)
      
  html = response.content.decode('utf8')
      self.assertTrue(html.startswith('<html>'))
      self.assertIn('<title>My Notes</title>', html)
	'''


