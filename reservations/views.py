from django.http import HttpResponse
from django.template import loader

# wcięcia tabami

def index(request):
	template_name='ReservationSystem/index.html'
	template = loader.get_template(template_name)
	context = {}
	return HttpResponse(template.render(context))
	
	
def login(request):
	template_name='login/login.html'
	template = loader.get_template(template_name)
	context = {}
	return HttpResponse(template.render(context))	

	
def reservations_callendar(request):
	template_name='ReservationSystem/reservations_callendar.html'
	template = loader.get_template(template_name)
	context = {}
	return HttpResponse(template.render(context))
	
	
def room_reservation(request):
	template_name='ReservationSystem/room_reservation.html'
	template = loader.get_template(template_name)
	context = {}
	return HttpResponse(template.render(context))
	
	
def dorm_reservation(request):
	template_name='ReservationSystem/dorm_reservation.html'
	template = loader.get_template(template_name)
	context = {}
	return HttpResponse(template.render(context))