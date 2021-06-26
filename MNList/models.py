from django.db import models

    
class IBrgy(models.Model):
      mncplty = models.TextField(default='')  
      bname = models.TextField(default='')  
      bID = models.CharField(default='', max_length=6) 
      class meta:
          db = "brgy"
	
class BResidents(models.Model):     
      rlname = models.TextField(default='')
      rfname = models.TextField(default='')
      rmname = models.TextField(default='')
      rrelation = models.TextField(default='')
      rjob = models.TextField(default='') 
      rnumber = models.IntegerField(default='')  
      radd = models.TextField(default='')
      ibrgy = models.ManyToManyField(IBrgy, default=None, on_delete=models.CASCADE)
      class meta:
          db = "residents"	
   	
              
class SBeneficiary(models.Model):  
      stranche = models.TextField(default='') 
      sincome = models.IntegerField(default='')
      scategory = models.TextField(default='')
      sclass = models.TextField(default='')
      samount = models.TextField(default='')
      bresidents = models.ManyToManyField(BResidents, default=None, on_delete=models.CASCADE)  
      class meta:
          db = "beneficiary"	 
          
class SDistributions(models.Model): 
      dmode = models.TextField(default='') 
      dtype = models.TextField(default='') 
      dlocation = models.TextField(default='')
    
      #dddate = models.DateTimeField(default='')  
     
      class meta:
          db = "distribution"	
          
class StatusDB(models.Model):	
      sdistribution = models.ManyToManyField(SDistributions, default=None)  	
      bresidents = models.ManyToManyField(BResidents, default=None)  
      sbeneficiary = models.ManyToManyField(SBeneficiary, default=None)  
      ddate = models.DateField(default='')  
      dstatus = models.TextField(default='')
      dperson = models.TextField(default='')
      dremarks = models.TextField(default='') 
  	

      class meta:
          db = "status"	  

