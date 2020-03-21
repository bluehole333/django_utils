from rest_framework import serializers

"""
serializers 可用字段

BooleanField	        BooleanField()
NullBooleanField	    NullBooleanField()
CharField	            CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
EmailField	            EmailField(max_length=None, min_length=None, allow_blank=False)
RegexField          	RegexField(regex, max_length=None, min_length=None, allow_blank=False)
SlugField	            SlugField(maxlength=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9-]+
URLField	            URLField(max_length=200, min_length=None, allow_blank=False)
UUIDField	            UUIDField(format='hex_verbose') 
                        format: 
                            1) 'hex_verbose' 如"5ce0e9a5-5ffa-654b-cee0-1238041fb31a" 
                            2） 'hex' 如 "5ce0e9a55ffa654bcee01238041fb31a" 
                            3）'int' - 如: "123456789012312313134124512351145145114" 
                            4）'urn' 如: "urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"
IPAddressField	        IPAddressField(protocol='both', unpack_ipv4=False, **options)
IntegerField	        IntegerField(max_value=None, min_value=None)
FloatField	            FloatField(max_value=None, min_value=None)
DecimalField	        DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)
                        max_digits: 最多位数
                        decimal_palces: 小数点位置
DateTimeField	        DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None)
DateField	            DateField(format=api_settings.DATE_FORMAT, input_formats=None)
TimeField	            TimeField(format=api_settings.TIME_FORMAT, input_formats=None)
DurationField	        DurationField()
ChoiceField	            ChoiceField(choices) choices与Django的用法相同

"""


class XXXXXXXSerializer(serializers.ModelSerializer):
    """
    ModelSerializer
    """
    # 返回值
    xxxxx = serializers.SerializerMethodField(label="xx")

    class Meta:
        model = ModelName
        fields = ('显示字段',)
        # fields和exclude 只能存在其一
        exclude = ('不显示字段',)
        read_only_fields = ('只读字段，不可被写入',)

    def get_xxxxx(self, obj):
        return obj.xxxxx


class XXXXXSerializer(serializers.Serializer):
    """
    一般可用于自定义验证
    """
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if value == 'xxxx':
            raise serializers.ValidationError(_('返回错误信息，http状态为400'))

        return value

    def validate(self, attrs):
        """
        全部字段自定义验证
        """
        # 需要创建Serializer时传入request XXXXXSerializer(data=request.data, context={'request': request})
        request = self.context.get('request')

        if attrs['email'] == 'xxxx':
            raise serializers.ValidationError({'email': _('返回错误信息，http状态为400')})

        return value
