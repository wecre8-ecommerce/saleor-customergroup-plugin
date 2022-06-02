import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from saleor.graphql.core.connection import (
    create_connection_slice, CountableConnection
)
from saleor.graphql.core.fields import FilterConnectionField
from saleor.graphql.product.filters import ProductVariantFilterInput
from saleor.graphql.product.types import ProductVariantCountableConnection
from customer_group import models


class CountableDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, *args, **kwargs):
        # Force it to use the countable connection
        countable_conn = CountableConnection.create_type(
            "{}CountableConnection".format(cls.__name__), node=cls
        )
        super().__init_subclass_with_meta__(*args, connection=countable_conn, **kwargs)


class CustomerGroup(CountableDjangoObjectType):
    variants = FilterConnectionField(
        ProductVariantCountableConnection,
        ids=graphene.List(
            graphene.ID, description="Filter product variants by given IDs."
        ),
        channel=graphene.String(
            description="Slug of a channel for which the data should be returned."
        ),
        filter=ProductVariantFilterInput(
            description="Filtering options for product variant."
        ),
        description="List of product variants.",
    )

    def resolve_variants(root, info, ids=None, channel=None, **kwargs):
        from saleor.graphql.channel import ChannelQsContext

        groups = models.CustomerGroup.objects.get(pk=root.id)
        qs = ChannelQsContext(groups.variants.all(), channel)
        return create_connection_slice(
            qs, info, kwargs, ProductVariantCountableConnection
        )

    class Meta:
        model = models.CustomerGroup
        filter_fields = ["id", "name", "description"]
        interfaces = (graphene.relay.Node,)


class CustomerGroupConnection(relay.Connection):
    class Meta:
        node = CustomerGroup
