
app.controller('homeController', function($scope, $http, carrito) {

    $scope.showHome = true;
    $scope.carrito = carrito;


    var listaProductos = function(request){
        console.log(request);
        $scope.showHome = true;
        $scope.listaProductos = request;
        for (var i = 0; i < $scope.listaProductos.length; i++ ){
            var images = $scope.listaProductos[i].images;
            for (var j = 0; j < images.length; j++){
                $scope.listaProductos[i].images[j].image = images[j].image.replace("localhost:8000/product/image", "localhost:8080/image"); 
            }
        }
    }

    var categories = function(request){
        $scope.categories = request;
    }

    $scope.updateList = function(){
        $http(tools.getSettings("GET", "/product/?category="+this.c.id)).success(listaProductos);            
    }

    $scope.details_product = function(){
        $scope.showHome = false;
        $scope.details = this.p;
    }

    $scope.addProductInCar = function(){
        $scope.carrito.push(this.p.id);
        tools.putCookie("productos", JSON.stringify($scope.carrito));
    }

    $http(tools.getSettings("GET", "/product/")).success(listaProductos);    
    $http(tools.getSettings("GET", "/categories/")).success(categories);    
      

});

