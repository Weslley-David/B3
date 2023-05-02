from django.http import Http404
from django.shortcuts import redirect, render
from my_wallet.models import Investidor, Stock, Transaction
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    user = request.user
    if user.is_authenticated:
        investidor = request.user.profile

        # transactions = Transaction.objects.filter(Investidor=investidor)
        transactions = Stock.objects.all()
        context = {
            'transactions': transactions,
        }
        print('\n\n\n\n\n usuário está authenticado')
        return render(request, template_name='my_wallet/dashboard.html', context=context)
    else:
        print('\n\n\n\n\n usuário não está authenticado')
        return render(request, template_name='my_wallet/dashboard.html')

@login_required
def transactions(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST' and (request.POST['codigo'] != ''):
            investidor = request.user.profile
            stock = Stock.objects.get(codigo=request.POST['codigo'])
            transactions= Transaction.objects.filter(stock=stock, Investidor=investidor)
            # transactions = Transaction.objects.filter(Investidor=investidor, Stock = request.POST['codigo']).order_by('data')
            
        else:
            investidor = request.user.profile
            transactions = Transaction.objects.filter(Investidor=investidor).order_by('data')
        context = {
            'transactions': transactions,
        }
        # print('\n\n\n\n\n usuário está authenticado')
        return render(request, template_name='my_wallet/transactions.html', context=context)
    else:
        # print('\n\n\n\n\n usuário não está authenticado')
        return render(request, template_name='my_wallet/dashboard.html')

@login_required
def detail(request, transaction: int):
    try:
        transaction_req = Transaction.objects.get(pk=transaction)
        context = {
            'transaction_req': transaction_req,
        }
    except Transaction.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,template_name='my_wallet/detalhe.html', context=context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        data = request.POST
        stock_id = data.get('stock_id')
        print('\n\n\n\n\n\n\n')
        stock = Stock.objects.get(id=stock_id)
        investidor = Investidor.objects.get(user=request.user.id)

        investment = Transaction(
            data=timezone.now(),
            stock=stock,
            quantidade_de_acoes=request.POST['quantity'],
            preco_unitario=request.POST['value_unit'],
            operacao=request.POST['operation'],
            corretagem=0.5,
            Investidor=investidor
        )
        investment.save()
        return redirect('index')
    else:
        stocks = Stock.objects.all()
        return render(request, 'my_wallet/add_transaction.html', {'stocks': stocks})
    
def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('transactions')
