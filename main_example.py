from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590")

class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    password = fields.CharField()
    #defined the fields (can look up documentation for pymodm fields)

#can create users
u = User('user1@email.com', last_name='Ross', first_name='Bob')
u2 = User('user2@email.com', last_name='Ross', first_name='Rob')

#save method will automatically save the users in the specified location from (connect)
u.save() # basically inherited from the MongoModel class
u2.save()

for user in User.objects.raw({"first_name":"Rob"}):
    # for each user that satisifies this query -> find in db and print it!
    print(user)
    print(user.first_name)
    print(user.last_name)
