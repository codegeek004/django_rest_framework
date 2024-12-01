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

class QuickstartSerailizer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model=Quickstart
		fields = ['url','id','highlight','owner',
				  'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail')

	class Meta:
		model = User 
		fields = ['url','id','username','snippets']





#This was working with primary key
#Modelserializer is simply shortcut for creating serializer class.
# class QuickstartSerializer(serializers.ModelSerializer):
# 	#snippets are associated with the users who created them.
# 	owner = serializers.ReadOnlyField(source='owner.username')
# 	class Meta:
# 		model = Quickstart
# 		fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']

# class UserSerializer(serializers.ModelSerializer):
# 	snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Quickstart.objects.all())
# 	class Meta:
# 		model = User 
# 		fields = ['id', 'username', 'snippets']


# class QuickstartSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template' : 'text_area.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	# def create(self, validated_data):
	# 	#Create and return a new `Snippet` instance, given the validated data.
	# 	return Quickstart.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	#Update and return an existing `Snippet` instance, given the validated data.
	# 	#instance: current model instance to be updated
	# 	#validated_data.get(): Fetches the new value for a field from validated_data, 
	# 	#or uses the current field value (instance.field) if no new value is provided.
	# 	instance.title = validated_data.get('title', instance.title)
	# 	instance.code = validated_data.get('code', instance.code)
	# 	instance.linenos = validated_data.get('linenos', instance.linenos)
	# 	instance.language = validated_data.get('language', instance.language)
	# 	instance.style = validated_data.get('style', instance.style)
	# 	instance.save()
	# 	return instance


	
