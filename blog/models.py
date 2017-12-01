# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Article(models.Model):
    """文章"""
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    abstract = models.CharField('摘要', max_length=50, blank=True, null=True, help_text='可选')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)


class Author(models.Model):
    """作者"""
    name = models.CharField('名称', max_length=20)


class Comment(models.Model):
    """评论"""
    user_name = models.CharField('评论者名字', max_length=100)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)


class Tag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)


class Category(models.Model):
    """分类"""
    name = models.CharField(u'分类名', max_length=20)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField(u'修改时间', auto_now=True)
