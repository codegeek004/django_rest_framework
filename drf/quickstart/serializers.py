from rest_framework import serializers
from quickstart.models import Quickstart, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User 
############Hyperlinked Serializer##############
# The HyperlinkedModelSerializer has the following differences from ModelSerializer:
# It does not include the id field by default.
# It includes a url field, using HyperlinkedIdentityField.
# Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.


##hyperlinks are URL references used to represent relationships between resources in an API. 
#They provide a more RESTful approach by linking related entities through their URLs rather
# than embedding data directly or using primary keys.

class QuickstartSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
#view_name is in the format basename_list and basename_detial
	class Meta:
		model=Quickstart
		fields = ['url','id','highlight','owner',
				  'title', 'code', 'linenos', 'language', 'style']
		extra_kwargs = {
            'url': {'view_name': 'snippet-detail'}  # Ensure this matches your view name
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User 
		fields = ('url','id','username','snippets')
		extra_kwargs = {
            'url': {'view_name': 'user-detail'}  # Ensure this matches your view name
        }




