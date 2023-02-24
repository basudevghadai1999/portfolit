from django.db import models

class Person1(models.Model):
    image = models.BinaryField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'
images = '/home/dev/Downloads/sequence.jpeg'
eimage = images.encode('utf-8')

person = Person1.objects.create(
    image = images,
    first_name='John',
    last_name='Doe',
    email='johndoe@example.com'
)


print("this is called")

#persons = Person1.objects.all()


# for person in persons:
#     print(person)