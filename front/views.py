from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER
from .models import ClientEmail, Article, Request
from validate_email import validate_email
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    """Home view"""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def post(self, request):
        quoteCompany = request.POST.get("fq_company")
        quoteLoad = request.POST.get("fq_load")
        quotePickUp = request.POST.get("fq_pickup")
        quoteDelivery = request.POST.get("fq_delivery")
        quoteEquipement = request.POST.get("fq_equipement")
        quoteEmail = request.POST.get("fq_email")
        quotePhone = request.POST.get("fq_phone")
        nl = "\n"
        send_mail(
            'Free Quote',
            f"Company : {quoteCompany} {nl} Load: {quoteLoad} {nl} PickUp : {quotePickUp} {nl} Delivery : {quoteDelivery} {nl} Equipement : {quoteEquipement} {nl} Email : {quoteEmail} {nl} Phone : {quotePhone}",
            EMAIL_HOST_USER,
            ['operations@clencylogistics.ca'],
            fail_silently=False,
        )
        send_mail(
            'Free Quote Confirmation',
            f"Dear {quoteCompany}, {nl}{nl}I hope this email finds you well. I am writing to confirm that we have received your email and we are grateful for your interest in our services. {nl}{nl}I want to assure you that we will work with you as soon as possible to address your needs and answer any questions you may have. Our team is dedicated to providing timely and professional service, and we are committed to ensuring that you have a positive experience with us. {nl}{nl}Please feel free to reach out to us if you have any further inquiries or concerns. We appreciate your patience and understanding as we work to respond to your email as quickly as possible. {nl}{nl}Thank you for choosing our services, and we look forward to serving you soon. {nl}{nl}Best regards, {nl}{nl}Clency Logistics",
            EMAIL_HOST_USER,
            [quoteEmail],
            fail_silently=False,
        )
        return redirect(reverse("home"))


class AboutView(TemplateView):
    """About view"""

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactView(TemplateView):
    """Contact view"""

    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = {}
        fName = request.POST.get("fname", "")
        lName = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        Request.objects.create(firstName=fName, lastName=lName, email=email, subject=subject, message=message)
        messages.add_message(request, messages.SUCCESS, 'Thank you for contacting us, we will get back to you soon!')
        return redirect("/contact/")


# def getArticle(request, **kwargs):
#     if request.method == "GET":
#         context = {}
#         try:
#             article = Article.objects.get(id=kwargs["pk"])
#             context["article"] = article
#         except:
#             return redirect("/articles/")
#         return render(request, "article.html", context)

# class ArticleView(TemplateView):
#     """Article view"""
#     template_name = "articles.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         articles = Article.objects.order_by('-creationDate').all()
        
#         paginator = Paginator(articles, 6)
#         page_number = self.request.GET.get("page", None)
#         articles = paginator.get_page(page_number)
#         context["articles"] = articles
#         return context


def getEmailNewsLetter(request):
    if request.method == "POST":
        newsLetterEmail = request.POST.get("newsLetterEmail")
        #is_valid = validate_email(newsLetterEmail,check_mx=True)
        #if is_valid:
        try:
            ClientEmail.objects.create(email=newsLetterEmail)
        except:
            pass
        previousRequest = request.META.get("HTTP_REFERER")
        return redirect(previousRequest)

        
