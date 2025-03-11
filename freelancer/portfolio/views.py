from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "portfolio/blog.html")

def case_studies(request):
    return render(request, "portfolio/case-studies.html")

service_vs_price = {
    "Website Devlopment": 50_000,
    "Web Scraping": 150_000,
    "Branding": 15_550_000,
    "Hacking": 2_000_000_000,
    "Data Analysis": 40_000,
    "App Development": 270_000,
}

def services(request):
    return render(request, "portfolio/services.html", {"services": service_vs_price})


def testimonials(request):
    customer_testimonials = {
        "Alice Johnson": "Amazing service! Quick and hassle-free.",
        "Mark Stevens": "Great quality, will definitely buy again!",
        "Sophia Lee": "Friendly staff and fast delivery. Loved it!",
        "James Carter": "Product exceeded my expectations!",
        "Emily Davis": "Affordable prices and excellent support.",
        "Daniel Wright": "Highly recommend! Smooth transaction."
    }
    context = {"testimonials": customer_testimonials}
    return render(request, "portfolio/testimonials.html", context)

def pricing(request):
    return render(request, "portfolio/pricing.html", {"service_vs_price": service_vs_price})