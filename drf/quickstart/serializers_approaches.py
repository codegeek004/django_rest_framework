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


	
