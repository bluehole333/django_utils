from rest_framework import serializers

"""
serializers可用属性

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
MultipleChoiceField	    MultipleChoiceField(choices)
FileField	            FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)
ImageField	            ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL)
ListField	            ListField(child=, min_length=None, max_length=None)
DictField	            DictField(child=)
"""

"""
serializers 可用参数:
    max_length	最大长度
    min_lenght	最小长度
    allow_blank	是否允许为空
    trim_whitespace	是否截断空白字符
    max_value	最小值
    min_value	最大值
    
通用参数:
    read_only	表明该字段仅用于序列化输出，默认False
    write_only	表明该字段仅用于反序列化输入，默认False
    required	表明该字段在反序列化时必须输入，默认True
    default	    反序列化时使用的默认值
    allow_null	表明该字段是否允许传入None，默认False
    validators	该字段使用的验证器
    error_messages	包含错误编号与错误信息的字典
    label	    用于HTML展示API页面时，显示的字段名称
    help_text	用于HTML展示API页面时，显示的字段帮助提示信息
    
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
