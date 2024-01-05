from app.models import LoaiPhong,Phong, User
from app import app, db
import hashlib



def load_categories():
    return LoaiPhong.query.all()


def load_products(kw=None, cate_id=None):

   products = Phong.query

   if kw:
       products = products.filter(Phong.name.contains(kw))



   if cate_id:
        products = products.filter(Phong.category_id.__eq__(cate_id))


   return products.all()


def get_user_by_id(id):
    return User.query.get(id)



def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                            User.password.__eq__(password)).first()