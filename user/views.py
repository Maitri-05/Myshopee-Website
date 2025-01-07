from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
       
class UserCls:
    def registerLogin(self,request):
        if request.method == "GET":
            return render(request,"product_files/registration.html")
        else:
            return render(request,"product_files/404.html")
  
    @csrf_exempt
    def register_user(self,request):
        if request.method =="POST":
            if request.POST.get("name") is not None and request.POST.get("name")!="" and request.POST.get("email") is not None and request.POST.get("email")!="" and request.POST.get("password") is not None and request.POST.get("password")!="" and request.POST.get("phone") is not None and request.POST.get("phone")!="" and request.POST.get("country") is not None and request.POST.get("country")!="" and request.POST.get("city") is not None and request.POST.get("city")!="":
                
                createClient = Users.objects.create(
                name = request.POST.get("name"),
                email = request.POST.get("email"),
                password = request.POST.get("password"),
                phone = request.POST.get("phone"),
                country = request.POST.get("country"),
                city = request.POST.get("city"),
                status = "Active",
                )
            
                if createClient:
                    return JsonResponse({"message":"User Registered successfully"})
                else:
                    return JsonResponse({"message":"Something went wrong"})
            else:
             return JsonResponse({"message":"one or more data is not given"})
        else:
            return JsonResponse({"message":"only POST request is allowed"})

        
    def login_user(self,request):
        if request.method == "POST":
            if request.POST.get("username") is not None and request.POST.get("username")!="" and request.POST.get("password") is not None and request.POST.get("password")!="":
                username = request.POST["username"]
                password = request.POST["password"]
                try:
                    fetchUser = Users.objects.get(email = username, password = password, status = "active")
                    name = fetchUser.name
                    return JsonResponse({"message":"User logged in successfully!","name":name})
                    def productPage(self,request):
                        context={"message":"Welcome to My Shopee!"}
                        return render(request,"product_files/product.html",context)
                except Users.DoesNotExist:
                    return JsonResponse({"message":"Username or password is incorrect"})
            else:
                return JsonResponse({"message":"one or more data is not given"})
        else:
            return JsonResponse({"message":"only POST request is allowed"})
    
    
    
    
        
    
        
        
    