from saleor.graphql.views import GraphQLView
from saleor.plugins.base_plugin import BasePlugin
from customer_group.graphql.schema import schema


class CustomerGroupPlugin(BasePlugin):
    PLUGIN_ID = "customer.group"
    PLUGIN_NAME = "Customer Group"
    DEFAULT_ACTIVE = True
    CONFIGURATION_PER_CHANNEL = False

    def webhook(self, request, path, previous_value):
        view = GraphQLView.as_view(schema=schema)
        request.app = self
        return view(request)
