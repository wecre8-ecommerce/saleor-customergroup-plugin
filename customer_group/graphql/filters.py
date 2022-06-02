import django_filters

from saleor.graphql.core.filters import MetadataFilterBase
from saleor.graphql.core.types.filter_input import FilterInputObjectType

from customer_group import models


def filter_by_query_param(queryset, query, search_fields):
    """Filter queryset according to given parameters.

    Keyword Arguments:
        queryset - queryset to be filtered
        query - search string
        search_fields - fields considered in filtering

    """
    if query:
        query_by = {
            "{0}__{1}".format(field, "icontains"): query for field in search_fields
        }
        query_objects = Q()
        for q in query_by:
            query_objects |= Q(**{q: query_by[q]})
        return queryset.filter(query_objects).distinct()
    return queryset


def filter_group_search(qs, _, value):
    group_fields = ["name"]
    qs = filter_by_query_param(qs, value, group_fields)
    return qs


class GroupFilter(MetadataFilterBase):
    search = django_filters.CharFilter(method=filter_group_search)

    class Meta:
        model = models.CustomerGroup
        fields = ["search"]


class GroupFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = GroupFilter
