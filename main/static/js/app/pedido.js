

app.controller('pedidoController', function($scope, $http, carrito) {
    $scope.addProductsInCar = [];
    init();

    function init(){
        for (var i in carrito){
            $http(tools.getSettings("GET", "/product/"+carrito[i])).success(function(request){
                $scope.addProductsInCar.push(request);
            });
        }
    }

});