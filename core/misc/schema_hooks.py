def remove_admin_routes(endpoints):
    return [
        (path, path_regex, method, callback)
        for (path, path_regex, method, callback) in endpoints
        if not path.startswith('/admin/')
    ]

def remove_docs_routes(endpoints):
    return [
        (path, path_regex, method, callback)
        for (path, path_regex, method, callback) in endpoints
        if not path.startswith('/docs/')
    ]
