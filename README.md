# myblog
Queryset 

 Post.objects.filter(author=me)
 from django.utils import timezone

  Post.objects.filter(published_date__lte=timezone.now())
  
  post = Post.objects.get(title ='Sample title')
post.publish
Post.objects.filter(published_date__lte=timezone.now())

Post.objects.filter(title__contains='title')

 Post.objects.order_by('created_date')
 
 Post.objects.order_by('-created_date')
 
 Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
