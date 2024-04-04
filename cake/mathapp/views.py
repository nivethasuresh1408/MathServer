from django.shortcuts import render
def cylarea(request):
    context={}
    context['area'] = "0"
    context['R'] = "0"
    context['H'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        R = request.POST.get('Radius','0')
        H = request.POST.get('Height','0')
        print('request=',request)
        print('Radius=',R)
        print('Height=',H)
        area = 2 * 3.14 * int(R) * int(H) + 2*3.14*int(R)*int(R)
        context['area'] = area
        context['R'] = R
        context['H'] = H
        print('Area=',area)
    return render(request,'mathapp/mat.html',context)