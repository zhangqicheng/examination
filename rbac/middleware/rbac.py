from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.conf import settings
import re

class RbacMiddleware(MiddlewareMixin):
    def process_request(self,request):
        """
        执行用户请求权限验证
        :param request:
        :return:
        """
        """
        1.获取当前用户的url
        2.获取当前用户在session中保存的权限列表
        3.权限信息匹配
        """
        current_url=request.path_info
        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url,current_url):
                '''白名单中的url无需权限验证'''
                return None

        permission_list=request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return HttpResponse('未获取到用户权限信息，请登录!')

        flag=False

        for url in permission_list:
            req='^%s$' % url
            if re.match(req,current_url):
                flag=True
                break

        if not flag:
            return HttpResponse('无权访问')

