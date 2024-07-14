from django.shortcuts import render
from django.http import JsonResponse
from .models import DIM_BU, DIMBrand
import requests 
import logging
logger = logging.getLogger(__name__)

def filter_new_dropdowns(request):
    # Fetch all distinct values for each column initially
    brand_owners = DIMBrand.objects.values_list('brandownername', flat=True).distinct()
    brands = DIMBrand.objects.values_list('brandname', flat=True).distinct()
    sub_brands = DIMBrand.objects.values_list('subbrandname', flat=True).distinct()

    context = {
        'brand_owners': brand_owners,
        'brands': brands,
        'sub_brands': sub_brands,
    }

    return render(request, 'application/filter_new_dropdowns.html', context)

def filter_dropdowns(request):
    # Fetch all distinct values for each column initially
    business_units = DIM_BU.objects.values_list('BusinessUnit', flat=True).distinct()
    categories = DIM_BU.objects.values_list('Category', flat=True).distinct()
    product_lines = DIM_BU.objects.values_list('ProductLine', flat=True).distinct()
    part_types = DIM_BU.objects.values_list('part_type_name', flat=True).distinct()

    context = {
        'business_units': business_units,
        'categories': categories,
        'product_lines': product_lines,
        'part_types': part_types,
    }

    # return render(request, 'application/filter_dropdowns.html', context)
    return render(request, 'application/filter_dropdowns_with_api_call.html', context)

# def filter_new_dropdowns(request):
#     brandownername = request.GET.get('brandownername', '')
#     brandname = request.GET.get('brandname', '')
#     subbrandname = request.GET.get('subbrandname', '')
    
#     # Logic to fetch options for brandownername, brandname, and subbrandname
#     brand_owners = DIMBrand.objects.values_list('brandownername', flat=True).distinct()
#     brands = DIMBrand.objects.filter(brandownername=brandownername).values_list('brandname', flat=True).distinct() if brandownername else []
#     sub_brands = DIMBrand.objects.filter(brandname=brandname).values_list('subbrandname', flat=True).distinct() if brandname else []

#     return JsonResponse({
#         'brand_owners': list(brand_owners),
#         'brands': list(brands),
#         'sub_brands': list(sub_brands),
#         'selected_brandownername': brandownername,
#         'selected_brandname': brandname,
#         'selected_subbrandname': subbrandname
#     })
def filter_new_dropdowns(request):
    brandownername = request.GET.get('brandownername', '')
    brandname = request.GET.get('brandname', '')
    subbrandname = request.GET.get('subbrandname', '')
    
    # Start with all records
    filtered_results = DIMBrand.objects.all()

    # Apply filters incrementally based on selected values
    if brandownername:
        filtered_results = filtered_results.filter(brandownername=brandownername)
    if brandname:
        filtered_results = filtered_results.filter(brandname=brandname)
    if subbrandname:
        filtered_results = filtered_results.filter(subbrandname=subbrandname)

    # Fetch distinct values for each dropdown based on the filtered results
    brand_owners = filtered_results.values_list('brandownername', flat=True).distinct()
    brands = filtered_results.values_list('brandname', flat=True).distinct()
    sub_brands = filtered_results.values_list('subbrandname', flat=True).distinct()

    data = {
        'brand_owners': list(brand_owners),
        'brands': list(brands),
        'sub_brands': list(sub_brands),
        'selected_brandownername': brandownername,
        'selected_brandname': brandname,
        'selected_subbrandname': subbrandname,
    }
    
    return JsonResponse(data)

def filter_dropdowns_ajax(request):
    business_unit = request.GET.get('business_unit')
    category = request.GET.get('category')
    product_line = request.GET.get('product_line')
    part_type = request.GET.get('part_type')

    filtered_results = DIM_BU.objects.all()

    if business_unit:
        filtered_results = filtered_results.filter(BusinessUnit=business_unit)
    if category:
        filtered_results = filtered_results.filter(Category=category)
    if product_line:
        filtered_results = filtered_results.filter(ProductLine=product_line)
    if part_type:
        filtered_results = filtered_results.filter(part_type_name=part_type)

    # Fetch distinct values for filtered results
    business_units = filtered_results.values_list('BusinessUnit', flat=True).distinct()
    categories = filtered_results.values_list('Category', flat=True).distinct()
    product_lines = filtered_results.values_list('ProductLine', flat=True).distinct()
    part_types = filtered_results.values_list('part_type_name', flat=True).distinct()

    data = {
        'business_units': list(business_units),
        'categories': list(categories),
        'product_lines': list(product_lines),
        'part_types': list(part_types),
        'selected_business_unit': business_unit,
        'selected_category': category,
        'selected_product_line': product_line,
        'selected_part_type': part_type,
    }
    return JsonResponse(data)

def filter_pies_api_view(request):
    # Get query parameters from the GET request
    part_number = request.GET.get('part_number')
    business_units = request.GET.getlist('business_units')
    categories = request.GET.getlist('categories')
    product_lines = request.GET.getlist('product_lines')
    part_types = request.GET.getlist('part_types')

    # Make request to external API (example)
    api_url = 'http://127.0.0.1:8001/api/filter_pies_api/'
    api_params = {
        'part_number': part_number,
        'business_units': business_units,
        'categories': categories,
        'product_lines': product_lines,
        'part_types': part_types,
    }

    response = requests.get(api_url, params=api_params)

    if response.status_code == 200:
        data = response.json()  # Assuming API returns JSON data
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=500)

from .forms import FilterForm

def filter_pies_view(request):
    form = FilterForm(request.GET)
    if form.is_valid():
        part_number = form.cleaned_data.get('part_number')
        business_units = form.cleaned_data.get('business_unit')
        categories = form.cleaned_data.get('category')
        product_lines = form.cleaned_data.get('product_line')
        part_types = form.cleaned_data.get('part_type')

        brandownername = form.cleaned_data.get('brandownername')
        brandname = form.cleaned_data.get('brandname')
        subbrandname = form.cleaned_data.get('subbrandname')
        print(part_number)
        # Make API call
        api_url = 'http://127.0.0.1:8001/api/filter_pies_api/'
        api_params = {
            'part_number': part_number,
            'business_unit': business_units,
            'category': categories,
            'product_line': product_lines,
            'part_type': part_types,

            'brandownername':brandownername,
            'brandname' : brandname,
            'subbrandname' : subbrandname,
        }
        logger.info(f"API Parameters: {api_params}")  
        response = requests.get(api_url, params=api_params)
        if response.ok:
            api_data = response.json()
            return JsonResponse(api_data, safe=False)
        else:
            return JsonResponse({'error': 'API Error'}, status=500)
    
    return JsonResponse({'error': 'Form is not valid'}, status=400)