'use strict';

trueOrFalseApp.controller("introductionCtrl", function ($scope, $location, $routeParams) {

    $scope.showQuestions = function () {
        $location.path('/question/' + $routeParams['id']);
    };

});