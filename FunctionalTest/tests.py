from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10
class BSMSTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

   
    
    def wait_for_table(self, row_text):        
        start_time = time.time()
        while True:  
      	    try:                
      	        table = self.browser.find_element_by_id('id_table')                  
      	        rows = table.find_elements_by_tag_name('tr')                
      	        self.assertIn(row_text, [row.text for row in rows])
      	        return
      	    except (AssertionError, WebDriverException) as e:  
      	        if time.time() - start_time > MAX_WAIT:  
      	            raise e                  
      	        time.sleep(0.5)  
 
    def test_for_first_entry(self):       

        self.browser.get('http://localhost:8000')
       #self.browser.get(self.live_server_url)
        self.assertIn('BARANGAY SAP MONITORING SYSTEM', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('BARANGAY SAP MONITORING SYSTEM', header_text)  
      	
        
        inputmncplty = self.browser.find_element_by_id('Municipality')
        inputbrgy = self.browser.find_element_by_id('Brgy')
        inputbrgyID = self.browser.find_element_by_id('BrgyID')
        self.assertEqual(inputmncplty.get_attribute('placeholder'),'Enter Municipality')
        self.assertEqual(inputbrgy.get_attribute('placeholder'),'Enter Barangay')
        self.assertEqual(inputbrgyID.get_attribute('placeholder'),'Enter Barangay ID')
        
        time.sleep(1)
        inputmncpltyy =  self.browser.find_element_by_id('Municipality')
        inputmncplty.click()
        inputmncplty.send_keys('Dasmariñas City')
       
        time.sleep(1)
        inputbrgy =  self.browser.find_element_by_id('Brgy')
        inputbrgy.click()
        inputbrgy.send_keys('Brgy. Victoria Reyes')
        
        time.sleep(1)
        inputbrgyId =  self.browser.find_element_by_id('BrgyID')
        inputbrgyID.click()
        inputbrgyID.send_keys('301185')
        

        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        

        time.sleep(1)
        
        inputaddFM= self.browser.find_element_by_id('addFM')
        inputaddRS = self.browser.find_element_by_id('addRS')
        inputaddadd = self.browser.find_element_by_id('addadd')
        self.assertEqual(inputaddFM.get_attribute('placeholder'),'Enter Family Member')
        self.assertEqual(inputaddRS.get_attribute('placeholder'),'Enter Relation')
        self.assertEqual(inputaddadd.get_attribute('placeholder'),'Enter Address')
        
        time.sleep(1)
        inputaddFM =  self.browser.find_element_by_id('addFM')
        inputaddFM.click()
        inputaddFM.send_keys('Sasuke Uchiha')
        
        time.sleep(1)
        inputaddRS =  self.browser.find_element_by_id('addRS')
        inputaddRS.click()
        inputaddRS.send_keys('Father')
        
        time.sleep(1)
        inputaddadd =  self.browser.find_element_by_id('addadd')
        inputaddadd.click()
        inputaddadd.send_keys('B 7 L 7')
        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        
        
        time.sleep(1)
        
        inputaddFM =  self.browser.find_element_by_id('addFM')
        inputaddFM.click()
        inputaddFM.send_keys('Sakura Haruno')
        
        time.sleep(1)
        inputaddRS =  self.browser.find_element_by_id('addRS')
        inputaddRS.click()
        inputaddRS.send_keys('Mother')
        
        time.sleep(1)
        inputaddadd =  self.browser.find_element_by_id('addadd')
        inputaddadd.click()
        inputaddadd.send_keys('B 7 L 7')
        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        time.sleep(1)

   
'''
    def test_for_second_entry(self):   
     
     
        self.browser.get('http://localhost:8000')
       #self.browser.get(self.live_server_url)
        self.assertIn('BARANGAY SAP MONITORING SYSTEM', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('BARANGAY SAP MONITORING SYSTEM', header_text)  
      
        
        inputbrgy = self.browser.find_element_by_id('Brgy')
        inputbrgyID = self.browser.find_element_by_id('BrgyID')
        self.assertEqual(inputbrgy.get_attribute('placeholder'),'Enter Barangay')
        self.assertEqual(inputbrgyID.get_attribute('placeholder'),'Enter Barangay ID')
        
        time.sleep(1)
        inputbrgy =  self.browser.find_element_by_id('Brgy')
        inputbrgy.click()
        inputbrgy.send_keys('Brgy. Sampaloc')
        
        time.sleep(1)
        inputbrgyId =  self.browser.find_element_by_id('BrgyID')
        inputbrgyID.click()
        inputbrgyID.send_keys('301186')
        

        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        

        time.sleep(1)
        
        inputaddFM= self.browser.find_element_by_id('addFM')
        inputaddRS = self.browser.find_element_by_id('addRS')
        inputaddadd = self.browser.find_element_by_id('addadd')
        self.assertEqual(inputaddFM.get_attribute('placeholder'),'Enter Family Member')
        self.assertEqual(inputaddRS.get_attribute('placeholder'),'Enter Relation')
        self.assertEqual(inputaddadd.get_attribute('placeholder'),'Enter Address')
        
        time.sleep(1)
        inputaddFM =  self.browser.find_element_by_id('addFM')
        inputaddFM.click()
        inputaddFM.send_keys('Kirigaya Kazuto')
        
        time.sleep(1)
        inputaddRS =  self.browser.find_element_by_id('addRS')
        inputaddRS.click()
        inputaddRS.send_keys('Father')
        
        time.sleep(1)
        inputaddadd =  self.browser.find_element_by_id('addadd')
        inputaddadd.click()
        inputaddadd.send_keys('B 11 L 11')
        
 
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()     
        
        time.sleep(1)
        
        inputaddFM= self.browser.find_element_by_id('addFM')
        inputaddRS = self.browser.find_element_by_id('addRS')
        inputaddadd = self.browser.find_element_by_id('addadd')
        self.assertEqual(inputaddFM.get_attribute('placeholder'),'Enter Family Member')
        self.assertEqual(inputaddRS.get_attribute('placeholder'),'Enter Relation')
        self.assertEqual(inputaddadd.get_attribute('placeholder'),'Enter Address')
        
        time.sleep(1)
        inputaddFM =  self.browser.find_element_by_id('addFM')
        inputaddFM.click()
        inputaddFM.send_keys('Yuuki Asuna')
        
        time.sleep(1)
        inputaddRS =  self.browser.find_element_by_id('addRS')
        inputaddRS.click()
        inputaddRS.send_keys('Mother')
        
        time.sleep(1)
        inputaddadd =  self.browser.find_element_by_id('addadd')
        inputaddadd.click()
        inputaddadd.send_keys('B 11 L 11')
        
 
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()     
        
        
        
        
     
#if __name__=='__main__':
#   unittest.main()

  user2_url = self.browser.current_url
        self.assertRegex(user2_url, '/MNList/.+')
        self.assertnotEqual(viewlist_url, user2_url)
      
 
    
	inputbox = self.browser.find_element_by_id('new_id')
        self.assertEqual(inputbox.get_attribute('placeholder'),'add notes')
        
        inputbox.send_keys('Raymond') 
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Raymond')
      
        inputbox = self.browser.find_element_by_id('new_id')    
        inputbox.send_keys('Loon')    
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('2: Loon')
        self.wait_for_row_in_list_table('1: Raymond')
   
  
        inputbox2 = self.browser.find_element_by_id('new_add')
        self.assertEqual(inputbox2.get_attribute('placeholder'),'add address')
       
        inputbox2.send_keys('Victo') 
        inputbox2.send_keys(Keys.ENTER)


self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Rayz', page_text)
        self.assertNotIn('Raizen', page_text)
       
        inputbox = self.browser.find_element_by_id('new_id')
        inputbox.send_keys('RaN')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: RaN')
    
        ray_list_url = self.browser.current_url
        self.assertRegex(ray_list_url, '/lists/.+')

     
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Rayz', page_text)
        self.assertIn('RaN', page_text)  
    
    def test_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('My Notes', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('My Notes', header_text)  
        inputbox = self.browser.find_element_by_id('new_id')
        self.assertEqual(inputbox.get_attribute('placeholder'),'add notes')
        
        inputbox.send_keys('Raymond') 
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Raymond')
      
        inputbox = self.browser.find_element_by_id('new_id')    
        inputbox.send_keys('Loon')    
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('2: Loon')
        self.wait_for_row_in_list_table('1: Raymond')
        
    
 def wait_for_row_in_list_table(self, row_text):
   table = self.browser.find_element_by_id('id_table')
   rows = table.find_elements_by_tag_name('tr')
   self.assertIn(row_text, [row.text for row in rows])

   inputbox.send_keys(Keys.ENTER)
   self.wait_for_row_in_list_table('Raymond')
    
   inputbox = self.browser.find_element_by_id('new_id')    
   inputbox.send_keys('Loon')    
   inputbox.send_keys(Keys.ENTER)
   time.sleep(1)
   self.wait_for_row_in_list_table('Raymond')
   self._for_row_in_list_table('Loon')
   
  def setUp(self):
   self.browser = webdriver.Firefox()
   
   def test_browser_title(self):
   self.browser.get('http://localhost:8000')
   self.assertIn('My Notes', self.browser.title)
 
  
   
   
  def tearDown(self):
   self.browser.quit()
   
  def test_browser_title(self):
   self.browser.get('http://localhost:8000')
   self.assertIn('My Notes', self.browser.title)



   header_text = self.browser.find_element_by_tag_name('h1').text
   self.assertIn('My Notes', header_text)  

   
 
   self.assertEqual(
   	   inputbox.get_attribute('placeholder'),
   	   'add notes'
   )

   inputbox.send_keys('Raymond')
   inputbox.send_keys(Keys.ENTER)    
   table = self.browser.find_element_by_id('id_list_table')
   rows = table.find_elements_by_tag_name('tr')
   self.assertIn('1: Raymond', [row.text for row in rows])
  


'''    
