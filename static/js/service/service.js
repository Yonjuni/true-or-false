'use strict';

angular.module('BackendService', [])
    .factory('Backend', function ($http) {
           return {
               loadQuestion: function (id) {
                   return $http({
                       method: "POST",
                       url: '/loadQuestions',
                       data: 'id=' + id,
                       headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                   });
               }
           }
    });