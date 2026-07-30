# POLYMORPHISM-Traffic-Management-System

## Overview
This repository contains a Python implementation of a Smart Traffic Management System. It is designed as a case study to demonstrate core Object-Oriented Programming (OOP) principles, specifically **inheritance**, **method overriding**, and **polymorphism**.

## Features
* **Parent Class (`TrafficDevice`):** Establishes a common blueprint with a base `activate()` method.
* **Child Classes:** Includes `TrafficLight`, `SpeedCamera`, `PedestrianSignal`, and `EmergencySiren`.
* **Method Overriding:** Each child class provides its own unique implementation of the `activate()` method so that each device performs a different task.
* **Polymorphism in Action:** All devices are stored in a single list and activated through a unified loop. The loop calls the `activate()` method without needing to check or know the specific type of each device.
* **Extensibility:** Easily accommodates the addition of a new `EmergencySiren` class without requiring any modifications to the core activation loop, adhering to clean coding practices.

## How to Run
1. Ensure you have Python installed on your machine.
2. Clone this repository or download the python file (e.g., `main.py`).
3. Open your terminal or command prompt and navigate to the folder containing the file.
4. Run the script using the following command:
   ```bash
   python main.py
