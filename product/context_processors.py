from . models import Contact, Product

def context(request):
    numb_contacts = Contact.objects.filter(is_read=False).count()
    contact = Contact.objects.all().order_by('-created')[0:5]
    products = Product.objects.all()[0:2]
    
    if request.LANGUAGE_CODE == 'ar':
        dir = 'rtl'
    else:
        dir = 'ltr'

    context = {
        'contacts': contact,
        'numb_contact' : numb_contacts,
        'items' : products,
        'dir': dir,
        'LANGUAGE_CODE': request.LANGUAGE_CODE
    }
    return context