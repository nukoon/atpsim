import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

world_file_name = 'atp_office/atpbot.model'
world = os.path.join(get_package_share_directory('atpbot_simulation'),'worlds', world_file_name)
launch_file_dir = os.path.join(get_package_share_directory('atpbot_simulation'), 'launch')
pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    
print(world_file_name)
print(world)
print(launch_file_dir)
