
#from django.http import HttpResponse    
from django.shortcuts import redirect, render
from MNList.models import BResidents, IBrgy, SBeneficiary, SDistributions, Statusdbs
#import git
from django.views.decorators.csrf import csrf_exempt

#1st page
def MainPage(request): 
   ibrgys = IBrgy.objects.all()
   #ibrgys = IBrgy.objects.filter(mncplty="DASMARINAS")
   ibrgys = IBrgy.objects.order_by("bname")     
   return render(request, 'BSMS.html',{'ibrgys' : ibrgys})
   
#data ng 1st page     
def new_ibrgy(request):   
    
   newibrgy_ = IBrgy.objects.create(mncplty=request.POST['Municipality'],bname=request.POST['Brgy'],bID=request.POST['BrgyID'])
   return redirect(f'/{newibrgy_.id}/')    
   
   
   
#2nd page     
def view_ibrgy(request, ibrgy_id):   
   bresidents = BResidents.objects.all()  
   sbeneficiarys = SBeneficiary.objects.all()
   sdistributions = SDistributions.objects.all()  
   
   bresidents = BResidents.objects.order_by("rlname")
   #bresidents = BResidents.objects.filter(rrelation="Head of the Family")
   #bresident_ = BResidents.objects.filter(rfname="RAYMOND")
 
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   return render(request, 'SInfo.html', {'ibrgy': ibrgy_,'sdistribution' : sdistributions,'bresidents' : bresidents,'sbeneficiary':sbeneficiarys}) 
   
#data ng 2nd page  
def add_info(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
    
   BResidents.objects.create(rlname=request.POST['addLN'],rfname=request.POST['addFN'],rmname=request.POST['addMN'],rrelation=request.POST['addRelation'],rjob=request.POST['addJob'],rnumber=request.POST['cnumber'],radd=request.POST['addadd'], ibrgy=ibrgy_)
   sbeneficiary=SBeneficiary(stranche=request.POST['btranche'],sincome=request.POST['bincome'],scategory=request.POST['bcategory'],sclass=request.POST['bclass'],samount=request.POST['bamount'])
   sbeneficiary.save()
   
   return redirect(f'/{ibrgy_.id}/statusb')     



def view_statuss(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   bresidents = BResidents.objects.all()
   statusdbs = Statusdbs.objects.all()
   return render(request, 'StatusDB2.html', {'ibrgy': ibrgy_,'statusdb' : statusdbs, 'bresident' : bresidents}) 



def add_statuss(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   statusdbs = Statusdbs(ddate=request.POST['sdate'],dstatus=request.POST['sstatus'],dperson=request.POST['sperson'],dremarks=request.POST['sremarks'])
   statusdbs.save()   
   
   
   return redirect(f'/{ibrgy_.id}/statusb')     


# #5th page     
#def view_status(request): 
#   statusdbs = Statusdbs.objects.all()
#   return render(request, 'StatusDB.html', {'statusdb' : statusdbs})  


#data ng 5th page  
#def add_status(request):   

#statusdbs = Statusdbs(ddate=request.POST['sdate'],dstatus=request.POST['sstatus'],dperson=request.POST['sperson'],dremarks=request.POST['sremarks'])
#   statusdbs.save()      statusdbs = Statusdbs(ddate=request.POST['sdate'],dstatus=request.POST['sstatus'],dperson=request.POST['sperson'],dremarks=request.POST['sremarks'])
#   statusdbs.save()   
#   return redirect(f'/status')
   
   




   
 #4th page     
def view_distribution(request):
   #ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   sdistributions = SDistributions.objects.all()
   return render(request, 'SDistribution.html', {'sdistribution' : sdistributions})  
   #return render(request, 'SDistribution.html', {'ibrgy': ibrgy_ ,'sdistribution' : sdistributions})     
    

def add_distribution(request):   
   sdistributions = SDistributions(dmode=request.POST['bmode'],dtype=request.POST['btype'],dlocation=request.POST['blocation'])
   sdistributions.save()
   
   return redirect('/distribution')
      

def s_about(request):     
   return render(request, 'about.html') 
 
# #5th page     
#def view_status(request): 
#   statusdbs = Statusdbs.objects.all()
#   return render(request, 'StatusDB.html', {'statusdb' : statusdbs})  


#data ng 5th page  
#def add_status(request):   

#statusdbs = Statusdbs(ddate=request.POST['sdate'],dstatus=request.POST['sstatus'],dperson=request.POST['sperson'],dremarks=request.POST['sremarks'])
#   statusdbs.save()      statusdbs = Statusdbs(ddate=request.POST['sdate'],dstatus=request.POST['sstatus'],dperson=request.POST['sperson'],dremarks=request.POST['sremarks'])
#   statusdbs.save()   
#   return redirect(f'/status')
   
   
   
   
 #CRUD
def edit(request, id):
   ibrgys = IBrgy.objects.get(id=id)
   context = {'ibrgys': ibrgys}
   return render(request, 'edit.html', context)
 
def update(request, id):
   ibrgy = IBrgy.objects.get(id=id)
   ibrgy.mncplty = request.POST['Municipality']
   ibrgy.bname = request.POST['Brgy']
   ibrgy.bID = request.POST['BrgyID']
   ibrgy.save()
   return redirect('/')
 
def delete(request, id):
   ibrgy = IBrgy.objects.get(id=id)
   ibrgy.delete()
   return redirect('/')    
  
  
  
def modify(request, id):
   sdistributions = SDistributions.objects.get(id=id)
   context = {'sdistribution': sdistributions}
   return render(request, 'remove.html', context)
 
def mupdate(request, id):
   sdistribution = SDistributions.objects.get(id=id)
   sdistribution.dmode = request.POST['bmode']
   sdistribution.dtype = request.POST['btype']
   sdistribution.dlocation = request.POST['blocation']
   sdistribution.save()
   return redirect('/distribution')
 
def remove(request, id):
   sdistribution = SDistributions.objects.get(id=id)
   sdistribution.delete()
   return redirect('/distribution')    
  


def dtmanipulation(request):
   
    #Creating a data
    ibrgy= IBrgy(mncplty="Dasmariñas City", bname="Brgy. Victoria", bID="301185")
    ibrgy.save()
    
    #Read All data
    ibrgy = IBrgy.objects.all()
    result = 'Printing all barangay entries in model: <br>'
    for x in objects:
        res += x.bname+"<br>"
        
    #Read a specific data    
    ibrgy = IBrgy.objects.get(id="Brgy")   
    res += 'Printing One entry <br>'
    res += ibrgy.Brgy
      
    #Delete a data
    res += '<br> Deleting an entry <br>'
    ibrgy.delete()
    
    bresidents = BResidents.objects.get(rname = 'Sasuke Uchiha')
    ibrgy.radd = "B 7 L 7"
    ibrgy.save()
    res = ""
    
    #Filtering data:
    qs = BResidents.objects.filter(rname = "Sasuke Uchiha")
    res += "Found: %s results<br>"%len(qs)
    
    #ordering results
    qs = IBrgy.objects.order_by("mncplty")
    for x in qs:
        res += x.bname + x.bID +'<br>'

         
'''    



#3rd page     
def view_beneficiary(request, ibrgy_id): 
   #bresidents = BResidents.objects.all() 

   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   return render(request, 'SBeneficiary.html', {'ibrgy': ibrgy_,'bresidents' : bresidents}) 
   
   
  
   
#data ng 3rd page  
def add_beneficiary(request, ibrgy_id):    
   #ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   #bresident_ = BResidents.objects.get(id=bresident_id)
   SBeneficiary.objects.create(sincome=request.POST['bincome'],scategory=request.POST['bcategory'],sclass=request.POST['bclass'],samount=request.POST['bamount'],ibrgy=ibrgy_)
 
   return redirect(f'/{ibrgy_.id}/beneficiary')  

        
@csrf_exempt
def update(request):
    if request.method == "POST":
     
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
      
        repo = git.Repo("test.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")       
        
        
        
        
        


   
#3rd page     
def view_beneficiary(request, ibrgy_id):    
   #sbeneficiarys = SBeneficiary.objects.all()
   #return render(request, 'SBeneficiary.html',{'sbeneficiarys' : sbeneficiarys})
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id) 
   return render(request, 'SBeneficiary.html', {'ibrgy': ibrgy_})   
  
   
#data ng 3rd page  
def add_beneficiary(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   SBeneficiary.objects.create(sincome=request.POST['bincome'],scategory=request.POST['bcategory'],sclass=request.POST['bclass'],samount=request.POST['bamount'],ibrgy=ibrgy_)
   
   return redirect(f'/{ibrgy_.id}/')  
   



def MainPage(request): 
   if request.method == 'POST':    
     #new_itext = request.POST['itext']  
     Info.objects.create(text=request.POST['itext'])
     #Info.objects.create(text=new_itext)  
     return redirect('/MNList/the-only-list-in-the-world/')
     
  #items = Item.objects.all()
  #return render(request, 'mynotes.html', {'items': items}) 
   return render(request, 'mynotes.html') 
   
def MainPage(request): 
   item = Item()   
   item.text = request.POST.get('item_text', '')    
   item.save()
   
   return render(request, 'mynotes.html', { 
        'new_item_text': item.text
   })
   
   else:       
     new_itext = '' 
   return render(request, 'mynotes.html', {        
    'new_itext': new_itext,     
})
   
'''
