from setuptools import find_packages, setup

package_name = 'vlm_api'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='trace',
    maintainer_email='trace@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'command_publisher = vlm_api.command_publisher:main',
        'vla_publisher0203= vlm_api.vla_publisher0203:main'
    ],
    },
)
