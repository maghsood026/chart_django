import json

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


def json_to_dict(filename):
    data = open(filename).read()
    jsonData = json.loads(data)
    return jsonData


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        mydict_pir = json_to_dict('PieChart.json')
        mydict_bar = json_to_dict('result.json')
        mydict = {k: v for k, v in sorted(mydict_pir.items(), key=lambda item: item[1], reverse=True)}

        Pielabels = list(mydict.keys())

        PiechartLabel = "malicious activity"
        Piechartdata = list(mydict.values())

        Barlabels = list(mydict_bar.keys())

        BarchartLabel = "malicious activity"
        Barchartdata = list(mydict_bar.values())
        data = {
            "Barlabels": Barlabels,
            "BarchartLabel": BarchartLabel,
            "Barchartdata": Barchartdata,
            "Pielabels": Pielabels,
            "PiechartLabel": PiechartLabel,
            "Piechartdata": Piechartdata,
        }
        return Response(data)
