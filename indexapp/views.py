from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,HttpResponse,redirect
from loginregist.models import DCategory,TBook,TUser

# Create your views here.
def index(request):
    login = request.session.get('login')
    # print(login)
    cate = DCategory.objects.filter(category_pid=0)# print(cate)
    cate_child = DCategory.objects.filter(~Q(category_pid=0))# print(cate_child)
    #新书上架
    newbook = TBook.objects.all().order_by('-publish_time')
    # print(newbook)
    #主编推荐
    editorbook = TBook.objects.all().order_by('editor_recommendation')
    #销量排行榜
    salebook = TBook.objects.all().order_by('-sales')
    if login:
        return render(request,'index.html',{'cate':cate,'cate_child':cate_child,'newbook':newbook,'editorbook':editorbook,'salebook':salebook,'login':login})
    return render(request, 'index.html',
                  {'cate': cate, 'cate_child': cate_child, 'newbook': newbook, 'editorbook': editorbook,
                   'salebook': salebook})


def booklist(request):
    #分类
    cate = DCategory.objects.filter(category_pid=0)  # print(cate)
    cate_child = DCategory.objects.filter(~Q(category_pid=0))  # print(cate_child)
    id = request.GET.get('id')# print(id)
    state = request.GET.get('state')
    # print(state)

    l = []
    listcate = DCategory.objects.filter(category_id=id)
    if listcate:
        l.append(listcate[0])
        if not(listcate[0].category_pid=='0'):
            pbook = DCategory.objects.get(category_id=listcate[0].category_pid)
            l.insert(0,pbook)

    catechild = DCategory.objects.filter(Q(category_id=id)|Q(category_pid=id)).values('category_id')
    # # print(list(catechild))
    cate_id=list(map(lambda x:x['category_id'],list(catechild)))
    books=TBook.objects.filter(book_category__in=cate_id)
    books1 = TBook.objects.filter().all()
    # print("hhhh",books)
    #分类
    categoryBook = []
    # pid = DCategory.objects.filter(category_id=id)[0].category_pid
    # categoryBook.append(DCategory.objects.filter(category_id=pid)[0])
    categoryBook.append(DCategory.objects.filter(category_id=id)[0])
    #排序
    if state == '1':
        books=TBook.objects.filter(book_category__in=cate_id)
    elif state == '2':
        books=TBook.objects.filter(book_category__in=cate_id).order_by('-sales')
    elif state == '3':
        books=TBook.objects.filter(book_category__in=cate_id).order_by('book_dprice')
    elif state == '4':
        books=TBook.objects.filter(book_category__in=cate_id).order_by('-publish_time')
    else:
        books = TBook.objects.filter(book_category__in=cate_id)



    num = request.GET.get('num',1)
    pages = Paginator(books,per_page=3)
    if int(num) not in pages.page_range:
        num = 1
    page = pages.page(int(num))
    return  render(request,'booklist.html',{'cate':cate,'cate_child':cate_child,'books':books,'pages':pages,'page':page,'id':id,'categoryBook':categoryBook,'state':state,'l':l})


    # catechild = DCategory.objects.filter(category_id=id)[0]
    # categoryBook = []
    # if catechild.category_pid != '0':
    #     pid =DCategory.objects.filter(category_id=id)[0].category_pid
    #     books = TBook.objects.filter(book_category=catechild.category_id)
    #     categoryBook.append(DCategory.objects.filter(category_id=pid)[0])
    #     categoryBook.append(DCategory.objects.filter(category_id=id)[0])
    #     # print(c_book)
    #
    #     if state == '1':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id))
    #         books.extend(list(b_book))
    #     elif state == '2':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('-sales')
    #         print(books)
    #         books.extend(list(b_book))
    #     elif state == '3':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('book_dprice')
    #         books.extend(list(b_book))
    #     elif state == '4':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('-publish_time')
    #         books.extend(list(b_book))
    #     else:
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id))
    #         books.extend(list(b_book))
    #
    #     num = request.GET.get('num', 1)
    #     pages = Paginator(books, per_page=3)
    #     page = pages.page(int(num))
    #     data = {'cate':cate,'cate_child':cate_child,'books':books,'pages':pages,'page':page,'id':id,'categoryBook':categoryBook,'state':state}
    #     return render(request,'booklist.html',data)
    # else:
    #     books = []
    #     c_cate = DCategory.objects.filter(category_pid=catechild.category_id)
    #     # print(c_cate)
    #     categoryBook.append(DCategory.objects.filter(category_id=id)[0])
    #     # print(categoryBook)
    #
    #     if state == '1':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id))
    #         books.extend(list(b_book))
    #     elif state == '2':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('-sales')
    #         print(books)
    #         books.extend(list(b_book))
    #     elif state == '3':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('book_dprice')
    #         books.extend(list(b_book))
    #     elif state == '4':
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id)).order_by('-publish_time')
    #         books.extend(list(b_book))
    #     else:
    #         b_book = TBook.objects.filter(Q(category_id=id) | Q(category_pid=id))
    #         books.extend(list(b_book))
    #
    #     for i in c_cate:
    #         a_book = TBook.objects.filter(book_category=i.category_id)
    #         if a_book:
    #             books.extend(a_book)
    #     # print(books)
    #     num = request.GET.get('num', 1)
    #     pages = Paginator(books, per_page=3)
    #     page = pages.page(int(num))
    #     data = {'cate': cate, 'cate_child': cate_child, 'books': books,'pages':pages,'page':page,'id':id,'categoryBook':categoryBook}
    #     return render(request,'booklist.html',data)

def Bookdetails(request):
    #书籍详情页
    id = request.GET.get('id')#print(id)

    categoryBook = []
    # pid = DCategory.objects.filter(category_id=id)[0].category_pid
    # categoryBook.append(DCategory.objects.filter(category_id=pid)[0])
    categoryBook.append(DCategory.objects.filter(category_id=id)[0])

    bookdetail = TBook.objects.filter(book_id=id)
    if bookdetail:
        return render(request,'Book details.html',{'bookdetail':bookdetail,'categoryBook':categoryBook})
    return render(request,'Book details.html')



