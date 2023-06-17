from django.shortcuts import render
from base.models import Contact
from base.models import Owner
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
def index(request):
   
    coordinates = [
    {"latitude": 28.248767785991863, "longitude": 83.98629856004847},
    {"latitude": 28.259071283420692, "longitude": 83.9791488647461},
    {"latitude": 28.246369554498177 , "longitude": 83.98497168545931},
    {"latitude": 28.261772096881458, "longitude": 83.95889282226562},
    {"latitude": 28.230187780248816, "longitude": 84.00179002120969}
    ]
        # coordinates={"latitude":[28.248767785991863,28.24876778599863,28.2487677859183,28.248767785991363, 28.24876778599863],"longitude":[ 83.98629856004847, 83.9862985600847, 83.9862985600447 83.9862985600847, 83.9862985604847]}


    return render(request,'index.html',{"coordinates":coordinates})

def owner(request):
    if request.method == 'POST':
        houseloc = request.POST.get('location')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('description')
        rentprice = request.POST.get('rentPrice')
        noroom = request.POST.get('numRooms')
        name = request.POST.get('ownerName')

        # Create a new Contact instance
        contact = Owner(
            houseloc=houseloc,
            email=email,
            phone=phone,
            desc=desc,
            rentprice=rentprice,
            noroom=noroom,
            name=name
        )

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
            if len(payload)==0:
                return render(request,"getcoordinates.html")
            else:
            # Process the payload data as needed
                variable1 = payload.get('var1')
                variable2 = payload.get('var2')

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
        return render(request,"getcoordinates.html")


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



