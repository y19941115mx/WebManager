from django.db import models
from datetime import date

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
    title = models.CharField('标题', max_length=50)
    reward_content = models.TextField('奖补内容')
    policy_basis = models.TextField('政策依据', max_length=500)
    policy_conditions = models.TextField('政策申报条件', max_length=500)
    end_time = models.DateField('截止时间', default=date.today)
    policy_level = models.IntegerField('政策层级', choices=policy_level_choices, default=0)
    policy_type = models.IntegerField('政策类型', choices=policy_type_choices, default=0)
    policy_area = models.CharField('政策区域', max_length=20)
    type = models.CharField('企业类型', max_length=100, blank=True, null=True)
    create_years = models.IntegerField('成立年限(年)', blank=True, null=True)
    
    total_assets = models.FloatField('最低总资产(万)', blank=True, null=True)
    fixed_assets = models.FloatField('最低固定资产（万）', blank=True, null=True)
    sales_profit = models.FloatField('最低销售收入（万）', blank=True, null=True)
    sales_mainly_prop = models.FloatField('最低主导产品收入占比(百分比)', blank=True, null=True)
    sales_profit_inc = models.FloatField('最低销售收入增长率(百分比)', blank=True, null=True)
    profit = models.FloatField('最低利润（万）', blank=True, null=True)
    profit_inc = models.FloatField('最低利润增长率（百分百）', blank=True, null=True)
    research_cost_prop = models.FloatField('最低研发投入占比(百分比)', blank=True, null=True)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)

    class Meta:
        verbose_name = "政策卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class PolicyResource(models.Model):
    card = models.ForeignKey(PolicyCard, on_delete=models.CASCADE, verbose_name="所属政策卡")
    name = models.CharField(max_length=100, verbose_name=u"文件名称")
    download = models.FileField(upload_to="policy/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"政策卡文件资源"
        verbose_name_plural = verbose_name

class PatentLimit(models.Model):
    patent_type_choices = (
        (0, '一类专利'),
        (1, '二类专利'),
        (2, '三类专利'),
        (3, '其他')
    )

    type = models.IntegerField('专利类型', choices=patent_type_choices)
    number = models.IntegerField('专利数量')
    policy = models.ForeignKey(PolicyCard, on_delete=models.CASCADE, verbose_name="所属政策卡")

    class Meta:
        verbose_name = "专利限制"
        verbose_name_plural = verbose_name


class StaffLimit(models.Model):
    max_num = models.IntegerField('最大员工数量')
    max_flag = models.BooleanField('是否包括最大数量')
    min_num = models.IntegerField('最小员工数量')
    min_flag = models.BooleanField('是否包括最小数量')
    tech_emp_prop = models.FloatField('技术人员占比')
    
    bachelor_prop = models.FloatField('本科学历占比', blank=True, null=True)
    master_prop = models.FloatField('硕士及以上学历占比', blank=True, null=True)

    policy = models.ForeignKey(PolicyCard, on_delete=models.CASCADE, verbose_name="所属政策卡")

    class Meta:
        verbose_name = "员工限制"
        verbose_name_plural = verbose_name





