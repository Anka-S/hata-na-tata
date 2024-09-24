from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# Create your views here.

class ReviewPage(TemplateView):
    """
    Displays review page
    """
    template_name = 'reviews/reviews.html'

def review_view(request):
    reviews = Review.objects.all().order_by("-created_on")
    reviews_count = reviews.filter(approved=True).count()
    review_form = ReviewForm()
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            
        messages.add_message(
         request, messages.SUCCESS,
        'Review is submitted and awaiting approval')
        return redirect('reviews')

    context = {
        "reviews": reviews,
        "reviews_count": reviews_count,
        "review_form": review_form,
    }

    return render(request, "reviews/reviews.html", context)