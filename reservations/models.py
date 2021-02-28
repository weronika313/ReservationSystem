from django.db import models
from django.urls import reverse
from users.models import CustomUser as User

# Create your models here.


class AcceptedManager(models.Manager):
    def get_queryset(self):
        return super(AcceptedManager, self).get_queryset().filter(status="accepted")


STATUS_CHOICES = (
    ("waiting", "Waiting"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    )


class Reservation(models.Model):
    STATUS_CHOICES = (
        ("waiting", "Waiting"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    amountOfPeople = models.IntegerField()
    comment = models.TextField(
        max_length=200,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    type = models.ForeignKey("ReservationType", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="waiting")

    def __str__(self):
        return self.id

    objects = models.Manager()  # The default manager.
    accepted = AcceptedManager()  # Our custom manager.


class RegularReservation(models.Model):
    DAYS_OF_WEEK = (
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    )

    name = models.CharField(max_length=40)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    day_of_week = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey("ReservationType", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="waiting")
    reservations = models.ManyToManyField(
        Reservation, through="SingleRegularReservation"
    )


class SingleRegularReservation(models.Model):
    regular_reservation_group = models.ForeignKey(
        "RegularReservation", on_delete=models.CASCADE
    )
    single_reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)


class ReservationType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Software(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=40)
    maxNumberOfPeople = models.IntegerField()
    building = models.ForeignKey("Building", on_delete=models.CASCADE)
    type = models.ForeignKey("RoomType", on_delete=models.CASCADE)
    softwares = models.ManyToManyField(Software, through="SoftwareRoom")
    equipments = models.ManyToManyField(Equipment, through="EquipmentRoom")
    room_keepers = models.ManyToManyField(User, through="RoomKeeper")
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("rezerwacje:room_detail", args=[self.name, self.slug])

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, unique=True)
    coordinators = models.ManyToManyField(User, through="Coordinator")

    def get_absolute_url(self):
        return reverse("rezerwacje:building_detail", args=[self.name, self.slug])

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class SoftwareRoom(models.Model):
    amount = models.IntegerField()
    software = models.ForeignKey("Software", on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


class EquipmentRoom(models.Model):
    amount = models.IntegerField()
    amount_of_free_equipment = models.IntegerField()
    equipment = models.ForeignKey("Equipment", on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


class Coordinator(models.Model):
    building = models.ForeignKey("Building", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class RoomKeeper(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
