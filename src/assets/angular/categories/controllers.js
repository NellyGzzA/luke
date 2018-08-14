'use strict';

app.controller('CategoriesCtrl', function(Category) {
    var vm = this;
    vm.count = 0;
    vm.active = true;
    vm.pageSize = 10;
    vm.currentPage = 1;
    vm.categories = [];
    vm.activeText = 'Active';

    vm.getCategoryList = function() {
        var queryParams = {
            'page_size': vm.pageSize,
            'page': vm.currentPage,
            'active': vm.active
        };
        Category.get(queryParams).$promise.then(function(response) {
            vm.count = response.meta.pagination.count;
            vm.categories = response.results;
            return vm.categories;
        });
    };

    vm.changePage = function(page) {
        vm.currentPage = page;
        vm.getCategoryList();
    };

    vm.changeActive = function() {
        vm.active = !vm.active;
        vm.activeText = vm.active ? 'Active' : 'Inactive';
        vm.currentPage = 1;
        vm.getCategoryList();
    };

    vm.getCategoryList();

    return vm;
});

app.controller('CategoriesCreateCtrl', function($state, $scope, Category) {
    var vm = this;
    vm.message = '';
    vm.errors = [];

    vm.submitCategory = function(categoryId) {
        var params = {
            'title': vm.title,
            'active': vm.active ? true : false
        };
        Category.save(params).$promise.then(function(response) {
            vm.message = 'Categoría guardada correctamente';
        }, function(response) {
            $scope.validate = 'invalid';
            vm.errors = response.data;
        });
    };
});