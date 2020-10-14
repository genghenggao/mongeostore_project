"""
序列化
"""
# from .models import Mysegy
# from rest_framework.validators import UniqueValidator
# from rest_framework import serializers
# import re
# from datetime import datetime, timedelta

# from django.contrib.auth import get_user_model
# UserInfo = get_user_model()

# from .models import VerifyCode

# class SmsSerializer(serializers.Serializer):
#     """
#     短信验证码序列化
#     """
#     mobile = serializers.CharField(max_length=11, min_length=11)

#     # 重载内置的方法，自定义验证 model 中的字段
#     # 函数名【强制要求】为 validate_(字段名)
#     def validate_mobile(self, mobile):
#         """
#         验证手机号码
#         :param mobile:
#         :return:
#         """
#         # 验证手机号码是否合法
#         REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"  # 手机号码正则表达式
#         if not re.match(REGEX_MOBILE, mobile):
#             raise serializers.ValidationError("手机号码不合法")  # 返回数据出错

#         # 验证手机是否注册
#         if User.objects.filter(mobile=mobile).count() > 0:
#             raise serializers.ValidationError("用户已经存在")  # 返回数据出错

#         # 验证发送频率
#         one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1,
#                                                      seconds=0)  # 获取一分钟以前的时间
#         if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count() > 0:
#             raise serializers.ValidationError("验证码发送频繁，请稍后再试")  # 返回数据出错

#         # 所有验证通过，返回数据
#         return mobile

# class RegisterSerializer(serializers.ModelSerializer):
#     """
#     用户注册序列化
#     """
#     # error_messages 表示数据出错时的提示字段
#     # write_only 设置了之后 save() 序列化时，就不会调用这个数据，且前端不会返回
#     # code = serializers.CharField(max_length=4, min_length=4, required=True, help_text="短信验证码", error_messages={
#     #     "blank": "验证码不能为空",
#     #     "required": "请输入验证码",
#     #     "max_length": "验证码太长了，最多4位",
#     #     "min_length": "验证码太短了，最少4位",
#     # }, label="验证码", write_only=True)

#     # 验证用户名唯一性
#     username = serializers.CharField(label="用户名",
#                                      required=True,
#                                      allow_blank=False,
#                                      validators=[UniqueValidator(queryset=UserInfo.objects.all(), message="用户已存在")])

#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         label="登录密码",
#         write_only=True
#     )

#     def create(self, validated_data):
#         """
#         重载创建方法
#         创建时将密码转为密文
#         （如果使用了signal，就不需要重载这个）
#         :param validated_data:
#         :return:
#         """
#         userInfo = super(RegisterSerializer, self).create(
#             validated_data=validated_data)
#         userInfo.set_password(validated_data["password"])  # django 自带的密码密文
#         userInfo.save()
#         return userInfo

#     def validated_code(self, code):
#         # 用户前端传过来的值，都会放在 self.initial_data 中
#         verify_record = VerifyCode.objects.filter(
#             mobile=self.initial_data["username"]).order_by("-add_time")
#         if verify_record:
#             last_record = verify_record[0]
#             five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5,
#                                                           seconds=0)  # 获取验证码有效期为5分钟

#             if five_minutes_ago > last_record.add_time:
#                 raise serializers.ValidationError("验证码已过期")  # 抛出序列化异常
#             if last_record.code != code:
#                 raise serializers.ValidationError("验证码错误")  # 抛出序列化异常
#         else:
#             raise serializers.ValidationError("验证码记录不存在")  # 抛出序列化异常

#     def validate(self, attrs):
#         """
#         validate 函数表示所有参数传递过来的验证
#         :param attrs: 前端传递过来的所有参数
#         :return: 将参数处理过后，传递给接下来的逻辑
#         """
#         attrs["mobile"] = attrs["username"]
#         del attrs["code"]  # 从 dict 中删除一项
#         return attrs

#     class Meta:
#         model = UserInfo
#         fields = ("username", "code", "mobile", "email", "password",)

# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ("username", "mobile", "email",)

# 学生测试序列化
# from .models import StudentsModel
# class StudentsSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()
#     port = serializers.IntegerField()

#     def create(self, validated_data):
#      return StudentsModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.content = validated_data.get('content', instance.content)
#         instance.email = validated_data.get('email', instance.email)
#         instance.created = validated_data.get('created', instance.created)
#         instance.port = validated_data.get('port', instance.port)
#         instance.save()

from rest_framework import serializers
from .models import UserInfo
# from .models import SmsCode
## mongeostore序列化 ##


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo  # 对应的Model中的类
        # fields = ("username", "mobile", "email",)
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
        # exclude = ('password',)   # 注意：结尾的 '，' 逗号，去掉会序列化失败。exclude 属性设置为从序列化程序中排除的字段列表。 实例化时将看不到  password 字段，及password 不被序列化，
        # fields = ('username','password','email')  # 序列化指定字段。
        # exclude = ['password']  # 使用list  形式也是可以的，此时可以不要逗号。同理fields 也支持 list 形式，因为官网 就是 list形式。

        #  本身ModelSerializer  它包含 .create() 和 .update() 的简单默认实现。 所以这里写不写,下面两个方法都行，但是在嵌套序列化 的情况下要重写下面两个方法。
        # def create(self, validated_data):
        #     print("~~~~~~~~~~~~~~")
        #     print(validated_data)
        #     return UserInfo.objects.create(**validated_data)
        #
        #
        # def update(self, instance, validated_data):
        #
        #     instance.name = validated_data.get('name',instance.name)
        #
        #
        #     instance.save()
        #     return instance

#短信序列化
# class SmscodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SmsCode  # 对应的Model中的类
#         # fields = ("username", "mobile", "email",)
#         fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
# from .models import UploadFile
# class UploadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UploadFile  # 对应的Model中的类
#         # fields = ("username", "mobile", "email",)
#         fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段