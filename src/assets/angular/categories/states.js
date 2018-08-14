'use strict';

app.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/index');

    $stateProvider.state({
        name: 'categories',
        url: ''
    })
    .state({
        name: 'categories.index',
        url: '/index',
        controller: 'CategoriesCtrl as vm',
        templateUrl: '/static/angular/categories/views/index.html'
    })
    .state({
        name: 'categories.create',
        url: '/create',
        controller: 'CategoriesCreateCtrl as vm',
        templateUrl: '/static/angular/categories/views/create.html'
    });
});