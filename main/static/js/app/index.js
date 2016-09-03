var token = null;


var app = angular.module('mainApp', []);
// configuracion para compatibilidad con python
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});


// productos agregados al carrito de compras
app.factory("carrito", function(){
    var idsProdIncar = tools.getCookie("productos");
    if (idsProdIncar != ""){
        return JSON.parse(idsProdIncar);
    } else {
        return [];
    }
});


app.controller('menuController', function($scope, $http, carrito) {

    $scope.carrito = carrito;
});





window.onload = function (){
    updateBanner();
};

function updateBanner(){
    var token = tools.getCookie("token");
    if (token == null || token == ""){
        $("#ulLogin").show();
        $("#ulSession").hide();
        $("#liRegProd").hide();
        return; 
    }
    user = session.getUser();
    if(user == "root") {
        $("#lbNameuser").html(user);
        $("#ulLogin").hide();
        $("#ulSession").show();
        $("#liRegProd").show();
        $('#login-modal').modal('hide');
    }
}


// var app = angular.module('appLogin', []);
// app.controller('formLogin', function($scope, $http) {
//     $scope.login = function() {
//         var user = {
//             username : $scope.user,
//             password : $scope.password,
//         };
//         tools.putCookie("user", $scope.user);
//         var url = "/token-auth/";
//         tools.post($http, url, user, session.init, session.errorLogin);
//         //alert($scope.user +" " + $scope.password);
//     };
// });


var session = {
    user: null,    
    login: function(){
        user = {
            username: $("#username").val(),
            password: $("#password").val(),
        }
        var url = "/token-auth/";
        $.ajax({
                type: "POST",
                contentType: "application/json; charset=utf-8",
                url: url,
                data: JSON.stringify(user),
                async: false,
                dataType: "json",
                success: session.init,
                error: session.errorLogin
        });
    },
    init: function(sessionToken){
        var token = sessionToken.token;
        if (token == null) {
            return false;   
        }
        tools.putCookie("user", user.username);
        tools.putCookie("token", token);
        updateBanner();
    },

    close: function(){
        tools.deleteCookie("user");
        tools.deleteCookie("token");
        updateBanner();
    },

    getUser: function(){
        var user = tools.getCookie('user');
        return user;
    },

    errorLogin: function (err){
        //if (err.status == 400){
            tools.deleteCookie('user');
            alert(err);
            //tools.msgError("usuario no registrado!");
        //}
    }

}
