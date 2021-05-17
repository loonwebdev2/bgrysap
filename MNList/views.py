#from django.http import HttpResponse    
from django.shortcuts import redirect, render
from MNList.models import Info, IBrgy

def MainPage(request): 
     infos = Info.objects.all()
     return render(request, 'BSMS.html',{'infos' : infos})
   
def add_info(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   Info.objects.create(textFM=request.POST['addFM'],textRS=request.POST['addRS'],textAdd=request.POST['addadd'], ibrgy=ibrgy_)
   return redirect(f'/MNList/{ibrgy_.id}/')    
   
def view_ibrgy(request, ibrgy_id):    
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   return render(request, 'SInfo.html', {'ibrgy': ibrgy_})
   
def new_ibrgy(request):   
  
	 
    #newCar = IBrgy.objects.create(bname=request.POST['Brgy'],bID=request.POST['BrgyID'],ibrgy=newCar)
    #return redirect(f'/MNList/{newCar_.id}/')
    
    #newibrgy_ = IBrgy.objects.create(bname=request.POST['Brgy'],bID=request.POST['BrgyID'],ibrgy=newibrgy_)
    #return redirect(f'/MNList/{newibrgy_.id}/') 
  
   ibrgy_ = IBrgy.objects.create()
   Info.objects.create(ibrgy=ibrgy_)
   return redirect(f'/MNList/{ibrgy_.id}/')
    
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
        res == x.Name+"<br>"
        
    #Read a specific data    
    cname = IBrgy.objects.get(id="19")   
    res += 'Printing One entry <br>'
    res += cname.Address
      
    #Delete a data
    res += '<br> Deleting an entry <br>'
    cname.delete()
    
    ibrgy = IBrgy.objects.get(name = 'Sasuke Uchiha')
    ibrgy.Number = "09954626390"
    ibrgy.save()
    res = ""
    
    #Filtering data:
    qs = Info.objects.filter(name = "Sasuke Uchiha")
    res += "Found: %s results<br>"%len(qs)
    
    #ordering results
    qs = IBrgy.objects.order_by("Address")
    for x in qs:
        res += x.Name + x.Address +'<br>'
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
