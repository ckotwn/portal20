from django.contrib import admin

from .models import Taxon, TaxonTree, DataSet

class DataSetAdmin(admin.ModelAdmin):
    model = DataSet
    list_display = ('title', 'name', 'stats_num_occurrence', 'pub_date', 'guid')
    list_filter = ('is_most_project', 'dwc_core_type')
    fields = ('title', 'name', 'description','author', 'pub_date', 'guid', 'dwc_core_type', 'stats_num_record', 'stats_num_occurrence', 'stats_extensions', 'is_most_project')
    readonly_fields = ('title', 'name', 'description','author', 'pub_date', 'guid', 'dwc_core_type', 'stats_num_record', 'stats_num_occurrence', 'stats_extensions')


class TaxonAdmin(admin.ModelAdmin):
    model = Taxon
    list_filter = ('rank','tree')
    list_display = ('name', 'name_zh', 'rank', 'parent', 'count', 'tree')
    fields = (('parent','parent_id'), 'name', 'name_zh', 'rank', 'count', 'tree')
    readonly_fields = ('count', 'parent', 'parent_id')
    search_fields = ('name', 'name_zh')

class TaxonTreeAdmin(admin.ModelAdmin):
    model = TaxonTree
    list_display = ('name',)
    fields = ('name', 'rank_map')


admin.site.register(Taxon, TaxonAdmin)
admin.site.register(TaxonTree, TaxonTreeAdmin)
admin.site.register(DataSet, DataSetAdmin)
