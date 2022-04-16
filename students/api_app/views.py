from django.views import View
from django.http import JsonResponse,request,HttpResponse
import json
from .models import Studentresult
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')

class result(View):
    def post(self, request):
        data={}
        if request.method == 'POST':
            request_data=request.POST
            name = request_data["stu_name"]
                #     print(request_data["stu_name"])
            #data = json.loads(request.body.decode("utf-8"))
            
            rolno = request_data["roll_no"]
            prt = request_data["parents_name"]
            mon = request_data["mo"]
            sub = request_data["total_subjects"]
            re = request_data["results"]
            #grds = request_data["grd"]
            
            data_of_stu = {
                'stu_name': name,
                'rollno': rolno,
                'parents_name': prt,
                'mo':mon,
                'total_subjects':sub,
                'results':re,
                #'grd':grds
            }

            stu = Studentresult.objects.create(**data_of_stu)
            
            data = {
                "msg" : f"new Studentresult id : {stu.id}"
                }
            return JsonResponse(data,status=201)
        return JsonResponse(data,status=201)
    
    def get(self, request):
        stu_count = Studentresult.objects.count()
        ite = Studentresult.objects.all()
        stu_data = []
        for stu in ite:
            stu_data.append({
                'stu_name': stu.stu_name,
                'rollno': stu.rollno,
                'grd': stu.grd,
            })

        data = {
            'ite': stu_data,
            'count': stu_count,
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')    
class resultUpdate(View):
    def patch(self, request, stu_id):
        data = json.loads(request.body.decode("utf-8"))
        stu = Studentresult.objects.get(id=stu_id)
        stu.grd = data['grd']
        stu.save()

        data = {
            'message': f'{stu_id} has been updated'
        }

        return JsonResponse(data)    
    
    def delete(self, request, stu_id):
        item = Studentresult.objects.get(id=stu_id)
        item.delete()

        data = {
            'message': f'Item {stu_id} has been deleted'
        }

        return JsonResponse(data)
    
