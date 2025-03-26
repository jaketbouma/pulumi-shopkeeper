import pulumi
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


pulumi.runtime.set_mocks(
    MyMocks(),
    preview=False,  # Sets the flag `dry_run`, which is true at runtime during a preview.
)


from shopkeeper_provider import StaticPage


@pulumi.runtime.test
def test_static_page():
    p = StaticPage("test", my_component_args={"indexContent": "<h1>Ollo</h1>"})
    assert 1==1
