from django.db import models

class Supplier_Detail(models.Model):
    Supplier_id = models.CharField(max_length=30,primary_key=True)
    Supplier_name = models.CharField(max_length=50)
    Address = models.TextField()
    Contact = models.CharField(max_length=10,default=None)
    Email_id = models.EmailField()
    Nature_of_business = models.CharField(max_length=30)
    GST_no = models.CharField(max_length=30)
    Distributor = models.CharField(max_length=20)
    List_of_item = models.CharField(max_length=50)
    Details  = models.TextField(default = None)
    Details_file = models.FileField(default = None)
    Facilities = models.TextField(default = None)
    Facilities_file = models.FileField(default = None)
    Information = models.TextField()
    Datime = models.DateTimeField()
    Prepared_by = models.BooleanField(default=False)
    Approved_by = models.BooleanField(default=False)
    def __str__(self):
        return self.Supplier_id

class Supplier_Evaluation(models.Model):
    Supplier_detail = models.ForeignKey(Supplier_Detail,default=None,on_delete=models.CASCADE)
    Items = models.TextField()
    Period = models.CharField(max_length=100)
    Consistent_quality = models.BigIntegerField()
    Technical_capability = models.BigIntegerField()
    Experience = models.BigIntegerField()
    Credit_terms = models.BigIntegerField()
    Capability_to_meet = models.BigIntegerField()
    Quality = models.BigIntegerField()
    Total = models.BigIntegerField()
    Meeting_schedule = models.BigIntegerField()
    Conclusion = models.CharField(max_length=50)
    Assessed_by = models.BooleanField(default=False)
    Approved_by = models.BooleanField(default=False)
    Datime = models.DateTimeField()

class Supplier_rating(models.Model):
    Supplier_detail = models.ForeignKey(Supplier_Detail, default=None, on_delete=models.CASCADE)
    TOQ = models.IntegerField()
    Qty_WD = models.IntegerField()
    Qty_W7D = models.IntegerField()
    Qty_PFP = models.IntegerField()
    Qty_ILS = models.IntegerField()
    DR = models.DecimalField(max_digits=5,decimal_places=2)
    TQR = models.IntegerField()
    Ta_AWOD = models.IntegerField()
    Ta_AWD = models.IntegerField()
    IRD = models.IntegerField()
    QR = models.DecimalField(max_digits=5,decimal_places=2)
    SR = models.DecimalField(max_digits=5,decimal_places=2)
    Prepared_by= models.BooleanField(default=False)
    Approved_by = models.BooleanField(default=False)
    Datime = models.DateTimeField()

class Supplier_assessment(models.Model):
    Supplier_detail = models.ForeignKey(Supplier_Detail, default=None, on_delete=models.CASCADE)
    Term_1 = models.IntegerField()
    Term_2 = models.IntegerField()
    Term_3= models.IntegerField()
    Term_4 = models.IntegerField()
    Term_5 = models.IntegerField()
    Term_6 = models.IntegerField()
    Term_7 = models.IntegerField()
    Term_8 = models.IntegerField()
    Term_9 = models.IntegerField()
    Term_10 = models.IntegerField()



