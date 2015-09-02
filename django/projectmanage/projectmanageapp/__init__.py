from projectmanageapp.models import project
post=project(name='test')
post.file.put(open(r'C:\\Users\min.sun\Desktop\阿布.jpg','rb'))
post.save()
