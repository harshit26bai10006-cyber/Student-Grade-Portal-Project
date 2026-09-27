# Student Grade Portal Project 🎓

A highly interactive, modular **Student Grade Portal** developed in Python for the CSE1021 course assessment. This project models end-to-end academic records lifecycle management for an engineering department using native, memory-efficient data structures (dictionaries and list arrays) without requiring external DBMS dependencies.

---

## 🛠️ Key Features

*   **Student Registry Center:** Automates the enrollment process, validates student age range thresholds (17–23), and dynamically computes distinct primary identifiers matching institutional conventions (e.g., `26VIT10001`).
*   **Grading & Evaluation Engine:** Supports custom academic score matrices matching five engineering streams (CSE, ME, CE, ECE, AE) with rigid bounding filters (0–100) to block out-of-bounds metrics. Computes total marks, relative percentages, and universal 10-point scale CGPA letter grades (S, A, B, C, D, E, Fail).
*   **Performance Metrics Visualizer:** Dynamically maps raw scores into inline console-rendered graphical histograms utilizing text-based spacing controls (`.ljust()`).
*   **Multi-Tier Sorted Leaderboards:** Real-time scoreboard rankings enabling instant directory sorting filtering by global CGPA, average percentages, or individual subject distributions (English, EVS, Maths, or core engineering disciplines).
*   **Administrative Security Wall:** Enforces standard credential authorization gates, hosts system metadata logging counters, and isolates high-privilege operations such as master database resets.

---

## 📂 Project Architecture & File Structure

The application strictly separates processing responsibilities into dedicated files to guarantee maintainability and prevent database corruption:

*   `Main.py` — The core execution loop hosting the centralized system dashboards and nested navigation loops.
*   `Records.py` — The data entry module controlling profiles creation, custom ID generation sequence, data updates, and exclusions.
*   `Grading.py` — The primary evaluation tier managing subject marks insertion, mathematical grade computations, and profile changes.
*   `Analytics.py` — The visualizer module rendering performance charts and compiling sorted score ranking matrices.
*   `Admin.py` — The security perimeter validation system managing user tracking logs and high-privilege data clear flags.

---

## 🚀 Getting Started

### Prerequisites
To deploy and execute this project locally, you only need **Python 3.x** installed on your operating system. 

### Installation & Execution
1. Clone this repository to your hard drive using a terminal application:
   ```bash
   git clone https://github.com/harshit26bai10006-cyber/Student-Grade-Portal-Project
   ```

2. Navigate inside the project root folder directory:
   ```bash
   cd Student-Grade-Portal-Project
   ```

3. Boot up the primary operational console portal:
   ```bash
   python Main.py
   ```

---

## 🛡️ Non-Functional Project Requirements

To satisfy the engineering assessment rubrics, the codebase balances the following performance baselines:
1.  **Maintainability:** Code modifications to the grading algorithms or registration filters can be executed inside localized modules without causing regressions across adjacent routing scripts.
2.  **Usability:** Menus utilize intuitive flag selection paths, visual grid padding, and early-exit loop options (such as strip processing on update inputs) to maximize clarity.
3.  **Reliability:** Core memory references are protected by passing data states consistently through strict `return student_list` assignments on every operational exit path, neutralizing `NoneType` value crashes.
4.  **Resource Efficiency:** Database read/write computations achieve near O(1) constant time complexity bounds by using native nested dictionaries mapped to unique primary keys instead of resource-heavy database interfaces.
