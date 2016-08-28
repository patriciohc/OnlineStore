var app = angular.module('appProducts', []);
// configuracion para compatibilidad con python
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('mainController', function($scope, $http) {
    // obtencion de catalogo de categorias
    $scope.product = {};
    var fillCmbCategories = function(resquest){ 
        $scope.categories = resquest; 
    }
    //creacion de nuevo producto
    var productoReistrado = function(resquest){
        $scope.product = resquest;
        console.log(resquest);
    }
    //subida de imagen
    var imagenSubida = function(resquest){
        console.log(response);
    }
    var llenadoTablaProductos = function (resquest){
        $scope.products = resquest;
    }
    var setUrlImages = function(resquest){
        console.log(resquest);
        $scope.images = resquest
        for (var i = 0; i < $scope.images.length; i++){
            var url = $scope.images[i].image;
            $scope.images[i].image = url.replace("localhost:8000/image/image", "localhost:8080/image");
        }
        actEvet();
    }

    $http(tools.getSettings("GET", "/categories/")).success(fillCmbCategories);
    //tools.get("/images/?product=" + $scope.product.id, setUrlImages);
    $http(tools.getSettings("GET", "/product/")).success(llenadoTablaProductos);
    $scope.addProduct = function(){
        //var fileImage = document.getElementById("imageUpload").files[0];
        //var form = new FormData();
        // registro de producto
        $http(tools.getSettings("POST", "/product/", $scope.product )).success(productoReistrado).error(
            function(err)
            {
                console.log(err);
            });
        // subida de imagen
        //form.append("product", $scope.product);
        //form.append("image", fileImage);
        //tools.post("/image/", form, imagenSubida );
    }

    $scope.setProduct = function(tr){
        $scope.product = tr.p;
        $http(tools.getSettings("GET", "/image/?product=" + $scope.product.id)).success(setUrlImages);
        console.log(tr);
    }
    $scope.uploadImage = function(){
        var inputFile = document.getElementById("imageUpload");
        var functionSucces = function(resquest){
            //tools.get("/images/?product=" + $scope.product.id, setUrlImages);
            $http(tools.getSettings("GET", "/image/?product=" + $scope.product.id)).success(setUrlImages);
            //$scope.images = resquest;
            console.log(resquest)
        }
        if (!('files' in inputFile)){
            console.log("no hay imagenes por subir");
            return;
        }
        if (inputFile.files.length == 0){
            console.log("no hay imagnes por subir");
            return;
        }
        if ($scope.product.id == null || typeof($scope.product.id) == 'undefined'){
            console.log("el producto no esta regisrado");
            return;
        }
        var form = new FormData();
        form.append("product", $scope.product.id);
        form.append("image", inputFile.files[0]);
        tools.post("/image/", form, functionSucces);
    }

});


/*function onClickImage(){
        $('.modal-body').empty();
        var title = $(this).parent('a').attr("title");
        $('.modal-title').html(title);
        $($(this).parents('div').html()).appendTo('.modal-body');
        $('#myModal').modal({show:true});
}*/

$(document).ready(function() {
    $('.thumbnail').click(function(){
        $('.modal-body').empty();
        var title = $(this).parent('a').attr("title");
        $('.modal-title').html(title);
        $($(this).parents('div').html()).appendTo('.modal-body');
        $('#myModal').modal({show:true});
    });
});

function actEvet(){
        $('.thumbnail').click(function(){
        $('.modal-body').empty();
        var title = $(this).parent('a').attr("title");
        $('.modal-title').html(title);
        $($(this).parents('div').html()).appendTo('.modal-body');
        $('#myModal').modal({show:true});
    });
}