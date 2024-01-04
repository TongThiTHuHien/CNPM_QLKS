from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db
# from flask_login import UserMixin



# class User(db.Model, UserMixin):
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     username = Column(String(50), nullable=False, unique=True)
#     password = Column(String(100), nullable=False)
#     avatar = Column(String(100), default='https://cdn1.viettelstore.vn/images/Product/ProductImage/medium/iPad-Pro-12.9-gray1.jpg')


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products= relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    image = Column(String(100))



if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.create_all()


        # c1 = Category(name='Phòng 1 giường')
        # c2 = Category(name='Phòng 2 giường')
        #
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        #
        # p1 = Product(name='Phòng 1 giường đôi cao cấp', price=1300000,
        #             category_id=1,
        #              image="https://www.cet.edu.vn/wp-content/uploads/2018/01/cac-loai-giuong-trong-khach-san.jpg")
        # p2 = Product(name='Phòng 2 giường ', price=2000000,
        #              category_id=2,
        #              image="https://noithatmyhouse.net/wp-content/uploads/2019/10/giuong-ngu-khach-san_11.jpg")
        # p3 = Product(name='Phòng 1 giường đơn', price=850000,
        #              category_id=1,
        #              image="https://chefjob.vn/wp-content/uploads/2020/07/tieng-anh-loai-phong-khach-san.jpg")
        # p4 = Product(name='Phòng 2 giường cao cấp ', price=2500000,
        #              category_id=2,
        #              image="https://decoxdesign.com/upload/images/hotel-caitilin-1952m2-phong-ngu-06-decox-design.jpg")
        # p5 = Product(name='Phòng 1 giường đôi view biển', price=1500000,
        #              category_id=1,
        #              image="https://www.hoteljob.vn/files/Anh-HTJ-Hong/tieu-chi-can-co-trong-thiet-ke-phong-khach-san-1.jpg")
        # p6 = Product(name='Phòng 1 giường đôi đầy đủ nội thất', price=1200000,
        #              category_id=1,
        #              image="https://tubepfurniture.com/wp-content/uploads/2020/09/phong-mau-khach-san-go-cong-nghiep-01.jpg")
        # p7 = Product(name='Phòng 2 giường đơn', price=1300000,
        #              category_id=2,
        #              image="https://everon.com/upload_images/images/noi-that-phong-ngu-khach-san/phong-ngu-khach-san-2.jpg")
        # p8 = Product(name='Phòng 2 giường đôi và đơn', price=1800000,
        #              category_id=2,
        #              image="https://www.hoteljob.vn/files/VB2-%E1%BA%A3nh%20HTJ/cac-loai-phong-trong-khach-san-2.jpg")
        #
        # db.session.add_all([p6, p7, p8])
        # db.session.commit()
