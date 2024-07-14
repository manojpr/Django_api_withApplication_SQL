from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import PiesDevSerializer
from .models import PiesDev
import pandas as pd
from django.db import connection

# Create your views here.
@api_view(['GET'])
def filter_pies_api(request):
    part_number = request.GET.get('part_number')
    business_unit = request.GET.get('business_unit')
    category = request.GET.get('category')
    product_line = request.GET.get('product_line')
    part_type = request.GET.get('part_type')

    brandownername = request.GET.get('brandownername')
    brandname = request.GET.get('brandname')
    subbrandname = request.GET.get('subbrandname')

    sql_query = "SELECT * FROM pies_dev WHERE 1=1 "
    params = []

    if brandownername:
        sql_query += " AND  [brand_owner_name] = %s"
        params.append( brandownername )

    if brandname:
        sql_query += " AND  [brand_name] = %s"
        params.append( brandname )

    if subbrandname:
        sql_query += " AND  [sub_brand_name] = %s"
        params.append( subbrandname )

    if part_number:
        part_number = str(part_number)

        if '*' in part_number:
            part_number=part_number.replace('*', '%')
        
        sql_query += " AND  part_number like %s"
        params.append(part_number)
    
    if business_unit:
       sql_query += " AND  [BusinessUnit] = %s"
       params.append( business_unit )

    if category:
        sql_query += " AND  [Category] = %s"
        params.append( category )
    
    if product_line:
        sql_query += " AND  [ProductLine] = %s"
        params.append( product_line)

    if part_type:
        sql_query += " AND  [part_type_name] = %s"
        params.append( part_type )

    with connection.cursor() as cursor:
        cursor.execute(sql_query, params)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    results = [dict(zip(columns, row)) for row in rows]

    # pies = PiesDev.objects.filter(**filters)
    serializer = PiesDevSerializer(results, many=True)

    return Response(serializer.data)

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def filter_pies_api(request):
#     part_number = request.GET.get('part_number')
#     page = request.GET.get('page', 1) # Default page number is 10
#     page_size = int(request.GET.get('page_size', 10))  # Default page size is 10
    
#     # Construct the SQL query
#     sql_query = "SELECT * FROM pies_dev"
#     params = []

#     # Add filters if provided
#     if part_number:
#         sql_query += " WHERE part_number = %s"
#         params.append(part_number)

#     # Execute the SQL query
#     with connection.cursor() as cursor:
#         cursor.execute(sql_query, params)
#         columns = [col[0] for col in cursor.description]
#         rows = cursor.fetchall()

#     # Convert rows to dictionaries
#     results = [dict(zip(columns, row)) for row in rows]

#     # Implement pagination
#     paginator = Paginator(results, page_size)
#     try:
#         paginated_results = paginator.page(page)
#     except PageNotAnInteger:
#         paginated_results = paginator.page(1)
#     except EmptyPage:
#         paginated_results = paginator.page(paginator.num_pages)

#     # Use the serializer to convert the paginated results to JSON
#     serializer = PiesDevSerializer(paginated_results, many=True)

#     return Response({
#         'count': paginator.count,
#         'num_pages': paginator.num_pages,
#         'current_page': page,
#         'page_size': page_size,
#         'results': serializer.data,
#         'next': paginated_results.has_next() and paginated_results.next_page_number() or None,
#         'previous': paginated_results.has_previous() and paginated_results.previous_page_number() or None,
#     })
