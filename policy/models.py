from django.db import models
from datetime import datetime

# Create your models here.

class PolicyCard(models.Model):
    policy_level_choices = (
        (0, '省级'),
        (1, '县级'),
        (2, '县（市， 区）级')
    )

    policy_type_choices = (
        (0, '综合类'),
        (1, '资金奖补类'),
        (2, '税收费用减免类'),
        (3, '资质荣誉类')
    )



    policy_id = models.IntegerField('政策编号', primary_key=True, default=None)
    title = models.CharField('标题', max_length=50, null=True, blank=True)
    reward_content = models.TextField('奖补内容')
    policy_basis = models.TextField('政策依据', max_length=500)
    policy_conditions = models.TextField('政策申报条件', max_length=500)
    end_time = models.DateTimeField('截止时间', default=datetime.now)
    policy_level = models.IntegerField('政策层级', choices=policy_level_choices, default=0)
    policy_type = models.IntegerField('政策类型', choices=policy_type_choices, default=0)
    policy_area = models.CharField('政策区域', max_length=20)
    type = models.CharField('企业类型', max_length=100, blank=True, null=True)
    create_years = models.IntegerField('成立年限(年)', blank=True, null=True)
    emp_num = models.IntegerField('最低企业员工数量', blank=True, null=True)
    tech_emp_num = models.IntegerField('最低技术人员数量', blank=True, null=True)
    total_assets = models.FloatField('最低总资产(万)', blank=True, null=True)
    fixed_assets = models.FloatField('最低固定资产（万）', blank=True, null=True)
    sales_profit = models.FloatField('最低销售收入（万）', blank=True, null=True)
    sales_mainly_prop = models.FloatField('最低主导产品收入占比(百分比)', blank=True, null=True)
    sales_profit_inc = models.FloatField('最低销售收入增长率(百分比)', blank=True, null=True)
    profit = models.FloatField('最低利润（万）', blank=True, null=True)
    profit_inc = models.FloatField('最低利润增长率（百分百）', blank=True, null=True)
    research_cost_prop = models.FloatField('最低研发投入占比(百分比)', blank=True, null=True)
    patent_num = models.IntegerField('最低专利数量', blank=True, null=True)
    intellectual_property = models.IntegerField('其他知识产权数量', blank=True, null=True)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)

    class Meta:
        verbose_name = "政策卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




