from django.contrib import admin
from auctions.models import *

admin.site.register(Watchlist)
admin.site.register(Listings)
admin.site.register(User)
admin.site.register(Bids)
admin.site.register(Comments)