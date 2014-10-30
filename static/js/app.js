'use strict';

var trueOrFalseApp = angular.module(
    "TrueOrFalse",
    [
        "ngAnimate",
        "ngRoute",
        "BackendService"
    ]).config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
        $routeProvider.
            when('/:id', {templateUrl: '/static/partials/introduction.html', controller: 'introductionCtrl'}).
            when('/question/:id', {templateUrl: '/static/partials/question.html', controller: 'questionCtrl'}).
            when('/thanks/:id', {templateUrl: '/static/partials/thanks.html', controller: 'thanksCtrl'}).
            otherwise({templateUrl: '/static/partials/introduction.html', controller: 'introductionCtrl'});
        // use the HTML5 History API
        $locationProvider.html5Mode(true).hashPrefix('!');
    }]);