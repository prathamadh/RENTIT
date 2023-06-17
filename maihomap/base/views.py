from django.shortcuts import render
from base.models import Contact
from base.models import Owner

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import JsonResponse
def index(request):
    return render(request,'index.html')

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
    if request.method == 'POST':
            # Retrieve the variables from the POST request
            var3=request.POST
            variable1 = request.POST.get('variable1')
            variable2 = request.POST.get('variable2')
            
            # Retrieve more variables as needed
            
            # Process the dataS
            
            # Return a JSON response
            response_data = {'message': 'Success',"var1":variable1,"var2":variable2,"var3":var3}
            return JsonResponse(response_data)
    else:
            # Handle other HTTP methods if needed
        return render(request,"getcoordinates.html")


    # if request.method == 'POST':
    #     try:
    #         data = request.POST

    #         latitude = data.get('value1')
    #         longitude = data.get('value2')
    #         context={"lat":latitude,"lon":longitude}

    #         # Process the coordinates as needed
    #         # ...

    #         # Return a JSON response indicating success
    #         return render(request,"saved.html",context)
    #     except Exception as e:
    #         # Handle any errors
    #         return JsonResponse({'error': str(e)}, status=400)
    # return  render(request,"getcoordinates.html")

# def showdata(request):
#     context={}