from django.shortcuts import render

# Create your views here.
from .models import PortfolioItem , Category

# views.py
from django.shortcuts import render
from .models import Category, PortfolioItem
# views.py
from django.shortcuts import render
from .models import Category, PortfolioItem
# views.py
from django.shortcuts import render
from .models import Category, PortfolioItem


# def portfolio_view(request):
#     categories = Category.objects.all()
#     selected_category_name = request.GET.get('category')

#     if selected_category_name:
#         selected_category = categories.filter(name=selected_category_name).first()
#         items = PortfolioItem.objects.filter(categories=selected_category) if selected_category else PortfolioItem.objects.none()
#     else:
#         selected_category = None
#         items = PortfolioItem.objects.all()  # Get all items if no category is selected

#     # Check if the request is an AJAX request
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         return render(request, 'portfolio/portfolio_items.html', {'items': items})

#     return render(request, 'portfolio/home.html', {
#         'categories': categories.distinct(),  # Ensure unique categories
#         'selected_category': selected_category,
#         'items': items,
#     })


# # views.py
# def portfolio_view(request):
#     categories = Category.objects.all()  # Fetch all categories
#     items = PortfolioItem.objects.all()   # Fetch all portfolio items

#     # Check if the request is an AJAX request
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         return render(request, 'portfolio/portfolio_items.html', {'items': items})

#     return render(request, 'portfolio/home.html', {
#         'categories': categories,
#         'items': items,  # Pass all items to the template
#     })



    

# views.py
from django.shortcuts import render
from .models import Category, PortfolioItem

def portfolio_view(request):
    categories = Category.objects.all()  # Fetch all categories
    selected_category_name = request.GET.get('category')

    if selected_category_name:
        # Get the items for the selected category
        selected_category = categories.filter(name=selected_category_name).first()
        items = PortfolioItem.objects.filter(categories=selected_category) if selected_category else PortfolioItem.objects.none()
    else:
        # Show all items if no specific category is selected
        items = PortfolioItem.objects.all()

    # Check if the request is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'portfolio/portfolio_items.html', {'items': items})

    return render(request, 'portfolio/home.html', {
        'categories': categories,
        'items': items,  # Pass the items to the template
    })