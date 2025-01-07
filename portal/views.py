from django.shortcuts import render,redirect
from django.http import JsonResponse
from portal.models import Clients
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
import os
from django.core.files.storage import FileSystemStorage
from myshopee import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class PortalClass:
  
  # registration form data for new client database
  # CLIENT DETAILS --> Name , email , password , mobile_number , country , state
  @csrf_exempt
  def client_register(self,request):
    if request.method =="POST":
      if request.POST.get("name") is not None and request.POST.get("name")!="" and request.POST.get("email") is not None and request.POST.get("email")!="" and request.POST.get("password") is not None and request.POST.get("password")!="" and request.POST.get("mobile_number") is not None and request.POST.get("mobile_number")!="" and request.POST.get("country") is not None and request.POST.get("country")!="" and request.POST.get("city") is not None and request.POST.get("city")!="":
        
        createClient = Clients.objects.create(
          name = request.POST.get("name"),
          email = request.POST.get("email"),
          password = request.POST.get("password"),
          mobile_number = request.POST.get("mobile_number"),
          country = request.POST.get("country"),
          city = request.POST.get("city"),
          status = "Active",
        )
        if createClient:
          return JsonResponse({"message":"Client Registered successfully"})
        else:
          return JsonResponse({"message":"Something went wrong"})
      else:
        return JsonResponse({"message":"one or more data is not given"})
    else:
      return JsonResponse({"message":"only POST request is allowed"})
  
  # client register
  def portal_register(self,request):
    if request.method == "GET":
      return render(request,"portal_files/portalRegister.html")
    else:
      return render(request,"portal_files/404.html")
    
  # CLIENT LOGIN DETAILS --> userName(email) , password 
  def client_login(self,request):
    if request.method == "POST":
      if request.POST.get("username") is not None and request.POST.get("username")!="" and request.POST.get("password") is not None and request.POST.get("password")!="":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
          fetchClient = Clients.objects.get(email = username, password = password, status = "active")
          # print("===========================",fetchClient)
          name = fetchClient.name
          # return JsonResponse({"location":"client-product"})
          request.session["username"] = name
          request.session["client_id"] = fetchClient.id
          return JsonResponse({"message":"Client logged in successfully!","location":"/"})
          
        except Clients.DoesNotExist:
            return JsonResponse({"message":"Username or password is incorrect"})
      else:
        return JsonResponse({"message":"one or more data is not given"})
    else:
      return JsonResponse({"message":"only POST request is allowed"})
  
  # login form data for existing client access
  def portal_login(self,request):
    if request.method == "GET":
      return render(request,"portal_files/portalLogin.html")
    else:
      return render(request,"portal_files/404.html")
  
  # client logout
  def client_logout(self, request):
    if "client_id" in request.session:
      del request.session["client_id"]
      del request.session["username"]
      return JsonResponse({"message":"Client logged out successfully!","location":"/"})
    else:
      return JsonResponse({"message": "User is not logged in"})
  
# client product entry page
  def client_product(self,request):
    if request.method == "GET":
      return render(request,"portal_files/clientProduct.html")
    else:
      return render(request,"portal_files/404.html")

  # product image function
  def get_img_path(self,foldername,mediapath):
      return os.path.join(foldername, mediapath)
    
  @csrf_exempt
  # add product function
  def add_product(self,request):
      if request.method == "POST":
          if request.POST.get("product_name") is not None and request.POST.get("product_name")!="" and request.POST.get("product_price") is not None and request.POST.get("product_price") != "" and request.POST.get("product_description") is not None and request.POST.get("product_description") != "" and request.FILES.get("product_thumbnail") is not None and request.POST.get("min_order_quantity") is not None and request.POST.get("min_order_quantity") != "":
                product_name = request.POST["product_name"]
                product_price = request.POST["product_price"]
                product_description = request.POST["product_description"]
                # product_availability = request.POST["product_availability"]
                min_order_quantity = request.POST["min_order_quantity"]

                if request.FILES['product_thumbnail']:
                    product_thumbnail = request.FILES['product_thumbnail']
                    if not os.path.exists(self.get_img_path("products/",os.path.join(settings.MEDIA_ROOT, self.get_img_path("products/",'')))):
                        os.makedirs(self.get_img_path("products/",os.path.join(settings.MEDIA_ROOT, self.get_img_path("products/",''))))
                    fp = FileSystemStorage(os.path.join(settings.MEDIA_ROOT,"products/"))
                    imag_name=product_thumbnail.name
                    img_url="products/"+imag_name

                createProduct = Product.objects.create(
                    product_name = product_name,
                    product_price = product_price,
                    product_description = product_description,
                    # product_availability = product_availability,
                    product_thumbnail = img_url,
                    min_order_quantity = min_order_quantity,
                )
                if createProduct:
                    if request.FILES['product_thumbnail']:
                        fp.save(imag_name, product_thumbnail)

                return JsonResponse({"message":"Product added successfully!"})
          else:
              return JsonResponse({"message":"one or more data is not given"})
      else:
          return JsonResponse({"message":"only POST request is allowed"})

  # show all product function
  def show_products(self,request):
    products = []
    fetchAllProducts = Product.objects.all()
    for i in fetchAllProducts:
      products.append({"id":i.id,"name":i.product_name,"price":i.product_price,"thumbnail":i.product_thumbnail,"description":i.product_description,"min_order":i.min_order_quantity})
    context = {"products":products}
    return render(request, 'product_files/product.html',context)

  # edit existing product form function
  def edit_product(self,request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'portal_files/edit_product_data.html',context)
  
  # update function
  def update_product(self,request,product_id):
    if request.method == "POST":
          if request.POST.get("product_name") is not None and request.POST.get("product_name")!="" and request.POST.get("product_price") is not None and request.POST.get("product_price") != "" and request.POST.get("product_description") is not None and request.POST.get("product_description") != ""  and request.POST.get("min_order_quantity") is not None and request.POST.get("min_order_quantity") != "":
            product_id = request.POST["product_id"]
            product_name = request.POST["product_name"]
            product_price = request.POST["product_price"]
            product_description = request.POST["product_description"]
            min_order_quantity = request.POST["min_order_quantity"]
            
            Product.objects.filter(id=product_id).update(
                          product_name=product_name,
                          product_price=product_price,
                          product_description=product_description,
                          min_order_quantity=min_order_quantity
                      )
            return JsonResponse({"message":"Product Updated successfully!","location":"/"})
            
          else:
              return JsonResponse({"message":"one or more data is not given"})
    else:
        return JsonResponse({"message":"only POST request is allowed"})
      
  # delete function
  def delete_product(self,request,product_id): 
    print(request.POST)
    try:
      products = Product.objects.get(id=product_id).delete() 
      return JsonResponse({"message": "Product deleted successfully!","location": "/"})
    except ObjectDoesNotExist:
      return JsonResponse({"message":"Product not found!"})
    
  class New:
    pass