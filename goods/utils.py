from django.db.models import Q
from goods.models import Products


def q_search(query):
    query = query.strip().lower()
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    return Products.objects.filter(description__search=query)

    # keywords = [word for word in query.split() if len(word) > 2]
    
    # if not keywords: #If there are no keywords, return empty queryset
    #     return Products.objects.none()


    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(name__icontains=token) | Q(description__icontains=token) # Correct syntax + add name
    
    # return Products.objects.filter(q_objects)