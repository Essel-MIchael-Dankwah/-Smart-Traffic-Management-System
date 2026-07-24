# ABSTRACTION-Smart-Traffic-Management-System

## Introduction
Welcome to the Smart Traffic Management System repository! This project is a case study demonstrating the principles of Object-Oriented Programming (OOP), specifically focusing on **Data Abstraction**. 

## Task Summary
In a smart city, various intelligent traffic devices need to be managed centrally. Every device receives a standard `activate()` command, but the complex internal workings of each specific device are abstracted away from the main system.

This program models that system by:
1. Creating an abstract parent class `TrafficDevice` that defines the required blueprint.
2. Implementing specific child classes (`TrafficLight`, `SpeedCamera`, `PedestrianSignal`, and an `EmergencySiren`).
3. Using an abstract method to enforce that each child class handles its own `activate()` logic.
4. Grouping all devices into a single list and activating them sequentially.

By utilizing abstraction, the central activation loop interacts only with a simplified, unified interface. It does not need to know the specific underlying code or type of each device, ensuring the system's complexity remains hidden and modular.
