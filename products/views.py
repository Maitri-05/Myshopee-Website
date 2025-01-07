from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product,Category
from .forms import CategoryForm
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from myshopee import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class ProductClass:
  def productPage(self,request):
    products = []
    fetchAllProducts = Product.objects.all()
    showName = False
    name = ""
    if request.session.get("client_id") is not None and request.session.get("client_id") != "":
      showName = True
      name = request.session.get("username")
    for i in fetchAllProducts:
      products.append({"id":i.id,"name":i.product_name,"price":i.product_price,"thumbnail":i.product_thumbnail,"description":i.product_description,"min_order":i.min_order_quantity})
    # print("=======================",products)
    context={"message":"Welcome to My Shopee!","products":products,"name":name,"showName":showName}
    return render(request,"product_files/product.html",context)
  
  # product detail function
  def product_detail(self,request,id):
    try:
      product = Product.objects.get(id=id)
    except Product.DoesNotExist:
      context = {'message':"Product not found!"}
      return JsonResponse(request, "product_files/product.html",context)
    data={"id":id,"name":product.product_name,"price":product.product_price,"thumbnail":product.product_thumbnail,"description":product.product_description,"min_order":product.min_order_quantity}
    
    return render(request,'product_files/product_detail.html',{'product':data})
  
  def get_img_path(self,foldername,mediapath):
      return os.path.join(foldername, mediapath)
  
  def client_category_page(self,request):
    if request.method == "GET":
      return render(request,"product_files/addCategory.html")
    else:
      return render(request,"404.html")
  @csrf_exempt 
  
  def add_category(self,request):
      if request.method == "POST":
          if request.POST.get("category_name") is not None and request.POST.get("category_name")!="" and request.FILES.get("category_thumbnail") is not None:
                category_name = request.POST["category_name"]
                if request.FILES['category_thumbnail']:
                    category_thumbnail = request.FILES['category_thumbnail']
                    if not os.path.exists(self.get_img_path("category/",os.path.join(settings.MEDIA_ROOT, self.get_img_path("category/",'')))):
                        os.makedirs(self.get_img_path("category/",os.path.join(settings.MEDIA_ROOT, self.get_img_path("category/",''))))
                    fp = FileSystemStorage(os.path.join(settings.MEDIA_ROOT,"category/"))
                    imag_name=category_thumbnail.name
                    img_url="category/"+imag_name

                createCategory = Category.objects.create(
                    category_name = category_name,
                    category_thumbnail = img_url,
                )
                if createCategory:
                    if request.FILES['category_thumbnail']:
                        fp.save(imag_name, category_thumbnail)

                return JsonResponse({"message":"Category added successfully!"})
          else:
              return JsonResponse({"message":"one or more data is not given"})
      else:
          return JsonResponse({"message":"only POST request is allowed"})
        
  def show_category(self,request):
    categories = []
    fetchAllCategory = Category.objects.all()
    for i in fetchAllCategory:
      categories.append({"id":i.id,"name":i.category_name,"thumbnail":i.category_thumbnail,})
    context = {"categories":categories}
    return render(request, 'product_files/category.html',context)
  
  def delete_category(self,request,category_id): 
    # print(request.POST)
    try:
      categories = Category.objects.get(id=category_id).delete() 
      return JsonResponse({"message": "Category deleted successfully!","location": "show_category"})
    except ObjectDoesNotExist:
      return JsonResponse({"message":"Category not found!"})