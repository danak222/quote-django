from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Quote
import random
import json
from django.shortcuts import render, get_object_or_404

# ============ TEMPLATE VIEWS (return HTML) ============

# TODO 7: Create a home view
#   - Get all quotes from database: Quote.objects.all()
#   - Pick a random quote
#   - Render 'quotes/home.html' with quote in context
def home(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return render(request, 'quotes/home.html', {'quote': None})

    quote = random.choice(quotes)

    return render(request, 'quotes/home.html', {'quote': quote})

# TODO 8: Create an all_quotes view
#   - Get all quotes
#   - Render 'quotes/all_quotes.html' with quotes in context
def all_quotes(request):
    quotes = Quote.objects.all()

    return render(request, 'quotes/all_quotes.html', {'quotes': quotes})


# ============ API VIEWS (return JSON) ============

# TODO 9: Create a random_quote_api view
#   - Get all quotes, pick random one
#   - Return JsonResponse with 'id', 'text', 'author'
def random_quote_api(request):
    quotes = list(Quote.objects.all())

    if not quotes:
        return JsonResponse({'error': 'No quotes found'}, status=404)

    quote = random.choice(quotes)

    return JsonResponse({
        'id': quote.id,
        'text': quote.text,
        'author': quote.author
    })

@csrf_exempt
def quotes_api(request):
    # TODO 10: Handle GET and POST for /api/quotes/
    #   GET: Return all quotes as JSON (use safe=False for lists)
    #   POST: Create new quote from request.body, return with status 201
    #   Check request.method to determine which action

    if request.method == 'GET':
        quotes = list(Quote.objects.values())
        return JsonResponse(quotes, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)

        quote = Quote.objects.create(
            text=data['text'],
            author=data['author']
        )

        return JsonResponse({
            'id': quote.id,
            'text': quote.text,
            'author': quote.author
        }, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def quote_detail_api(request, id):
    # TODO 11: Handle GET, PUT, DELETE for /api/quotes/<id>/
    #   GET: Return single quote as JSON (404 if not found)
    #   PUT: Update quote from request.body, return updated quote
    #   DELETE: Delete quote, return success message
    #   Check request.method to determine which action

    quote = get_object_or_404(Quote, id=id)

    if request.method == 'GET':
        return JsonResponse({
            'id': quote.id,
            'text': quote.text,
            'author': quote.author
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)

        quote.text = data.get('text', quote.text)
        quote.author = data.get('author', quote.author)
        quote.save()

        return JsonResponse({
            'id': quote.id,
            'text': quote.text,
            'author': quote.author
        })

    elif request.method == 'DELETE':
        quote.delete()

        return JsonResponse({'message': 'Quote deleted successfully'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)
    pass