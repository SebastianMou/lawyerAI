from django.shortcuts import render,get_object_or_404
from api.models import ContractProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def chats(request):
    return render(request, 'chats.html')

def contracts(request):
    return render(request, 'documents/contracts.html')

def contract(request, pk):
    # Retrieve the ContractProject object based on its primary key (pk)
    contract = get_object_or_404(ContractProject, pk=pk)
    contract = {
        'contract': contract,
    }
    return render(request, 'documents/contract.html', contract)
