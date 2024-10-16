from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import openai

from .models import ContractProject, AIHighlightChat
from .serializer import ContractProjectSerializer, AIHighlightChatSerializer

openai.api_key = settings.OPENAI_API_KEY

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        ## Contract projects
        'Contract Projects': '/contract-projects/',
        'Contract Project Detail View': '/contract-project-detail/<str:pk>/',
        'Contract Project Create': '/contract-project-create/',
        'Contract Project Update': '/contract-project-update/<str:pk>/',
        'Contract Project Delete': '/contract-project-delete/<str:pk>/',

        'Chat history': '/get-chat-history-contract/<str:contract_project_id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def contract_project(request):
    contracts = ContractProject.objects.filter(owner=request.user)
    serializer = ContractProjectSerializer(contracts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contract_project_detail(request, pk):
    contracts = ContractProject.objects.get(id=pk)
    serializer = ContractProjectSerializer(contracts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def contract_project_create(request):
    serializer = ContractProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)
    else:
        print(serializer.errors)  # Log errors to see what went wrong
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def contract_project_update(request, pk):
    contract = ContractProject.objects.get(id=pk)
    data = request.data.copy()  # Make a copy of the request data

    # Log the incoming data to check if it is being received correctly
    print('Incoming data:', data)

    # Ensure the description is not None
    if data.get('description') is None:
        data['description'] = ''  # Replace None with an empty string

    serializer = ContractProjectSerializer(instance=contract, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        print('Data saved successfully')  # Add this log to confirm successful save
        return JsonResponse(serializer.data, status=200)
    else:
        print('Serializer errors:', serializer.errors)  # Log errors to help debug
    
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def contract_project_delete(request, pk):
    contract = ContractProject.objects.get(id=pk)
    contract.delete()

    return Response('Contract project deleted successfully :)')

@api_view(['POST'])
def create_ai_chat_contract(request, contract_project_id):
    try:
        print(f"Request data: {request.data}")
        print(f"Contract Project ID: {contract_project_id}")
        
        # Get the contract project the AI chat is associated with
        contract_project = ContractProject.objects.get(id=contract_project_id)

        # Get the user, highlighted text, and instruction from the request data
        user = request.user
        highlighted_text = request.data.get('highlighted_text')
        instruction = request.data.get('instruction')

        # Generate AI response (using ChatCompletion API)
        prompt = f"Highlight: {highlighted_text}\nInstruction: {instruction}\n"
        
        # OpenAI's chat-based API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available in your plan
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract the AI's response from the 'choices' array
        ai_response = response.choices[0].message.content.strip()

        # Save AI chat in the database
        ai_chat = AIHighlightChat.objects.create(
            user=user,
            contract_project=contract_project,
            highlighted_text=highlighted_text,
            instruction=instruction,
            ai_response=ai_response
        )

        return JsonResponse({'ai_response': ai_response}, status=201)

    except ContractProject.DoesNotExist:
        return JsonResponse({'error': 'Contract project not found'}, status=404)
    except Exception as e:
        print(f"Error occurred: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def get_chat_history_contract(request, contract_project_id):
    try:
        # Get all chat messages related to the contract project
        chat_history = AIHighlightChat.objects.filter(contract_project_id=contract_project_id).order_by('created_at')
        serializer = AIHighlightChatSerializer(chat_history, many=True)
        
        return JsonResponse({'chat_history': serializer.data}, status=200)
    
    except ContractProject.DoesNotExist:
        return JsonResponse({'error': 'Contract project not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
