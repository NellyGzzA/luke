'use strict';

app.factory('Category', [
    '$resource',
    function ($resource) {
        return $resource(
            '/api/v1/categories'
        );
    }
])