"""
Sample data for testing the pharmaceutical information system
Run this with: python manage.py shell < populate_data.py
Or: python manage.py shell
>>> exec(open('populate_data.py').read())
"""

from medicines.models import Ingredient, Company, Efficacy, Medicine
from board.models import Post
from django.contrib.auth.models import User
from datetime import date

print("Starting data population...")

# Create ingredients
ingredients_data = [
    {'name': '아세트아미노펜', 'description': '해열 진통제 성분'},
    {'name': '이부프로펜', 'description': '비스테로이드성 소염진통제'},
    {'name': '덱스트로메토르판', 'description': '진해제 성분'},
    {'name': '클로르페니라민', 'description': '항히스타민제 성분'},
    {'name': '비타민C', 'description': '항산화 비타민'},
    {'name': '아스피린', 'description': '해열진통소염제'},
    {'name': '로라타딘', 'description': '항히스타민제'},
]

ingredients = []
for data in ingredients_data:
    ingredient, created = Ingredient.objects.get_or_create(
        name=data['name'],
        defaults={'description': data['description']}
    )
    ingredients.append(ingredient)
    if created:
        print(f"Created ingredient: {ingredient.name}")

# Create companies
companies_data = [
    {'name': '동아제약', 'address': '서울시 동대문구', 'phone': '02-920-8114'},
    {'name': '일동제약', 'address': '서울시 강서구', 'phone': '02-526-3114'},
    {'name': '유한양행', 'address': '서울시 동작구', 'phone': '02-828-0181'},
    {'name': '종근당', 'address': '서울시 중구', 'phone': '02-2194-0114'},
    {'name': 'CJ헬스케어', 'address': '서울시 중구', 'phone': '02-6740-2800'},
]

companies = []
for data in companies_data:
    company, created = Company.objects.get_or_create(
        name=data['name'],
        defaults={
            'address': data['address'],
            'phone': data['phone']
        }
    )
    companies.append(company)
    if created:
        print(f"Created company: {company.name}")

# Create efficacies
efficacies_data = [
    {'name': '해열진통', 'description': '열을 내리고 통증을 완화'},
    {'name': '감기증상완화', 'description': '감기로 인한 제반 증상 완화'},
    {'name': '소염진통', 'description': '염증 완화 및 통증 감소'},
    {'name': '알레르기증상완화', 'description': '알레르기 반응으로 인한 증상 완화'},
    {'name': '기침완화', 'description': '기침 증상 완화'},
    {'name': '영양보급', 'description': '영양소 보충'},
]

efficacies = []
for data in efficacies_data:
    efficacy, created = Efficacy.objects.get_or_create(
        name=data['name'],
        defaults={'description': data['description']}
    )
    efficacies.append(efficacy)
    if created:
        print(f"Created efficacy: {efficacy.name}")

# Create medicines
medicines_data = [
    {
        'name': '타이레놀',
        'company': companies[0],
        'ingredients': [ingredients[0]],
        'efficacies': [efficacies[0]],
        'dosage': '성인 1회 1~2정, 1일 3~4회 복용',
        'precautions': '간질환자는 복용 전 의사와 상담하세요',
        'side_effects': '드물게 두드러기, 호흡곤란 등이 나타날 수 있습니다',
        'storage': '실온(1~30℃)에서 보관',
    },
    {
        'name': '판피린',
        'company': companies[1],
        'ingredients': [ingredients[0], ingredients[2], ingredients[3]],
        'efficacies': [efficacies[1], efficacies[4]],
        'dosage': '성인 1회 1포, 1일 3회 식후 복용',
        'precautions': '임산부는 복용 전 의사와 상담하세요',
        'side_effects': '졸음, 구갈 등이 나타날 수 있습니다',
        'storage': '실온에서 보관',
    },
    {
        'name': '게보린',
        'company': companies[2],
        'ingredients': [ingredients[1]],
        'efficacies': [efficacies[0], efficacies[2]],
        'dosage': '성인 1회 1정, 1일 3회 복용',
        'precautions': '위장장애가 있을 수 있으므로 식후 복용을 권장합니다',
        'side_effects': '위장장애, 속쓰림 등이 나타날 수 있습니다',
        'storage': '실온에서 보관',
    },
    {
        'name': '지르텍',
        'company': companies[3],
        'ingredients': [ingredients[6]],
        'efficacies': [efficacies[3]],
        'dosage': '성인 1회 1정, 1일 1회 복용',
        'precautions': '운전이나 기계조작 시 주의하세요',
        'side_effects': '졸음, 두통 등이 나타날 수 있습니다',
        'storage': '실온에서 보관',
    },
    {
        'name': '비타500',
        'company': companies[4],
        'ingredients': [ingredients[4]],
        'efficacies': [efficacies[5]],
        'dosage': '성인 1회 1정, 1일 1회 복용',
        'precautions': '과량 복용 시 설사가 있을 수 있습니다',
        'side_effects': '일반적으로 부작용이 거의 없습니다',
        'storage': '실온에서 보관',
    },
    {
        'name': '아스피린',
        'company': companies[0],
        'ingredients': [ingredients[5]],
        'efficacies': [efficacies[0], efficacies[2]],
        'dosage': '성인 1회 1정, 1일 3회 복용',
        'precautions': '위장장애가 있을 수 있으므로 식후 복용하세요',
        'side_effects': '위장장애, 출혈 경향 등이 나타날 수 있습니다',
        'storage': '실온에서 보관',
    },
]

for data in medicines_data:
    medicine, created = Medicine.objects.get_or_create(
        name=data['name'],
        defaults={
            'company': data['company'],
            'dosage': data['dosage'],
            'precautions': data['precautions'],
            'side_effects': data['side_effects'],
            'storage': data['storage'],
        }
    )
    if created:
        medicine.ingredients.set(data['ingredients'])
        medicine.efficacies.set(data['efficacies'])
        print(f"Created medicine: {medicine.name}")

# Create a test user for board posts
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={
        'email': 'test@example.com',
        'is_staff': False,
        'is_superuser': False
    }
)
if created:
    user.set_password('testpass123')
    user.save()
    print(f"Created user: {user.username}")

# Create sample board posts
if Post.objects.count() == 0:
    posts_data = [
        {
            'title': '의약품 복용 시 주의사항',
            'content': '의약품을 복용할 때는 반드시 용법과 용량을 지켜야 합니다. 특히 어린이나 노인의 경우 더욱 주의가 필요합니다.',
        },
        {
            'title': '감기약 선택 가이드',
            'content': '감기약을 선택할 때는 자신의 증상에 맞는 약을 선택하는 것이 중요합니다. 해열이 필요한지, 기침 증상이 있는지 등을 고려해야 합니다.',
        },
        {
            'title': '진통제 올바른 복용법',
            'content': '진통제는 통증이 있을 때 복용하되, 장기간 복용은 피해야 합니다. 통증이 지속되면 의사와 상담하세요.',
        },
    ]
    
    for data in posts_data:
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            author=user
        )
        print(f"Created post: {post.title}")

print("\nData population completed!")
print(f"Total ingredients: {Ingredient.objects.count()}")
print(f"Total companies: {Company.objects.count()}")
print(f"Total efficacies: {Efficacy.objects.count()}")
print(f"Total medicines: {Medicine.objects.count()}")
print(f"Total posts: {Post.objects.count()}")
print(f"Total users: {User.objects.count()}")
