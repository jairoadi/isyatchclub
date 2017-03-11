def Last5ProductsMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.last5 = request.session.get('last5')
        if request.last5 is None:
            request.last5 = []


        print('>>> START Middleware Function')

        #let Django continue the processing
        response = get_response(request)

        # Code to be executed for each request/response after the view is called.
        request.session['last5'] = request.last5[:5]
        
        print('>>> END Middleware Function')
        return response

    return middleware
