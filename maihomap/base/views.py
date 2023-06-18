from django.shortcuts import render
from base.models import Contact
from base.models import Owner
from django.shortcuts import redirect
# from base.models import Owner
from django.db.models import Q
import requests

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
a=28.248767785991863
b=83.98629856004847
a =False
image="/static/img/placeholder.png"
def index(request):
    #owner.objects.raw("select longitude,latitude from base_Owner where longitude like '28.24%' and latitude like '83.98%'")
    search_query = '28'
    search_query2 = '83'

    results = Owner.objects.filter(Q(latitude__contains=search_query)|Q(latitude__contains=search_query2))
    #if a==False:
    image="static/img/blacklogo.png"
    image2="static/img/placeholder.png"


   
       
    coordinates = []
    coordinates2=[]
    for result in results:
      
        coordinates.append({"Longitude": result.longitude, "Latitude": result.latitude})

    print(coordinates)
    if request.method=="GET":
          search=request.GET.get("search")
          print(search)
          var=str(search)
          if search :
    
            url = f'https://overpass-api.de/api/interpreter?data=[out:json];area[name="Pokhara"];node(area)["amenity"="{search}"];out;'
            response = requests.get(url)
            
            image="static/img/blacklogo.png"

                # Check the response status
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

        # Process the data
            for result in data['elements']:
                name = result.get('tags', {}).get('name', 'N/A')
                latitude = result.get('lat', 'N/A')
                longitude = result.get('lon', 'N/A')
                coordinates2.append({"Longitude": longitude, "Latitude":latitude})
                
            
    

    return render(request,'index.html',{"coordinates":coordinates,"coordinates2":coordinates2,'image':image,"image2":image2,"search":var})

def owner(request):
    if request.method == 'POST':
        houseloc = request.POST.get('location')
        
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('description')
        rentprice = request.POST.get('rentPrice')
        noroom = request.POST.get('numRooms')
        name = request.POST.get('ownerName')
        select = request.POST.get('select')
        
        latitude=28.248767785991863
        longitude=83.98629856004847

        # Create a new Contact instance
        contact = Owner(
            latitude=latitude,
            longitude=longitude,
            email=email,
            phone=phone,
            desc=desc,
            rentprice=rentprice,
            noroom=noroom,
            name=name,
            newrequest=0
        )
        print(request.POST )

        # Save the Contact instance
        contact.save()
        context={"name":name}
        return render(request,"saved.html",context)
    return render(request,"ownerpage.html")

# def gmc(request):
#     if request.method == 'POST':
#         data=

def endpoint_view(request):
    if request.method == 'GET':
            # Retrieve the variables from the POST request
            payload = request.GET
            
            # Process the payload data as needed
            variable1 = payload.get('var1')
            variable2 = payload.get('var2')
            a=variable1
            b=variable2

            print(variable1)
            print(variable2)
            print(payload)
                

                
                # Retrieve more variables as needed
                
                # Process the dataS
                
                # Return a JSON response
            response_data = {'message': 'Success',"var1":variable1,"var2":variable2}
            return JsonResponse(response_data)
            
    else:
            # Handle other HTTP methods if needed
        return HttpResponse("cannot get coordinates")


def experiment(request):
        return render(request,"experiments.html")

def signin(request):
    if request.method=="GET" and request.GET.get('phone_signup')!=None:
        name = request.GET.get('username_signup')
        phone = request.GET.get('phone_signup')
        email = request.GET.get('email_signup')
        username=f'{name}'
        password=request.GET.get('password_signup')
       
        print(name,email,phone,password)
        try:
            user = User( email=email, username=name, password=password)
            user.save()
            print("sucess")
        except:
            print("cannot save")
        messages.success(request,"Your accout has been Created")
        return render(request,"index.html")

        if request.method=="get"  and request.GET.get('phone_signup')!=None and request.GET.get('username_signup')==None:
            name = request.GET.get('username_signin')
            
            usernamel=f'{name}'
            passwordl=request.GET.get('password_signin')
            print(usernamel,passwordl)


    return render(request,"sign_in.html")

def listbuilding(request):
    owner_obj=Owner.objects.get(id=1)
    
    print(owner_obj.phone)
    return render(request,"cards.html")

def index2(request):
    #import data
     owner_obj=Owner.objects.get(id=8)
     context={"owner":owner_obj.name,"email":owner_obj.name,"phone":owner_obj.phone,"desc":owner_obj.desc,"rentprice":owner_obj.rentprice,"noroom":owner_obj.noroom,}
     print(context)
     return render(request,"index-2.html",context)


def getcoordinates(request):
    return render(request,"getcoordinates.html")

def notify(request):
     a=request.user.id
     
     print(a)
     Owner.objects.filter(name=request.user).update(newrequest=a)
     return JsonResponse({"hello":a})
    #  name=request.Get.ge('name')
    #  obj=Owner.objects.filter(name="Terry")

def customer(request):
     return render(request,"customer.html")

     


