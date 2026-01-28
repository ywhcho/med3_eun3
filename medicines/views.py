from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Medicine, Ingredient, Company, Efficacy

# Create your views here.

def search_view(request):
    """의약품 검색 뷰"""
    search_type = request.GET.get('type', '')
    selected_id = request.GET.get('id', '')
    page_number = request.GET.get('page', 1)
    
    # 모든 성분, 회사, 효능 목록 가져오기
    ingredients = Ingredient.objects.all()
    companies = Company.objects.all()
    efficacies = Efficacy.objects.all()
    
    medicines = None
    page_obj = None
    
    # 검색 타입에 따라 필터링
    if search_type and selected_id:
        if search_type == 'ingredient':
            medicines_list = Medicine.objects.filter(ingredients__id=selected_id).distinct()
        elif search_type == 'company':
            medicines_list = Medicine.objects.filter(company__id=selected_id)
        elif search_type == 'efficacy':
            medicines_list = Medicine.objects.filter(efficacies__id=selected_id).distinct()
        else:
            medicines_list = Medicine.objects.none()
        
        # 페이지네이션 (10개씩)
        paginator = Paginator(medicines_list, 10)
        page_obj = paginator.get_page(page_number)
        medicines = page_obj.object_list
    
    context = {
        'ingredients': ingredients,
        'companies': companies,
        'efficacies': efficacies,
        'medicines': medicines,
        'page_obj': page_obj,
        'search_type': search_type,
        'selected_id': selected_id,
    }
    
    return render(request, 'medicines/search.html', context)


def detail_view(request, pk):
    """의약품 상세 정보 뷰"""
    medicine = get_object_or_404(Medicine, pk=pk)
    
    context = {
        'medicine': medicine,
    }
    
    return render(request, 'medicines/detail.html', context)

