from rest_framework import serializers

"""
serializers 可用字段

BooleanField	BooleanField()
NullBooleanField	NullBooleanField()
CharField	CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
EmailField	EmailField(max_length=None, min_length=None, allow_blank=False)

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
