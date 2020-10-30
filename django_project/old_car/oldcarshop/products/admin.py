from django.contrib import admin
from .models.pro_info import ProBrand, ProDetail, ProCategory, ProImage
from .models.first_page_config import FirstPageSlide
from django.utils.html import format_html

admin.site.register(ProCategory)
admin.site.register(ProBrand)
admin.site.register(ProImage)


class ProDetailAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sale_status',
        'is_on_sale',
        'is_recommend',
        'category',
        'brand',
        'pro_model',
        'new_old',
        'fuel_type',
        'engine_model',
        'stock',
        'driver_seat',
        'engine_system',
        'original_use',
        'electric_system',
        'electric_system',
        'liquid_pressure_system',
        'outside_paint',
    )
    filter_horizontal = ('images',)
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'sale_status',
                    'is_on_sale',
                    'is_recommend',
                    'images',
                    'category',
                    'brand',
                    'pro_model',
                    'new_old',
                    'fuel_type',
                    'engine_model',
                    'stock',
                    'driver_seat',
                    'engine_system',
                    'original_use',
                    'electric_system',
                    'liquid_pressure_system',
                    'outside_paint',
                ),
            }
        ),
    )


class SlideAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_show',
        'element',
        'test_css'
    )
    fieldsets = (
        (
            None, {
                'fields': [
                    'name',
                    'is_show',
                    'element',
                    'product'
                ]
            }
        ),
    )
    list_filter = ('name', )

    def test_css(self, rec):
        html = """<a class="changelink" href="/admin/products/firstpageslide/%s/change/">编辑</a>""" % rec.id
        return format_html(html)

    test_css.short_description = '编辑'


admin.site.register(ProDetail, ProDetailAdmin)
admin.site.register(FirstPageSlide, SlideAdmin)

