from django.shortcuts import render, HttpResponse
from datetime import datetime as dt
from django.views.generic import TemplateView

# Create your views here.
def getNowTime() -> dict[str, str]:
    nowString = dt.now().strftime("%Y/%m/%d %H:%M:%S")
    print(nowString)
    return {"time": nowString, "title": "No Title"}


def index(request) -> HttpResponse:
    props = getNowTime()
    props["title"] = "index"
    return render(request, "index.html", props)


class Test(TemplateView):
    template_name = "index.html"

    def __init__(self):
        props = getNowTime()
        props["title"] = "index"
        self.props = props

    def get(self, request, **kwargs):
        return self.render_to_response(self.props)
