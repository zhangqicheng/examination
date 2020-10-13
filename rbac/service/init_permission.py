from django.conf import settings

def init_permission(current_user,request):

    # 1.权限信息初始化
    # 根据当前用户获取权限信息，并放入session
    permission_query = current_user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                                   'permissions__title',
                                                                                   'permissions__is_menu',
                                                                                   'permissions__icon',
                                                                                   'permissions__url',).distinct()
    #2.获取权限+菜单信息
    menu_list=[]
    permission_list=[]
    for item in permission_query:
        permission_list.append(item['permissions__url'])
        if item['permissions__is_menu']:
            temp={
                'title':item['permissions__title'],
                'icon':item['permissions__icon'],
                'url':item['permissions__url']
            }
            menu_list.append(temp)

    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list