from setuptools import setup

setup(
    name="customer-group",
    version="0.1.0",
    packages=["customer_group"],
    package_dir={"customer_group": "customer_group"},
    description="Tappy payment plugin",
    entry_points={
        "saleor.plugins": ["customer_group = customer_group.plugin:CustomerGroupPlugin"],
    },
)
