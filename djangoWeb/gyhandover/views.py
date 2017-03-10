from django.shortcuts import render, HttpResponse
from .models import GYHandover


# Create your views here.
def upload_img(request):
    if request.method == 'POST':
        img_obj = request.FILES.getlist('img')
        if img_obj == None:
            return HttpResponse('file not existing in the request')
        new_img = GYHandover(
            handover_img=img_obj
        )
        new_img.save()
        return HttpResponse('Upload Succeed!')
    return render(request, 'gyhandover/gyuploadimg.html')


def show_img(request):
    imgs = GYHandover.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'gyhandover/gyshowimg.html', content)
