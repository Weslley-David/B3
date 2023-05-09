from django.http import Http404
from django.shortcuts import redirect, render
from accounts import models
from my_wallet.models import Investidor, Stock, Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Case, When
from django.db.models import Count

def index(request):
    user = request.user
    if user.is_authenticated:
        investidor = request.user.profile
        stocks_ranking = Stock.objects.annotate(
            num_transacoes=Count('transaction')).order_by('-num_transacoes')
        compras = Transaction.objects.filter(
            operacao='C', Investidor=investidor).count()

        vendas = Transaction.objects.filter(
            operacao='V', Investidor=investidor).count()

        total = vendas + compras

        context = {
            'stocks_ranking': stocks_ranking,
            'compras': compras,
            'vendas': vendas,
            'total': total
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
            transactions = Transaction.objects.filter(
                stock=stock, Investidor=investidor)
            # transactions = Transaction.objects.filter(Investidor=investidor, Stock = request.POST['codigo']).order_by('data')

        else:
            investidor = request.user.profile
            transactions = Transaction.objects.filter(
                Investidor=investidor).order_by('data')
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
    return render(request, template_name='my_wallet/detalhe.html', context=context)


@login_required
def edit(request, transaction: int):
    if request.method == 'POST':
        stock_id = request.POST['stock_id']
        transaction_req = Transaction.objects.get(pk=transaction)
        stock = Stock.objects.get(id=stock_id)

        transaction_req.operacao = request.POST['operation']
        transaction_req.stock = stock
        transaction_req.data = request.POST['date']
        transaction_req.corretagem = request.POST['brokerage']
        transaction_req.quantidade_de_acoes = request.POST['quantity']
        transaction_req.preco_unitario = request.POST['value_unit']
        transaction_req.data = request.POST['date']

        transaction_req.save()
        return redirect('transactions')
    else:
        transaction_res = Transaction.objects.get(pk=transaction)
        stocks = Stock.objects.all()
        context = {
            'transaction_res': transaction_res,
            'stocks': stocks
        }
        print('\n\n\n\n\n',transaction_res)
       
        return render(request, 'my_wallet/edit_transaction.html', context=context)
    

@login_required
def add_transaction(request):
    if request.method == 'POST':

        stock_id = request.POST['stock_id']

        stock = Stock.objects.get(id=stock_id)
        investidor = Investidor.objects.get(user=request.user.id)

        investment = Transaction(
            data=request.POST['date'],
            stock=stock,
            quantidade_de_acoes=request.POST['quantity'],
            preco_unitario=request.POST['value_unit'],
            operacao=request.POST['operation'],
            corretagem=request.POST['brokerage'],
            Investidor=investidor
        )
        investment.save()
        return redirect('transactions')
    else:
        stocks = Stock.objects.all()
        return render(request, 'my_wallet/add_transaction.html', {'stocks': stocks})


def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('transactions')
