from django.db import models

class register(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	adharno=models.CharField(max_length=60)

class register1(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	adharno=models.CharField(max_length=60)
	Image=models.CharField(max_length=60)

class issue1(models.Model):
	user=models.ForeignKey(register1,on_delete=models.CASCADE)
	Dept=models.CharField(max_length=60)
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)
	des=models.CharField(max_length=100)
	Status=models.CharField(max_length=50)
	Location=models.CharField(max_length=150)

class issue(models.Model):
	user=models.ForeignKey(register1,on_delete=models.CASCADE)
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)
	des=models.CharField(max_length=100)
	Status=models.CharField(max_length=50)
	Location=models.CharField(max_length=150)

class empreg(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	uname=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	rpassword=models.CharField(max_length=60)
	dob=models.CharField(max_length=60)
	gender=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	
class admin1(models.Model):
	username=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	
class report(models.Model):
	sugar=models.CharField(max_length=60)
	molass=models.CharField(max_length=60)
	filt=models.CharField(max_length=60)
	baga=models.CharField(max_length=60)
	straw=models.CharField(max_length=60)
	tops=models.CharField(max_length=60)
	total=models.CharField(max_length=60)

class report1(models.Model):
	user=models.ForeignKey(register1,on_delete=models.CASCADE)
	sugar=models.CharField(max_length=60)
	molass=models.CharField(max_length=60)
	filt=models.CharField(max_length=60)
	baga=models.CharField(max_length=60)
	straw=models.CharField(max_length=60)
	tops=models.CharField(max_length=60)
	total=models.CharField(max_length=60)
	dt=models.CharField(max_length=60, default=0)
	tton=models.CharField(max_length=60,default=0)
	ed=models.CharField(max_length=60,default=0)

# Create your models here.
