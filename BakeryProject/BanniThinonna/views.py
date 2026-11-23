
from django.shortcuts import render, get_object_or_404
from .models import Sweet,Cake,Namkeen


def home(request):
    return render(request, 'home.html')


def sweets(request):
    all_sweets = Sweet.objects.filter(
        is_available=True
    ).order_by('name')

    return render(request, 'sweets.html', {
        'sweets': all_sweets
    })


def sweet_detail(request, sweet_id):
    sweet = get_object_or_404(
        Sweet,
        id=sweet_id,
        is_available=True
    )

    similar_sweets = Sweet.objects.filter(
        category=sweet.category,
        is_available=True
    ).exclude(id=sweet.id)[:4]

    return render(request, 'sweet_detail.html', {
        'sweet': sweet,
        'similar_sweets': similar_sweets
    })


def cart(request):
    return render(request, 'cart.html', {
        'cart_items': [],
        'total': 0
    })


def wishlist(request):
    return render(request, 'wishlist.html', {
        'wishlist_items': []
    })


def cakes(request):

    all_cakes = Cake.objects.filter(
        is_available=True
    ).order_by('name')

    return render(request, 'cakes.html', {
        'cakes': all_cakes
    })

def cake_detail(request, cake_id):

    cake = get_object_or_404(
        Cake,
        id=cake_id,
        is_available=True
    )

    similar_cakes = Cake.objects.filter(
        category=cake.category,
        is_available=True
    ).exclude(id=cake.id)[:4]

    return render(request, 'cake_detail.html', {
        'cake': cake,
        'similar_cakes': similar_cakes
    })


def cart(request):
    return render(request, 'cart.html', {
        'cart_items': [],
        'total': 0
    })

def namkeens(request):

    selected_category = request.GET.get('category', '')

    namkeen_list = Namkeen.objects.all()

    if selected_category:
        namkeen_list = namkeen_list.filter(
            category=selected_category
        )

    categories = Namkeen.CATEGORY_CHOICES

    return render(request, 'namkeen.html', {
        'namkeens': namkeen_list,
        'categories': categories,
        'selected_category': selected_category
    })


def namkeen_detail(request, id):

    namkeen = get_object_or_404(Namkeen, id=id)

    similar_namkeens = Namkeen.objects.filter(
        category=namkeen.category
    ).exclude(id=namkeen.id)[:4]

    return render(request, 'namkeen_detail.html', {
        'namkeen': namkeen,
        'similar_namkeens': similar_namkeens
    })