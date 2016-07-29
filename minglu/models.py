#coding=utf8
from django.db import models

# Create your models here.

class ssdata(models.Model):
    '''
    title = models.CharField(max_length = 150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    '''
    
    zch = models.TextField()
    mcyename = models.TextField()
    fddbri = models.TextField()
    zyxmlb = models.TextField()
    dz = models.TextField()
    rjzczb = models.TextField()
    qylx = models.TextField()
    clrq = models.TextField()
    yyqx = models.TextField()
    hzrq = models.TextField()
    djjg = models.TextField()
    zt = models.TextField()
    jyfw = models.TextField()
    xydm = models.TextField() 
    #def __unicode__(self):
    #    return self.name
    
    class Meta:
        db_table = 'ssjibenxinxi'   #指定表名
        ordering = ['-hzrq']        #按核准日期排序

class gszxdata(models.Model):
    '''
    title = models.CharField(max_length = 150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    '''
    
    zch = models.TextField()
    qiyename = models.TextField()
    hzriqi = models.TextField()
    djjg = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'gsqiyezhuxiao'   #指定表名
        ordering = ['-hzriqi']        #按核准日期排序    
        
        
class gssldata(models.Model):
    '''
    title = models.CharField(max_length = 150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    '''
    
    zch = models.TextField()
    qiyename = models.TextField()
    hzriqi = models.TextField()
    djjg = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = 'gsqiyesheli'   #指定表名
        ordering = ['-hzriqi']        #按核准日期排序    
        
        
#############


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)