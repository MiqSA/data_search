def response_api(code, data, error_name=None):
    codes_messages = {
        200: "Success!",
        400: "Bad request.",
    }
    if code in codes_messages.keys():
        msg = codes_messages[code]
    else:
        try:
            msg = error_name
            code = code
        except:
            msg = 'Error!'
            code = 404
    if type(data) != list:
        data = [data]
    response = {'message': msg, 'results': data, 'status': code}, code

    return response