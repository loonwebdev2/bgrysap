#from django.http import HttpResponse    
from django.shortcuts import redirect, render
from MNList.models import BResidents, IBrgy, SBeneficiary, SDistributions, StatusDB

def MainPage(request): 
     ibrgys = IBrgy.objects.all()
     return render(request, 'BSMS.html',{'ibrgys' : ibrgys})
     
  
def add_info(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   BResidents.objects.create(rname=request.POST['addFM'],rrelation=request.POST['addRS'],radd=request.POST['addadd'], ibrgy=ibrgy_)
   return redirect(f'/MNList/{ibrgy_.id}/')    
   
def view_ibrgy(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   return render(request, 'SInfo.html', {'ibrgy': ibrgy_})
   
def new_ibrgy(request):   
  
	 
    #newCar = IBrgy.objects.create(bname=request.POST['Brgy'],bID=request.POST['BrgyID'],ibrgy=newCar)
    #return redirect(f'/MNList/{newCar_.id}/')
    
    newibrgy_ = IBrgy.objects.create(mncplty=request.POST['Municipality'],bname=request.POST['Brgy'],bID=request.POST['BrgyID'])
    return redirect(f'/MNList/{newibrgy_.id}/') 
  
   #ibrgy_ = IBrgy.objects.create()
   #Info.objects.create(ibrgy=ibrgy_)
   #return redirect(f'/MNList/{ibrgy_.id}/')
    
   #return redirect('/MNList/the-only-list-in-the-world/')
   #Info.objects.create(text=request.POST['itext'])
   #return redirect('/MNList/the-only-list-in-the-world/')
   #return redirect('/MNList/the-only-list-in-the-world/')

def dtmanipulation(request):
   
    #Creating a data
    ibrgy= IBrgy(Brgy="Brgy. Victoria", BrgyID="301185")
    ibrgy.save()
    
    #Read All data
    ibrgy = IBrgy.objects.all()
    result = 'Printing all entries in Carrier model: <br>'
    for x in objects:
        res == x.addFM+"<br>"
        
    #Read a specific data    
    cname = IBrgy.objects.get(id="Brgy")   
    res += 'Printing One entry <br>'
    res += cname.Address
      
    #Delete a data
    res += '<br> Deleting an entry <br>'
    cname.delete()
    
    ibrgy = IBrgy.objects.get(name = 'Sasuke Uchiha')
    ibrgy.addadd = "B 7 L 7"
    ibrgy.save()
    res = ""
    
    #Filtering data:
    qs = BResidents.objects.filter(name = "Sasuke Uchiha")
    res += "Found: %s results<br>"%len(qs)
    
    #ordering results
    qs = IBrgy.objects.order_by("Address")
    for x in qs:
        res += x.addFM + x.addadd +'<br>'
'''      

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
