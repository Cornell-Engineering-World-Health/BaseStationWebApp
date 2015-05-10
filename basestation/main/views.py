from django.shortcuts import render

from django.http import HttpResponse

from .models import Nurse, Patient

from .forms import *

import pdb


# def index(request):
# 	nurse_list = Nurse.objects.all()
# 	context = {'nurse_list': nurse_list}
# 	return render(request, 'main/AdminPage.html',context)

def index(request):
      context = {}
      nurse_list = Nurse.listAll()
      patient_list = Patient.listAll()

      context['nurse_list'] = nurse_list
      context['patient_list'] = patient_list


      if request.method == "POST":
            add_patient =AddPatient(request.POST)
            edit_patient = EditPatient(request.POST)
            delete_patient = DeletePatient(request.POST)


            add_nurse = AddNurse(request.POST)
            edit_nurse = EditNurse(request.POST)
            delete_nurse = DeleteNurse(request.POST)


            if add_patient.is_valid():
                  p_id = add_patient.cleaned_data['p_id']
                  bed = add_patient.cleaned_data['bed']
                  condition = add_patient.cleaned_data['condition']

                  Patient.add(p_id,bed,condition)

            if edit_patient.is_valid():
                  p_id = edit_patient.cleaned_data['p_id']
                  bed = edit_patient.cleaned_data['bed']
                  condition = edit_patient.cleaned_data['condition']

                  Patient.edit(p_id,bed,condition)

            if delete_patient.is_valid():
                  p_id = delete_patient.cleaned_data['p_id']

                  Patient.delete(p_id)

            if add_nurse.is_valid():
                  name = add_nurse.cleaned_data['name']
                  number = add_nurse.cleaned_data['number']

                  Nurse.add(name,number)

            if edit_nurse.is_valid():
                  name = edit_nurse.cleaned_data['name']
                  number = edit_nurse.cleaned_data['number']

                  Nurse.edit(name,number)

            if delete_nurse.is_valid():
                  name = delete_nurse.cleaned_data['name']

                  Nurse.delete(name)
      else:
            add_patient = AddPatient()
            edit_patient = EditPatient()
            delete_patient = DeletePatient()

            add_nurse = AddNurse()
            edit_nurse = EditNurse()
            delete_nurse = DeleteNurse()


      context['add_patient'] = add_patient
      context['edit_patient'] = edit_patient
      context['delete_patient'] = delete_patient
      context['add_nurse'] = add_nurse
      context['edit_nurse'] = edit_nurse
      context['delete_nurse'] = delete_nurse


      return render(request, 'AdminPage.html', context)