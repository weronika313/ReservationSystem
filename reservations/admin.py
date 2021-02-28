from django.contrib import admin

# Register your models here.
from .models import Reservation
from .models import RegularReservation
from .models import SingleRegularReservation
from .models import Room
from .models import Building
from .models import RoomType
from .models import RoomKeeper
from .models import Coordinator
from .models import Software
from .models import SoftwareRoom
from .models import Equipment
from .models import EquipmentRoom
from .models import ReservationType


@admin.register(ReservationType)
class ReservationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(SoftwareRoom)
class SoftwareRoomAdmin(admin.ModelAdmin):
    list_display = ("software", "room", "amount")
    raw_id_fields = ("software", "room")
    ordering = ("room",)


@admin.register(EquipmentRoom)
class EquipmentRoomAdmin(admin.ModelAdmin):
    list_display = ("equipment", "room", "amount")
    raw_id_fields = ("equipment", "room")
    ordering = ("room",)


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ("building", "user")
    raw_id_fields = ("building", "user")
    ordering = ("building",)


@admin.register(RoomKeeper)
class RoomKeeperAdmin(admin.ModelAdmin):
    list_display = ("room", "user")
    raw_id_fields = ("room", "user")
    ordering = ("room",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "start", "end", "amountOfPeople", "type", "status")
    list_filter = ("status", "start")
    search_fields = ("room", "user")
    raw_id_fields = ("user", "room", "type")
    date_hierarchy = "start"
    ordering = ("status", "start")


@admin.register(RegularReservation)
class RegularReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "room", "user", "start_time", "end_time", "day_of_week", "start_date", "end_date", "type", "status")
    list_filter = ("status", "start_time", "day_of_week", "start_date", "end_date")
    search_fields = ("room", "user", "day_of_week")
    raw_id_fields = ("user", "room", "type")
    date_hierarchy = "start_date"
    ordering = ("status", "start_time", "day_of_week")


@admin.register(SingleRegularReservation)
class RoomKeeperAdmin(admin.ModelAdmin):
    list_display = ("regular_reservation_group", "single_reservation")
    raw_id_fields = ("regular_reservation_group", "single_reservation")
    ordering = ("regular_reservation_group",)



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "maxNumberOfPeople", "building")
    list_filter = ("building",)
    raw_id_fields = ("building",)
    ordering = ("building",)
