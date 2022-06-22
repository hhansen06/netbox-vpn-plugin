from setuptools import find_packages, setup

setup(
    name='netbox-vpn-plugin',
    version='0.3.1',
    description='Manage VPN Connections in Netbox',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)