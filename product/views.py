from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from . models import *
from .forms import *
from django.contrib import messages
from django.utils.translation import activate, gettext as _
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

now = timezone.now()


def home(request):
    algo_benefits = Benefit.objects.filter(language__code=request.LANGUAGE_CODE, category__name='Algo Indicateur').order_by('-created')[0:10]
    robot_benefits = Benefit.objects.filter(language__code=request.LANGUAGE_CODE, category__name='Robot Auto trading').order_by('-created')[0:10]


    products_indicateur = Product.objects.filter(language__code=request.LANGUAGE_CODE, category__name="Algo Indicateur").order_by('-created')
    products_robot = Product.objects.filter(language__code=request.LANGUAGE_CODE, category__name="Robot Auto trading").order_by('-created')

    post_indicateur = Post.objects.filter(language__code=request.LANGUAGE_CODE, category__name="Algo Indicateur").order_by('-created')
    post_robo = Post.objects.filter(language__code=request.LANGUAGE_CODE, category__name="Robot Auto trading").order_by('-created')

    context = {
        'algo_benefits': algo_benefits,
        'robot_benefits':  robot_benefits,
        
        'products_indicateur': products_indicateur,
        'products_robot': products_robot,

        'post_indicateur': post_indicateur,
        'post_robo': post_robo,
       
    }
    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    products = Product.objects.all().order_by('-created')
    users = User.objects.all()
    

    today_oders = Order.objects.filter(created__date=now.date())
    month_orders = Order.objects.filter(created__year=now.year, created__month=now.month)


    orders = Order.objects.filter(canceled=False, confirmed=False).order_by('-created')


    context = {
        'products': products,
        'users': users,
        "today_oders": today_oders,
        "month_orders": month_orders,
        'orders': orders
    }
    return render(request, 'dash/index.html', context)



# Product Admin
def products(request):
    list = Product.objects.all().order_by('-created')
    paginator = Paginator(list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products
    }
    return render(request, 'dash/product-list.html', context)

def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        order = form.save(commit=False)
        if request.user.is_authenticated:
            order.user = request.user
        order.save()
        order.products.add(product)
        order.save()
        return redirect('/thanks')
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


# Create Product
@login_required
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, _("Produit créé avec succès!"))
            return redirect('/product/create')
    context = {
        'form': form
    }
    return render(request, 'dash/product-create.html', context)




@login_required
def deleteProduct(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        product.delete()
        messages.success(request, _('Le produit a été supprimé avec succès.'))
    else :
        return redirect('/')
    return redirect('/product/list')

@login_required
def updateProduct(request, id):
    product = get_object_or_404(Product, id=id)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid:
            form.save()
            messages.success(request, _("Produit mis à jour avec succès"))
            return redirect('/product/list')
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'dash/product-create.html', context)

@login_required
def AdToCart(request):
    id = request.GET.get('product')
    product = get_object_or_404(Product, id=id)
    if request.user in product.cart.all():
        product.cart.remove(request.user)
        cart = False
    else:
        product.cart.add(request.user)
        cart = True
    product.save()
    return JsonResponse({"cart": request.user.user_cart.all().count(), 'exist': cart})

@login_required
def cart(request):
    products = Product.objects.filter(cart__in=[request.user])
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            if products.count() > 0:
                order.save()
                for item in products:
                    order.products.add(item)
                    item.cart.remove(request.user)
                form.save_m2m()
                return redirect('/thanks')
            else :
                messages.success(request, _("Vous n'avez pas de produit dans le panier"))
                return redirect('/cart')

    context = {
        'products': products,
        'form': form
    }
    return render(request, 'cart.html', context)



def thanks(request):
    return render(request, 'thanks.html')



def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        if request.user.is_authenticated:
            contact.user = request.user
        contact.save()
        messages.success(request, _("Le message a été envoyé avec succès"))
        return redirect('/contact')

    context = {
        'form': form,
        "title": _("Contactez-nous")
    } 
    return render(request, 'contact.html', context)

@login_required
def contactList(request):
    list = Contact.objects.all().order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    context = {
        'msgs': contacts
    }
    return render(request, 'dash/contact-list.html', context)


@login_required
def message(request, id):
    message = get_object_or_404(Contact, id=id)
    message.is_read = True
    message.save()
    context = {
        'message': message
    }
    return render(request, 'dash/message.html', context)




def ourProducts(request):
    list = Product.objects.filter(language__code=request.LANGUAGE_CODE).order_by('-created')
    paginator = Paginator(list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

@login_required
def listBenefit(request):
    list = Benefit.objects.all().order_by('-created')
    paginator = Paginator(list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    benefits = paginator.get_page(page_number)
    return render(request, 'dash/benefit-list.html', {'benefits': benefits})


@login_required
def createBenefit(request):
    if request.method == 'POST':
        form = BenefitForm(request.POST)
        if form.is_valid():
            benefit = form.save(commit=False)
            benefit.user = request.user
            benefit.save()
            messages.success(request, "Avantage a été créé avec succès." )
            return redirect('/benefit/create')
    else:
        form = BenefitForm()
    return render(request, 'dash/benefit-from.html', {'form': form})


@login_required
def benefitUpdate(request, pk):
    benefit = get_object_or_404(Benefit, pk=pk)
    if request.method == 'POST':
        form = BenefitForm(request.POST, instance=benefit)
        if form.is_valid():
            benefit = form.save()
            messages.success(request, "Avantage a été edit avec succès." )
            return redirect('/benefit/list')
    else:
        form = BenefitForm(instance=benefit)
    return render(request, 'dash/benefit-from.html', {'form': form})


@login_required
def benefitDelete(request, pk):
    benefit = get_object_or_404(Benefit, pk=pk)
    if request.user.is_superuser:
        benefit.delete()
        messages.success(request, "L'avantage a été supprimé avec succès." )
        return redirect('/benefit/list')
    else :
        return redirect('/')

# Articl





@login_required
def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, _("Article créé avec succès."))
            return redirect('/post/list')
    else:
        form = PostForm()
    
    context = {'form': form, 'title': 'Create Article'}
    return render(request, 'dash/post/create.html', context)


@login_required
def PostList(request):
    list = Post.objects.all().order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts}
    return render(request, 'dash/post/list.html', context)

@login_required
def PostUpdate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, _("Article a été edit avec succès."))
            return redirect('/post/list')
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'title': 'Update Article', "post": post}
    return render(request, 'dash/post/create.html', context)

@login_required
def PostDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        post.delete()
        messages.success(request, _("Article a été supprimé avec succès."))
        return redirect('/post/list')
    else:
        return redirect('/')
    

def PostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    products = Product.objects.filter(language__code=request.LANGUAGE_CODE).order_by('-created')[0:4]
    context = {'title': post.title, "post": post, 'products': products}
    return render(request, 'post.html', context)


@login_required
def OrderList(request):
    list = Order.objects.all().order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    context = {'orders': orders, 'total': list.count()}
    return render(request, 'dash/order/list.html', context)


@login_required
def OrderNew(request):
    list = Order.objects.filter(confirmed=False, canceled=False).order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    context = {'orders': orders}
    return render(request, 'dash/order/new.html', context)

@login_required
def OrderConfirmed(request):
    list = Order.objects.filter(confirmed=True).order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    context = {'orders': orders}
    return render(request, 'dash/order/confirmed.html', context)

@login_required
def OrderCanceled(request):
    list = Order.objects.filter(canceled=True).order_by('-created')
    paginator = Paginator(list, 30) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    context = {'orders': orders}
    return render(request, 'dash/order/canceled.html', context)


@login_required
def ConfirmOrder(request):
    if request.user.is_superuser:
        id = request.GET.get('confirm')
        order = Order.objects.get(id=id)
        if order.confirmed:
            order.confirmed = False
        else:
            order.confirmed = True
        order.save()
        messages.success(request, 'The order was Confirmed successfully.')
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer)
    
@login_required
def CancelOrder(request):
    if request.user.is_superuser:
        id = request.GET.get('cancel')
        order = Order.objects.get(id=id)
        if order.canceled:
            order.canceled = False
        else:
            order.canceled = True
        order.save()
        messages.success(request, 'The order was canceled successfully.')
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer)
    
@login_required
def order(request, pk):
    if request.user.is_superuser:
        order = Order.objects.get(id=pk)
        context = {
            'order': order
        }

        return render(request, 'dash/order/order.html', context)
    else:
        return redirect('/')
    


def costumers(request):
    list = User.objects.all().order_by('date_joined')
    paginator = Paginator(list, 30) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    context = {
        'users': users
    }
    return render(request, 'users.html', context)

        












    