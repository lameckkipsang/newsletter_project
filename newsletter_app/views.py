from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscriberForm
# Create your views here.

def subscribe(request):
    success_message = None
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            
            # Send confirmation email
            subject = "Welcome to Our Newsletter!"
            message = (
                f"Hi,\n\n"
                f"Thank you for subscribing to our newsletter! We're thrilled to have you on board.\n\n"
                f"Best regards,\nThe Team"
            )
            recipient_list = [subscriber.email]
            
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                success_message = "Subscription successful! Please check your inbox for a confirmation email."
            except Exception as e:
                print(f"--- GMAIL SMTP ERROR: {e} ---") 
                success_message = f"Subscribed, but email failed: {e}"
            
            form = SubscriberForm()
    else:
        form = SubscriberForm()
        
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'subscribe.html', context)