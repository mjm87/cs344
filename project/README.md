This is a project designed to extend the Puppo the Corgi example project from Unity Technologies
which showcases some of the tools provided in Unity's ML-Agents Toolkit for game developers to
more easily embrace some of the cool advancements in AI, particularly reinforcement learning.

This project's goal was to get a starship to sucessfully navigate a labyrinth.

Due to Github size limitations, only the code and assets that I created specifically were kept. The only script files that I added were the ObstacleScript.cs and the myriad of PilotAgentSM0*.cs which contain the various adaptations to the Player Agent that accrued during development. 

To install / replicate:

1. Download the Puppo the Corgi sample code from Unity. (https://blogs.unity3d.com/2018/10/02/puppo-the-corgi-cuteness-overload-with-the-unity-ml-agents-toolkit/)

2. Go through the installation steps provided with the sample project.
    - installing the correct version of python / tensorflow / ml-agents-toolkit

3. Copy the Unity3D folder into the Assets folder of the Corgi project

4. SimpleMaze01, SimpleMaze02, and SimpleMaze04 have internal byte-compiled models ready to run if you simply open up the scenes, training involves the additional steps.

5. Tweak and have fun!