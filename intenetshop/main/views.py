from django.shortcuts import render


def main(request, ):
    data = {'title': "Main page!!!",
            'values': ['Hello', '123', 'world']}

    return render(request, 'main/bais.html', data)


def about(request):
    return render(request, 'main/about.html')