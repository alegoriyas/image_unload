from django.db import models
#from filefieldtools import upload_to

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    #Загрузка файлов в каталог по текущей дате
    # uploads/books/2012/04/27/<filename>
    #picture = models.ImageField(upload_to=upload_to('books/%Y/%m/%d'))

    #Приводит имя файла к нижнему регистру
    # Upload filename: 'My Picture.JPG'
    # Path: 'uploads/books/pictures/My-Picture.JPG'
    #picture1 = models.ImageField(upload_to=upload_to('books/pictures', to_lower=False))

    #Генерация обезличенного имени файла
    # uploads/books/pictures/fb999b0773ba7cd946a708aea.<extension>
    #picture = models.ImageField(upload_to=upload_to('books/pictures', to_hash=True))

    #Контроль длины пути к файлу
    # default max_length for ImageField is 100.
    #
    # Upload filename: '1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40.xls'
    # Upload filename length: 110
    #
    # Path: 'books/pictures/1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30.xls'
    #picture = models.ImageField(upload_to=upload_to('books/pictures', field_name='picture'))

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
        
        
    #books = Book.objects.all()

    #for book in books:
        #book.delete()