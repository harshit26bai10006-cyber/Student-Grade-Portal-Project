# Problem Statement & System Design Specification

## 📝 1. Problem Statement
Educational institutions require highly scalable systems to handle student registries, subject mapping configurations, score evaluation models, and analytical tracking records. Traditional command-line architectures often cluster multi-tier tasks into single massive scripts, resulting in low maintainability, hard-coded constraints, lack of security routing, and frequent crash events due to missing validation checks.

This project delivers a **Modular Student Grade Portal** that models a real-world university registrar framework. By dividing operations across five decoupled functional environments, the portal eliminates memory leakage, enforces strict academic data sanitization ranges, computes real-time performative matrices, and gates system monitoring logs behind an administrative credential firewall.

---

## ⚙️ 2. Core Operational Constraints & Rules

### 2.1 Registration & Identification Limits
*   **Age Range Constraints:** Enforces strict boundary verification where `17 <= Age <= 23`. Any values violating this rule are rejected immediately.
*   **Primary Key Assembly Pattern:** Registration IDs are dynamically assembled using the format string `"26" + "VIT" + str(10000 + len(database) + 1)`, ensuring a persistent, non-overlapping serial primary index for every student.

### 2.2 Marks Processing & Grading Parameters
*   **Sanitization Scope:** Valid inputs are rigidly bounded within `0.0 <= Mark <= 100.0`. Inputs violating these limits are blocked to prevent skewed analytics.
*   **Universal Course Tracking Matrix:** Common courses consist of *English*, *EVS*, and *Maths*. The fourth subject changes dynamically based on the student's chosen academic track shorthand code (*CSE*, *ME*, *CE*, *ECE*, *AE*).
*   **The Academic Grading Scale:**
    *   `>= 90` and `<= 100` → **S Grade** (Points Value: 10)
    *   `>= 80` and `< 90` → **A Grade** (Points Value: 9)
    *   `>= 70` and `< 80` → **B Grade** (Points Value: 8)
    *   `>= 60` and `< 70` → **C Grade** (Points Value: 7)
    *   `>= 50` and `< 60` → **D Grade** (Points Value: 6)
    *   `>= 40` and `< 50` → **E Grade** (Points Value: 5)
    *   `< 40` → **Fail Grade** (Points Value: 0)

---

## 📊 3. Internal Data Structure Schema

The application handles live runtime record snapshots using nested Python dictionaries structured under the following logical entity key layout mapping:

```python
student_list = {
    "26VIT10001": {
        "First Name": "Harshit",
        "Last Name": "Shah",
        "Age": 19,
        "Course": "Computer Science and Engineering(CSE)",
        "Marks": {
            "English": 92.0,
            "EVS": 88.0,
            "Maths": 95.0,
            "CSE": 90.0
        },
        "Grades": {
            "English": "S",
            "EVS": "A",
            "Maths": "S",
            "CSE": "S"
        },
        "Percentage": 91.25,
        "CGPA": 9.75,
        "Status": "Pass"
    }
}
```
