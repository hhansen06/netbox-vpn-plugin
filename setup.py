from setuptools import find_packages, setup

setup(
    name='netbox-vpn-plugin',
    version='0.4',
    download_url='https://github.com/hhansen06/netbox-vpn-plugin/archive/refs/tags/0.4.tar.gz'
    description='Manage VPN Connections in Netbox',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
