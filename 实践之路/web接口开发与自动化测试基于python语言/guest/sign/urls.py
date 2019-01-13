

from django.conf.urls import url

from sign import  views_api




urlpatters = [
    # sign system interface:
    # ex: /api/add_event/
    url(r"^add_event/",views_api.add_event,name='add_event'),

    # ex: /api/add_guest/
    url(r"^add_guest/",views_api.add_guest,name='add_guest'),

    # ex: /api/get_event_list/
    url(r"^get_event_list/",views_api.get_event_list,name='get_event_list'),

    # ex:  /api/get_guest_list/

    url(r"^get_guest_list/",views_api.get_guest_list,name='get_guest_list'),

    # ex: /api/user_sign/

    url(r"^user_sign/",views_api.user_sign,name='user_sign')
]
