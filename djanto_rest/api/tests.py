# from django.test import TestCase
#
# # Create your tests here.
# import unittest
# import requests
#
#
#
# class UserTest(unittest.TestCase):
#     '''用户查询测试'''
#
#     def setUp(self):
#         self.base_url = 'http://127.0.0.1:8000/users'
#         self.auth = ('Greenbirch2007','mingyifan2007')
#
#     def test_user1(self):
#         '''　test user admin '''
#         r = requests.get(self.base_url+'/1/',auth=self.auth)
#         result = r.json()
#         self.assertEqual(result['username'],'Greenbirch2007')
#         self.assertEqual(result['email'],'291109028@qq.com')
#
#     def test_user2(self):
#         '''test user tom '''
#         r =requests.get(self.base_url+'/2/',auth=self.auth)
#         result = r.json()
#         self.assertEqual(result['usename'],'tom')
#         self.assertEqual(result['email','tom@mail.com'])
#
#     def test_user3(self):
#         '''　test user jack '''
#         r = requests.get(self.base_url+'/3/',auth=self.auth)
#         result = r.json()
#         self.assertEqual(result['username'],'jack')
#         self.assertEqual(result['email','jack@mail.com'])
#
#
#
# class GroupsTest(unittest.TestCase):
#     ''' 用户组查询测试'''
#
#     def setUp(self):
#         self.base_url = 'http://127.0.0.1:8000/groups'
#         self.auth = ('Greenbirch2007','mingyifan2007')
#
#
#     def test_gorup1(self):
#         '''test groups test'''
#         r = requests.get(self.base_url+'/1/',auth=self.auth)
#         result = r.json()
#         self.assertEqual(result['name'],'test')
#
#     def test_group2(self):
#         ''' test groups developer'''
#         r = requests.get(self.base_url+'/2/',auth=self.auth)
#         result = r.json()
#         self.assertEqual(result['name'],'developer')
#
#
# if __name__ =='__main__':
#     unittest.main()


def application(env,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'Hello  World~']