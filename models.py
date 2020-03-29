from django.db import models


class Member(models.Model):
    NORMAL = 0
    FORBIDDEN = 1
    STATUS = {
        NORMAL: "正常",
        FORBIDDEN: "禁用",
    }

    name = models.CharField("昵称", max_length=64, null=True, blank=True)
    email = models.CharField('邮箱', null=True, blank=True, max_length=64)
    password = models.CharField('密码', max_length=64, null=True, blank=True)
    # 外键设置: 1.使用"app.Model" 2. "Model" 3. Model
    # on_delete:
    #   CASCADE: 删除关联数据,与之关联也删除
    #   DO_NOTHING: 删除关联数据,什么也不做
    #   PROTECT: 删除关联数据,引发错误ProtectedError
    #   SET_NULL: 删除关联数据,与之关联的值设置为null
    #   SET_DEFAULT: 删除关联数据,与之关联的值设置为默认值(需要设置default)
    #   CASCADE: 删除关联数据,与之关联也删除
    #   SET(): 自定义一个值，该值当然只能是对应的实体了 on_delete=models.SET(obj)
    invite_user = models.ForeignKey('Member', on_delete=models.CASCADE, help_text='邀请人不能为自己', verbose_name='邀请人',
                                    null=True, blank=True)
    is_validate_email = models.BooleanField('是否邮箱验证', default=False)
    status = models.SmallIntegerField("用户状态", default=NORMAL, choices=STATUS.items())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '用户'
        verbose_name = verbose_name_plural
        # 关联唯一约束
        unique_together = ('name', 'email')

        # 指定数据库表名
        db_table = 'member_member'

        #  设置索引
        indexes = [
            models.Index(fields=['invite_user']),
            models.Index(fields=['name']),
            models.Index(fields=['email']),
            models.Index(fields=['name', 'email']),
        ]
