

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jsonp.renderers import JSONPRenderer
from django.http import HttpResponse
import requests

class Multiply(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        try:
            first_number = float(request.GET.get('a'))
            second_number = float(request.GET.get('b'))
            r = first_number*second_number
            return post(r)
            '''
            return HttpResponse({'result': res})
            '''
        except Exception as e:
            return HttpResponse({'result': 'there was an error ' + str(e)})


class Divide(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        try:
            first_number = float(request.GET.get('a'))
            second_number = float(request.GET.get('b'))
            r=float(eval( 'first_number/second_number'))
            return post(r)
        except Exception as e:
            return Response({'result': 'there was an error ' + str(e)})


class Addition(APIView):
    renderer_classes = (JSONPRenderer,)
    @staticmethod
    def get(request):
        try:
            first_number = float(request.GET.get('a'))
            second_number = float(request.GET.get('b'))
            r = first_number+second_number
            return post(r)
        except Exception as e:
            return Response({'result':'there was an error ' + str(e)})


class Subtraction(APIView):
    rendered_classes = (JSONPRenderer,)
    @staticmethod
    def get(request):
        try:
            first_number = float(request.GET.get('a'))
            second_number = float(request.GET.get('b'))
            r =first_number-second_number
            return post(r)
        except Exception as e : 
            return Response({'result':'there was an error'+ str(e)})

def post(result):
    html ="<html><body>result is %s. </body></html>" %result
    return HttpResponse(html)
    '''con = requests.post('http://127.0.0.1:8000/', data=result)
    con.read()
    '''
