'use strict';

trueOrFalseApp.controller("questionCtrl", function ($scope, Backend, $routeParams) {

    Backend.loadQuestion($routeParams['id']).success(function(data){

       var result = angular.fromJson(data);
       $scope.questionData = result;

    });

    $scope.clickButton = function (answer) {

    };

    $scope.dontKnow = function () {

    };

});