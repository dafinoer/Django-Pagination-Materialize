# Django-pagination-materialize

implementation django pagination from [djangosnippets](https://djangosnippets.org/snippets/1441/),integration using materialize pagination [materialize](http://materializecss.com/pagination.html)


##### How to Use
1. go to you apps/views.py
2. create some view for retrive all data (i'm use class-based generic views TemplateView)
3. create directory in your, example apps/templates
4. add new file using name pagination.py
5. and use ```{% load pagination %} {% pagination yourpage %}``` in your templates
