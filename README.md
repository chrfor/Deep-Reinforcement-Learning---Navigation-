# Deep-Reinforcement-Learning---Navigation-
Udacity Deep Reinforcement Learning - Navigation project implementation
README.md

Project Details (Form Udacity Navigation project description )

The simulation contains a single agent that navigates a large environment. At each time step, it has four actions at its disposal:
0 - walk forward
1 - walk backward
2 - turn left
3 - turn right
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes. It does not happen with the current version of the Agent/Model.


Getting Started

The files must be installed following the explication here under (Mostly from Udacity )

Step 1: Clone https://github.com/chrfor/Deep-Reinforcement-Learning---Navigation-
If you haven't already, please follow the instructions in the DRLND GitHub repository(https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

(For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.

Step 2: Download the Unity Environment
For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

Linux: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip
Mac OSX: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip
Windows (32-bit): click here
Windows (64-bit): click here

Then, place the file in the same folder as where the Navigation github has been cloned and unzip (or decompress) the file.

(For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to enable a virtual screen, and then download the environment for the Linux operating system above.)


Instructions

The README describes how to run the code in the repository, to train the agent. For additional resources on creating READMEs or using Markdown, see here and here.

Once all the files installed. Please followed the sequence here under :
Go to your console 
Get to the folder where you clone Navigation github and the unity environment 
Type Jupyter Notebook 
Open "Navigation" by clicking on it
Go to Kernel, select Select "Change Kernel" to drlnd
Go to kernel and "Restart & Run all" to have all the agent starting to learn

