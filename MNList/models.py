from django.db import models

    
class IBrgy(models.Model):
      mncplty = models.TextField(default='')  
      bname = models.TextField(default='')  
      bID = models.CharField(default='', max_length=6) 
      class meta:
          db = "brgy"
	
class BResidents(models.Model):     
      rname = models.TextField(default='')  
      rrelation = models.TextField(default='')
      radd = models.TextField(default='')    
      ibrgy = models.ForeignKey(IBrgy, default=None, on_delete=models.CASCADE)
      class meta:
          db = "residents"	
          
class SBeneficiary(models.Model):  
      scategory = models.TextField(default='')
      samount = models.TextField(default='')
      bresidents = models.ForeignKey(BResidents, default=None, on_delete=models.CASCADE)  
      class meta:
          db = "beneficiary"	 
          
class SDistributions(models.Model):
      dtranche = models.TextField(default='') 
      dmode = models.TextField(default='') 
      dlocation = models.TextField(default='')
      sbeneficiary = models.ForeignKey(SBeneficiary, default=None, on_delete=models.CASCADE)  
      class meta:
          db = "distribution"	
          
class StatusDB(models.Model):
      dstatus = models.TextField(default='')
      dremarks = models.TextField(default='')   	
      ddate = models.DateTimeField(default='')  
      sdistributions = models.ForeignKey(SDistributions, default=None, on_delete=models.CASCADE)
      class meta:
          db = "status"	  
'''    

class Info(models.Model):    
    
    textFM = models.TextField(default='')  
    textRS = models.TextField(default='')
    textAdd = models.TextField(default='')    
    ibrgy = models.ForeignKey(IBrgy, default=None, on_delete=models.PROTECT)
    '''
