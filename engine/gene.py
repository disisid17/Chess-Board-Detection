import argparse
 
import torch

import genesis as gs

import numpy as np
franka = None
def main():
    global franka

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vis", action="store_true", default=False)
    args = parser.parse_args()

    ########################## init ##########################
    gs.init(backend=gs.cpu)

    ########################## create a scene ##########################

    scene = gs.Scene(
        sim_options=gs.options.SimOptions(),
        viewer_options = gs.options.ViewerOptions(
        res           = (1280, 960),
        camera_pos    = (3.5, 0.0, 2.5),
        camera_lookat = (0.0, 1.0, 0.5),
        camera_fov    = 40,
        ),
        show_viewer=args.vis,
        rigid_options=gs.options.RigidOptions(
            dt=0.01,
            gravity=(0.0, 0.0, -10.0),
        ),
    )

    ########################## entities ##########################
    plane = scene.add_entity(
        gs.morphs.Plane(),
    )
    cube = scene.add_entity(
        gs.morphs.Box(
            size = (0.04, 0.04, 0.04),
            pos  = (0.65, 0.0, 0.02),
        )
    )
    franka = scene.add_entity(
        gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
    )

    ########################## build ##########################
    scene.build()

    motors_dof = np.arange(7)
    fingers_dof = np.arange(7, 9)

    # set control gains
    # Note: the following values are tuned for achieving best behavior with Franka
    # Typically, each new robot would have a different set of parameters.
    # Sometimes high-quality URDF or XML file would also provide this and will be parsed.
    franka.set_dofs_kp(
        np.array([4500, 4500, 3500, 3500, 2000, 2000, 2000, 100, 100]),
    )
    franka.set_dofs_kv(
        np.array([450, 450, 350, 350, 200, 200, 200, 10, 10]),
    )
    franka.set_dofs_force_range(
        np.array([-87, -87, -87, -87, -12, -12, -12, -100, -100]),
        np.array([ 87,  87,  87,  87,  12,  12,  12,  100,  100]),
    )

    gs.tools.run_in_another_thread(fn=run_sim, args=(scene, args.vis))
    if args.vis:
        scene.viewer.start()


def run_sim(scene, enable_vis):
    from time import time

    t_prev = time()
    i = 0
    
    i += 1

    scene.step()

    t_now = time()
    print(1 / (t_now - t_prev), "FPS")
    t_prev = t_now
    end_effector = franka.get_link('hand')

    # move to pre-grasp pose
    qpos = franka.inverse_kinematics(
        link = end_effector,
        pos  = np.array([0.65, 0.0, 0.25]),
        quat = np.array([0, 1, 0, 0]),
    )
    # gripper open pos
    qpos[-2:] = 0.04
    path = franka.plan_path(
        qpos_goal     = qpos,
        num_waypoints = 200, # 2s duration
    )
    # execute the planned path
    for waypoint in path:
        franka.control_dofs_position(waypoint)
        scene.step()

    # allow robot to reach the last waypoint
    for i in range(100):
        scene.step()

    if enable_vis:
        scene.viewer.stop()


if __name__ == "__main__":
    main()