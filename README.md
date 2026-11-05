# Page Replacement Algorithms Visualizer 🖥️

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Course](https://img.shields.io/badge/Course-Operating%20Systems-orange.svg)

## 📌 Project Overview
This project is an **Operating System Project-Based Learning (PBL)** assignment that simulates and visualizes how different Page Replacement Algorithms manage memory. 

In modern operating systems, virtual memory allows processes to execute even if they are not entirely in main memory (RAM). When a process requests a page not currently in memory, a **Page Fault** occurs. If the memory is full, the OS must swap out an existing page using a specific algorithm. This visualizer helps users understand the inner workings of three fundamental algorithms: **FIFO, LRU, and Optimal**.

## ✨ Features
* **Interactive Graphical User Interface (GUI):** Built completely in Python using the `tkinter` library.
* **Dynamic Inputs:** Users can enter their own reference string (sequence of requested pages) and specify the number of memory frames.
* **Step-by-Step Visualization:** The GUI visually maps out the memory state at each step of the reference string.
* **Page Fault Highlighting:** Clearly distinguishes between a "Page Hit" and a "Page Fault" (highlighted in red) to show when a page replacement actually occurs.
* **Comparative Analysis:** Easily run the same reference string through all three algorithms to compare their efficiency and total page fault counts.

## 🧠 Algorithms Implemented

1. **First-In, First-Out (FIFO):** Replaces the oldest page in memory. Simple to implement using a queue, but susceptible to *Belady's Anomaly* (where increasing frames can increase page faults).
2. **Least Recently Used (LRU):** Replaces the page that has not been accessed for the longest period. It effectively utilizes spatial and temporal locality.
3. **Optimal Page Replacement:** Replaces the page that will not be needed for the longest time in the future. While impossible to implement in real-time OS (as it requires predicting the future), it serves as the benchmark for maximum efficiency.

## 🛠️ Prerequisites
To run this project, you only need Python installed on your system. The GUI is built using `tkinter`, which is included in the standard Python library.
* Python 3.x

## 🚀 How to Run
1. Clone this repository to your local machine
2. Navigate to the project directory
3. Run the Python script

## 📖 How to Use the Visualizer
1. Launch the application.
2. Enter a **Reference String** (e.g., `7 0 1 2 0 3 0 4 2 3 0 3 2`). Space-separated numbers are recommended depending on your input handling.
3. Enter the **Number of Frames** (e.g., `3` or `4`).
4. Select the algorithm you wish to visualize (FIFO, LRU, or Optimal).
5. Watch the memory grid update step-by-step and observe the final Page Fault count!

## 👥 Team Members
**Group - B.Tech CSE-2 Third Year (Odd Semester 2026)**
* **Vaishnavi Vashisth** (Enrollment: 07411502724)
* **Gauri Aggarwal** (Enrollment: 11011502724)
* **Bhavya Sharma** (Enrollment: 12111502724)

*Submitted to: Dr. Aarti | Bharati Vidyapeeth’s College of Engineering, New Delhi*
