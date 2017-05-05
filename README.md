# CS5800-bridge
Programming Project for CS5800 (Distributed Operating Systems at Missouri S&amp;T). Design and implement a message passing channel based on the problem specifications.

## Problem Description
Two towns A and B are connected with a bridge. Suppose there are four people and their moving directions are indicated by the arrows. The bridge is narrow, and at any time, multiple people cannot pass in the opposite directions.
  1. Based on the Ricart & Agrawales mutual exclusion algorithm, design a decentralized protocol so that at most one person can be on the bridge at any given time, and no person is indefinitely prevented from crossing the bridge. Treat each person to be a process, and assume that there clocks are synchronized.
  2. Design another protocol so that multiple people can be on the bridge as long as they are moving in the same direction but no person is indefinitely prevented from crossing the bridge.

Design a GUI to display the movement of the people, so that the instructor can control the walking speed of the people and verify the protocol. Note that to receive full credit, you should provide instructions on how to compile and run your program, and your program should be well-documented.


## Prerequisites
**Must have python 3 installed on computer (possibly 3.5)**

## Installing
**Download the submitted zipfile and extract it to its own folder. It should have 3 pictures, the program, and the readme**

## Running
**open the command prompt and type "python3 bridgeSimV3.py" or however you would normally run a python file**

## Authors
* Tyler Hembrock: Thembro01
* Alex Marey: AlexMarey
* Tyler Percy: tcphw5
