from django.http import JsonResponse
from one_endpoint_rest_api.server_side import data_processing
from rest_framework.decorators import api_view


@api_view(['GET'])
def start_endpoint(request):
    """  The only endpoint the app works through  """
    result = data_processing(eval(list(request.query_params.dict())[0]))

    return JsonResponse(result, safe=False)
