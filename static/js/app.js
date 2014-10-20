'use strict';

var trueOrFalseApp = angular.module(
    "TrueOrFalse",
    [
        "ngAnimate",
        "ngRoute"
    ]).config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        $routeProvider.
            when('/', {templateUrl: 'partials/introduction.html', controller: 'introductionCtrl'}).
            when('/question', {templateUrl: 'partials/question.html', controller: 'questionCtrl'}).
            otherwise({templateUrl: 'partials/introduction.html', controller: 'introductionCtrl'});
        // use the HTML5 History API
        $locationProvider.html5Mode(true).hashPrefix('!');
    }]);