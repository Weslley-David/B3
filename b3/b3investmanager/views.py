from django.shortcuts import redirect, render

# Create your views here.
from django.http import Http404, HttpResponse
from .models import Code, Investment


def index(request):
    return render(request, "b3investmanager/index.html")


# list of codes and investments
def code_index(request):
    codes = Code.objects.all()
    context = {"codes": codes}
    return render(request, "b3investmanager/code_index.html", context)


def investment_index(request):
    investments = Investment.objects.all()
    context = {"investments": investments}
    return render(request, "b3investmanager/investment_index.html", context)

# create investment


def add_code(request):
    if request.method == 'POST':
        code_identifyer = request.POST['code_identifyer']
        code = Code(code_identifyer=code_identifyer)
        code.save()
        return redirect('code_index')
        # Redirect to success page
    else:
        # Render empty form
        return render(request, 'b3investmanager/add_code.html')


def add_investment(request):
    if request.method == 'POST':
        investment = Investment(
            date=request.POST['date'],
            investment_identifyer=request.POST['investment_identifyer'],
            Code=Code.objects.get(
                code_identifyer=request.POST['code_identifyer']),
            quantity=request.POST['quantity'],
            value_unit=request.POST['value_unit'],
            operation=request.POST['operation'],
            value_brokerage=request.POST['value_brokerage'],
            value_operation=request.POST['value_operation'],
            b3_rate=request.POST['b3_rate'],
            value_total=request.POST['value_total']
        )
        investment.save()
        # Redirect to success page
        return redirect('investment_index')
        # Redirect to success page
    else:
        # Render empty form
        codes = Code.objects.all()
        return render(request, 'b3investmanager/add_investment.html', {'codes': codes})


def delete_code(request, pk):
    code = Code.objects.get(pk=pk)
    code.delete()
    return redirect('code_index')

def delete_investment(request, pk):
    investment = Investment.objects.get(pk=pk)
    investment.delete()
    return redirect('investment_index')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
