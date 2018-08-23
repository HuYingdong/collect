
# python3 manage.py shell

from api.models import Bookmark
from api.serializers import BookmarkSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


bookmark = Bookmark(issue='在配置文件中为Logger配置多个handler',
                    url='https://blog.csdn.net/yypsober/article/details/51782281')
bookmark.save()

bookmark = Bookmark(issue='扩展阅读_零基础入门学习Python',
                    sort='python',
                    url='https://fishc.com.cn/forum.php?mod=forumdisplay&fid=243&filter=typeid&typeid=403')
bookmark.save()

serializer = BookmarkSerializer(bookmark)
serializer.data

content = JSONRenderer().render(serializer.data)
content

# Deserialization
from django.utils.six import BytesIO
stream = BytesIO(content)
data = JSONParser().parse(stream)
data

data = {'id': 2, 'issue': '扩展阅读_零基础入门学习Python',
        'url': 'https://fishc.com.cn/forum.php?mod=forumdisplay&fid=243&filter=typeid',
        'sort': 'python'}

serializer = BookmarkSerializer(data=data)
serializer.is_valid()  # True
serializer.validated_data
# serializer.save()

# many
serializer = BookmarkSerializer(Bookmark.objects.all(), many=True)
serializer.data

