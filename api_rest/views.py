from rest_framework import viewsets
from rest_framework import generics
from main.models import Product, Category, Image
from api_rest.serializers import ProductSerializer, CategorySerializer, ImageSerializer
from rest_framework import permissions
from rest_framework.response import Response
from permissions import isAdmin
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
	lookup_field = "id"

	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ("category", )

	#permission_classes = (isAdmin, )

	# def get_queryset(self):
	# 	try:
	# 		category = self.kwargs['category']
	# 		queryset = Product.objects.filter(category=category)
	# 	except KeyError:
	# 		queryset =  Product.objects.all()
	# 	return queryset

	# def list(self, request, *aargs, **kwargs):
	# 	print request.user
	# 	return super(ProductList, self).list(request, *aargs, **kwargs)

class ImageViewSet(viewsets.ModelViewSet):
	serializer_class = ImageSerializer
	queryset = Image.objects.all()
	lookup_field = "id"
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('product',)

class CategoryList(generics.ListCreateAPIView):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()
	#permission_classes = (isAdmin,)

	def list(self, request, *aargs, **kwargs):
		print request.user
		return super(CategoryList, self).list(request, *aargs, **kwargs)

	#permission_classes = (permissions.IsAdminUser, )



#class UserList(generics.ListAPIView):
#	serializer_class = UserSerializer

#	def get_queryset(self):
#		queryset = User.objects.all()
		#username = self.request.query_params.get('name_user', None)
		#queryset = queryset.filter(name_user=username)
		# try:
		# 	username = self.kwargs['name_user']
		# 	queryset = User.objects.filter(name_user=username)
		# except KeyError:
		# 	queryset =  User.objects.all()
#		return queryset

	# def get(self, request, format=None):
	# 	users = User.objects.all()
	# 	serializer = UserSerializer(users, many=True)
	# 	return Response(serializer.data)

	# def post(self, request, format=None):
	# 	serializer = UserSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class UserDetail(APIView):
#	pass
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# first we define the serializers