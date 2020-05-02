from django.shortcuts import render, redirect
from .models import Member, Document, Ajax, CsvUpload, Item, CompOrder, MainData, DrinkData, DessertData, SideData
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from timeit import default_timer as timer

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def admin(request):
    return render(request, 'admin.html')

@login_required
def getData(request):
    id = request.POST.get('id', '')
    data = Item.objects.filter(comp_id=id)
    xml = ''
    for p in data:
        xml += '<tr id="'+ str(p.id) +'"><td>'+ p.name+ '</td><td>'+ str(p.carb) +'</td><td>'+ str(p.fat) +'</td><td>'+ str(p.suaaer) +'</td><td>'+ str(p.protein) +'</td><td>'+ str(p.price) +'</td><td><a class="btn btn-sm btn-warning" href="editItem/'+ str(p.id) +'"><span class="fa fa-edit"></span> Edit</a> <a class="btn btn-sm btn-danger" href="delItem/'+ str(p.id) +'"><span class="fa fa-trash"></span> Delete</a></td></tr>'
    return JsonResponse({'data': xml})

@login_required
def addItem(request, id):
    context = {'comp_id': id}
    return render(request, 'addItem.html', context)

@login_required
def editItem(request, id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'editItem.html', context)

@login_required
def updateItem(request, id):
    item = Item.objects.get(id=id)
    item.name = request.POST['name']
    item.carb = request.POST['carb']
    item.fat = request.POST['fat']
    item.suaaer = request.POST['suaaer']
    item.protein = request.POST['protein']
    item.price = request.POST['price']
    item.save()
    messages.success(request, 'Item was updated successfully!')
    return redirect('/admin')

@login_required
def delItem(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    messages.error(request, 'Item was deleted successfully!')
    return redirect('/admin')

@login_required  
def saveItem(request):
    if request.method == 'POST':
        item = Item(
            comp_id = request.POST['comp_id'],
            name = request.POST['name'],
            carb = request.POST['carb'],
            fat = request.POST['fat'],
            suaaer = request.POST['suaaer'],
            protein = request.POST['protein'],
            price = request.POST['price']
        )
        item.save()
        messages.success(request, 'Item was created successfully!')
        return redirect('admin')
    else:
        return render(request, 'addItem.html')

@login_required
def mainSave(request):
    parent_id = request.POST.get('parent_id')
    item_data = request.POST.get('item_data')

    MainData.objects.filter(parent_id=parent_id).delete()
    item_data = item_data.split(',')
    for p in item_data:
        row = MainData(
            parent_id = parent_id,
            item_id = p,
        )
        row.save()
    return JsonResponse({'data': 'success'})

@login_required
def drinkSave(request):
    parent_id = request.POST.get('parent_id')
    item_data = request.POST.get('item_data')
    DrinkData.objects.filter(parent_id=parent_id).delete()
    item_data = item_data.split(',')
    for p in item_data:
        row = DrinkData(
            parent_id = parent_id,
            item_id = p,
        )
        row.save()
    return JsonResponse({'data': 'success'})

@login_required
def dessertSave(request):
    parent_id = request.POST.get('parent_id')
    item_data = request.POST.get('item_data')

    DessertData.objects.filter(parent_id=parent_id).delete()
    item_data = item_data.split(',')
    for p in item_data:
        row = DessertData(
            parent_id = parent_id,
            item_id = p,
        )
        row.save()
    return JsonResponse({'data': 'success'})

@login_required
def sideSave(request):
    parent_id = request.POST.get('parent_id')
    item_data = request.POST.get('item_data')

    SideData.objects.filter(parent_id=parent_id).delete()
    item_data = item_data.split(',')
    for p in item_data:
        row = SideData(
            parent_id = parent_id,
            item_id = p,
        )
        row.save()
    return JsonResponse({'data': 'success'})

@login_required
def calc(request):
    start = timer()
    carb = request.POST.get('carb')
    fat = request.POST.get('fat')
    sugar = request.POST.get('sugar')
    price = request.POST.get('price')

    order = CompOrder.objects.all().order_by('id')
    first = ''
    second = ''
    third = ''
    fourth = ''

    result = '';
    firstResult = '';

    count = 1
    for o in order:
        if o.item_id == 1:
            if count == 1:
                first = MainData.objects.all().order_by('id')
            elif count == 2:
                second = MainData.objects.all().order_by('id')
            elif count == 3:
                third = MainData.objects.all().order_by('id')
            else:
                fourth = MainData.objects.all().order_by('id')
        elif o.item_id == 2:
            if count == 1:
                first = DrinkData.objects.all().order_by('id')
            elif count == 2:
                second = DrinkData.objects.all().order_by('id')
            elif count == 3:
                third = DrinkData.objects.all().order_by('id')
            else:
                fourth = DrinkData.objects.all().order_by('id')
        elif o.item_id == 3:
            if count == 1:
                first = DessertData.objects.all().order_by('id')
            elif count == 2:
                second = DessertData.objects.all().order_by('id')
            elif count == 3:
                third = DessertData.objects.all().order_by('id')
            else:
                fourth = DessertData.objects.all().order_by('id')
        else:
            if count == 1:
                first = SideData.objects.all().order_by('id')
            elif count == 2:
                second = SideData.objects.all().order_by('id')
            elif count == 3:
                third = SideData.objects.all().order_by('id')
            else:
                fourth = SideData.objects.all().order_by('id')
        count += 1
    count = 1
    for f in first:
        first_data = Item.objects.get(id=f.item_id)
        firstCarb = first_data.carb
        firstFat = first_data.fat
        firstSugar = first_data.suaaer
        firstPrice = first_data.price
        for s in second:
            if s.parent_id != f.item_id and s.parent_id > 0:
                continue
            second_data = Item.objects.get(id=s.item_id)
            secondCarb = second_data.carb
            secondFat = second_data.fat
            secondSugar = second_data.suaaer
            secondPrice = second_data.price
            for t in third:
                if t.parent_id != s.item_id and t.parent_id != f.item_id and t.parent_id > 0:
                    continue
                third_data = Item.objects.get(id=t.item_id)
                thirdCarb = third_data.carb
                thirdFat = third_data.fat
                thirdSugar = third_data.suaaer
                thirdPrice = third_data.price
                for fo in fourth:
                    if fo.parent_id != t.item_id and fo.parent_id != s.item_id and fo.parent_id != f.item_id and fo.parent_id > 0:
                        continue
                    four_data = Item.objects.get(id=fo.item_id)
                    fourCarb = four_data.carb
                    fourFat = four_data.fat
                    fourSugar = four_data.suaaer
                    fourPrice = four_data.price
                    totalCarb = firstCarb + secondCarb + thirdCarb + fourCarb
                    totalFat = firstFat + secondFat + thirdFat + fourFat
                    totalSugar = firstSugar + secondSugar + thirdSugar + fourSugar
                    totalPrice = firstPrice + secondPrice + thirdPrice + fourPrice
                    if Decimal(carb) < Decimal(totalCarb) or Decimal(fat) < Decimal(totalFat) or Decimal(sugar) < Decimal(totalSugar) or Decimal(price) < Decimal(totalPrice):
                        continue;
                    else:
                        if count == 7:
                            return JsonResponse({'data': result, 'firstResult': firstResult})
                        end = timer()
                        time = end - start
                        if count == 1:
                            firstResult = str(first_data.name) + ',' + str(second_data.name) + ',' + str(third_data.name) + ',' + str(four_data.name) + ' : ' + str(time * 1000) + 'ms'
                        else:
                            if result == '':
                                result = str(first_data.name) + ',' + str(second_data.name) + ',' + str(third_data.name) + ',' + str(four_data.name) + ' : ' + str(time * 1000) + 'ms'
                            else:
                                result = result + '<br>' + str(first_data.name) + ',' + str(second_data.name) + ',' + str(third_data.name) + ',' + str(four_data.name) + ' : ' + str(time * 1000) + 'ms'
                        count += 1
    start = ''
    if result == '':
        return JsonResponse({'data': '', 'firstResult': 'No meal according to your preferences and constraints , please relax your constraints'})
    else:
        return JsonResponse({'data': result, 'firstResult': firstResult})

@login_required  
def saveData(request):
    order_array = request.POST.get('order_array')
    order_array = order_array.split(',')
    CompOrder.objects.all().delete()

    MainData.objects.all().delete()
    DrinkData.objects.all().delete()
    DessertData.objects.all().delete()
    SideData.objects.all().delete()

    row1 = CompOrder(
        item_id = '1',
        prefer_type = request.POST.get('prefer1'),
        condition = request.POST.get('condition1'),
        parent_id = request.POST.get('parent1'),
    )
    row2 = CompOrder(
        item_id = '2',
        prefer_type = request.POST.get('prefer2'),
        condition = request.POST.get('condition2'),
        parent_id = request.POST.get('parent2'),
    )
    row3 = CompOrder(
        item_id = '3',
        prefer_type = request.POST.get('prefer3'),
        condition = request.POST.get('condition3'),
        parent_id = request.POST.get('parent3'),
    )
    row4 = CompOrder(
        item_id = '4',
        prefer_type = request.POST.get('prefer4'),
        condition = request.POST.get('condition4'),
        parent_id = request.POST.get('parent4'),
    )
    for p in order_array:
        if p == '1':
            row1.save()
        elif p == '2':
            row2.save()
        elif p == '3':
            row3.save()
        elif p == '4':
            row4.save()
    return JsonResponse({'data': 'success'})


@login_required
def first(request):
    return render(request, 'first.html')

@login_required
def second(request):
    datas = CompOrder.objects.all().order_by('id')

    main_items = Item.objects.filter(comp_id=1)
    drink_items = Item.objects.filter(comp_id=2)
    dessert_items = Item.objects.filter(comp_id=3)
    side_items = Item.objects.filter(comp_id=4)

    return render(request, 'second.html',{'datas': datas,'main_items': main_items,'drink_items':drink_items,'dessert_items':dessert_items,'side_items':side_items})
# 

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            is_staff=True,
            is_active=True,
            is_superuser=True,
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'success.html',
    )

@login_required
def changePassword(request):
    print('changepasword')
    return render(request, 'change_password.html')

