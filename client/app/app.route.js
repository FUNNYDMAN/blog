function mainRouterProvider($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('home', {
            url: '/',
            views: {
                'header': {
                    template: require('./shared/header/header.tmp.html')
                },
                'content': {
                    template: require('./components/home/home.tmp.html'),
                    controller: 'homeController'
                },
                'footer': {
                    template: require('./shared/footer/footer.tmp.html')
                }
            }

        })
}

module.exports = mainRouterProvider;