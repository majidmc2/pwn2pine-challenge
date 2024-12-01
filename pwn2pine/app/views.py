import base64
import string
import random

from jinja2 import Environment
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(["GET"])
def index(request, id=None):
    # Challange ONE
    if id == 1:
        cookie = request.COOKIES
        if "color" in cookie and "value" in cookie:
            try:
                color_base64_bytes = cookie["color"].encode("ascii")
                color_string_bytes = base64.b64decode(color_base64_bytes)
                color = color_string_bytes.decode("ascii")
            except:
                color_list = ['red', 'blue', 'green']
                color = random.choice(color_list)

        else:
            color_list = ['red', 'blue', 'green']
            color = random.choice(color_list)

        jinja2 = Environment()
        color = jinja2.from_string(color).render()
        response = render(request, "ch1.html", {"color": color})

        color_value = color.encode("ascii")
        color_value_base64_bytes = base64.b64encode(color_value)
        color_cookie = color_value_base64_bytes.decode("ascii")
        response.set_cookie(key="color", value=color_cookie)
        response.set_cookie(key="value", value=''.join(random.choice(string.ascii_uppercase) for _ in range(42)))

        return response

    # Challange TWO
    if id == 2:
        return render(request, "ch2.html", {})

    if id == 3:
        cookie = "WMZFMKHTILTTGWQXCAIIYEORYSJOGBWFRSODEJNPAF"
        response = render(request, "ch3.html", {})
        response.set_cookie(key="ch3", value=cookie)
        return response


    else:
        return redirect("/1")

@require_http_methods(["GET"])
def callback(request):
    callback_param = request.GET.get("callback", None)
    id_param = request.GET.get("id", None)

    cookie = request.COOKIES.get("ch3", None)

    if callback_param is None or id_param is None or cookie is None or cookie != "WMZFMKHTILTTGWQXCAIIYEORYSJOGBWFRSODEJNPAF":
        return HttpResponse(status=400, content_type="application/javascript")
    else:
        if id_param == "admin":
            data = {
                "username": 'admin' + ''.join(random.choice(string.ascii_uppercase) for _ in range(4)),
                "email": "admin@pwn2pine.com",
                "password": ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
            }
        else:
            data = {}
        return HttpResponse(f"{callback_param}({data})", status=200, content_type="application/javascript")
