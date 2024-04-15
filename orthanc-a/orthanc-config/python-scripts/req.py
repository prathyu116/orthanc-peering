import orthanc
import pprint


def Filter(uri, **request):
    pprint.pprint(request)
    pprint.pprint(uri)
    pprint.pprint(uri == '/instances')
    if uri == '/instances':
        print('Extracted Cookie link:')
        return True
    return False
   
   

orthanc.RegisterIncomingHttpRequestFilter(Filter)