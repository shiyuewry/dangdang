from loginregist.models import TBook
class Car_item():
    def __init__(self,book,number):
        self.book = book
        self.number = number


class Car():
    def __init__(self):
        self.car_items = []
        self.total_price = 0
        self.save_price = 0
    def sums(self):
        self.total_price = 0
        self.save_price = 0
        for i in self.car_items:
            self.total_price += float(i.book.book_dprice)*float(i.number)
            self.save_price += float(i.book.book_price)*float(i.number)-float(i.book.book_dprice)*float(i.number)


    #向购物车添加商品
    def add_car(self,bookid):
        for i in self.car_items:
            if str(i.book.book_id) == str(bookid):
                i.number +=1
                self.sums()
                return
        self.car_items.append(Car_item(TBook.objects.filter(book_id=int(bookid))[0],1))
        self.sums()

    # 删除购物车中某个商品
    def del_item(self,bookid):
        for i in self.car_items:
            if str(i.book.book_id) == str(bookid):
                self.car_items.remove(i)
                self.sums()

    #修改购物车某个商品信息
    def change_item(self,bookid,number):
        for i in self.car_items:
            if str(i.book.book_id) == str(bookid):
                i.number = number
                self.sums()

