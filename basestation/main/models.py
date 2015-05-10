from django.db import models

# Create your models here.
class Nurse(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    @classmethod
    def add(cls, n, num):
    	Nurse.objects.create(name=n, number=num)
    	# new_nurse.save()

    @classmethod
    def delete(cls, n):
    	Nurse.objects.filter(name=n).delete()

    @classmethod
    def edit(cls, n, new_num):
    	nurse = Nurse.objects.get(name=n)
    	if (new_num != ""): nurse.number = new_num
    	nurse.save()

    @classmethod
    def listAll(cls):
    	html_out = "<table class='table table-striped'>"
    	html_out += "<thead><th>Name</th><th>Phone #</th></thead><tbody>"

    	nurses = Nurse.objects.order_by('name')

    	if (not nurses) : return "No nurses"

    	for nurse in nurses:
    		name = nurse.name
    		number = nurse.number
    		html_out += "<tr>"
    		html_out += "<td>" + name + "<td>"
    		html_out += "<td>" + number + "<td>"
    		html_out += "</tr>"

    	html_out += "</tbody></table>"

    	return html_out

    def __str__(self):
    	return self.name + " & " + self.number 


class Patient(models.Model):
    p_id = models.CharField(max_length=10)
    bed = models.CharField(max_length=10)
    condition = models.IntegerField()

    @classmethod
    def add(cls, p, b, c):
    	Patient.objects.create(p_id=p, bed=b, condition=c)
    	# new_patient.save()

    @classmethod
    def delete(cls, p):
    	Patient.objects.filter(p_id=p).delete()

    @classmethod
    def edit(cls, p, new_b, new_c):
    	patient = Patient.objects.get(p_id=p)
    	if (new_b != ""): patient.bed = new_b
    	if (new_c != ""):patient.condition = new_c
    	patient.save()


    @classmethod
    def listAll(cls):
    	html_out = "<table class='table table-striped'>"
    	html_out += "<thead><th>ID</th><th>Bed</th><th>Condition</th></thead><tbody>"

    	patients = Patient.objects.order_by('p_id')

    	if (not patients) : return "No patients"

    	for patient in patients:
    		p = patient.p_id
    		b = patient.bed
    		c = patient.condition
    		html_out += "<tr>"
    		html_out += "<td>" + p + "<td>"
    		html_out += "<td>" + b + "<td>"
    		html_out += "<td>" + str(c) + "<td>"
    		html_out += "</tr>"

    	html_out += "</tbody></table>"

    	return html_out

	def __str__(self):
		return self.p_id + " & " + self.bed + " & " + self.condition