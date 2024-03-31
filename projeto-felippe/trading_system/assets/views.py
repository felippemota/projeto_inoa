from django.shortcuts import render
from .models import Asset, Quotation
import requests
from django.http import HttpResponse

# View para a página inicial
def index(request):
    assets = Asset.objects.all()  # Obtém todos os ativos do banco de dados
    # Renderiza o template 'index.html', passando os ativos como contexto
    return render(request, 'assets/index.html', {'assets': assets})

# View para atualizar as cotações
def update_quotations(request):
    assets = Asset.objects.all()  # Obtém todos os ativos do banco de dados
    for asset in assets:
        # Obtenha a cotação atual do ativo do Yahoo Finance (API Pública)
        response = requests.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{asset.name}?region=BR&lang=pt-BR&includePrePost=false&interval=2m&range=1d&corsDomain=br.financas.yahoo.com&.tsrc=finance')
        data = response.json()
        price = data['chart']['result'][0]['meta']['regularMarketPrice']

        # Crie uma nova cotação com o preço atual
        quotation = Quotation(asset=asset, price=price)
        quotation.save()

    # Retorna uma resposta HTTP indicando que as cotações foram atualizadas com sucesso
    return HttpResponse('Cotações atualizadas com sucesso.')
