from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import *

import logging

logger = logging.getLogger(__name__)

# ListView, DetailView를 사용하기 하기 위해서 html 파일 이름을 정해줘야함
# ListView: 모델의 리스트를 보여주는 뷰로 _list.html 이름을 고수하여야 함
# DetailView: 모델의 상세 정보를 보여주는 뷰로 _detail.html 이름을 고수하여야 함


class BookModelView(TemplateView):
    template_name = "book.html"
    logger.debug("BookModelView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
