from django.shortcuts import render,HttpResponse
import string,random
from captchaapp.captcha.image import ImageCaptcha
# Create your views here.

#生成验证码
def getcaptcha(request):
    image = ImageCaptcha()
    codes = random.sample(string.ascii_letters+string.digits,4)
    codes = "".join(codes)
    print(codes)
    request.session['codes']=codes
    data = image.generate(codes)
    # print(data)
    return HttpResponse(data,'image/png')