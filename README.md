# Personal File Search Utility

## a. Problem Being Solved

On my system, I regularly save important files such as certificates, resumes, assignments, and scanned documents using my name “pratiksha” in the file name.  
Over time, these files get stored across different folders, and I often forget their exact locations.

When I need these files urgently, manually browsing through multiple directories is time-consuming and inefficient.  
To address this real and recurring problem, I built a small command-line utility that searches for files containing a given keyword (for example, “pratiksha”) within a selected directory and all its subdirectories.

This utility allows me to quickly locate my personal files without manually navigating folder structures.

---

## b. How to Run the Program

1. Ensure that Python is installed on your system.
2. Save the source file as `filesearch.py`.
3. Open Command Prompt or Terminal.
4. Run the following command:

Search for files containing "pratiksha":
python filefinder.py C:\Users\Pratiksha --name pratiksha


Search by file extension:
python filefinder.py C:\Users\Pratiksha --ext .pdf

You can replace:
- `C:\Users\Pratiksha` with any directory path
- `pratiksha` with any keyword you want to search for

---

You can replace:
- `C:\Users\Pratiksha` with any directory path
- `pratiksha` with any keyword you want to search for

---

## c. Design Decisions

- I used only Python standard libraries (`os` and `argparse`) to strictly follow the assignment guidelines.
- `os.walk()` is used to recursively scan all subdirectories so that no folders are missed during the search.
- The program performs a simple case-insensitive keyword match on file names to make the search more user-friendly.
- A command-line interface was chosen because it is lightweight, scriptable, and easy to integrate into everyday workflows.
- Basic input validation is included to display a helpful message if the user forgets to provide the keyword.
- The output format is kept clean and readable to make results easy to scan.

The overall design focuses on correctness, clarity, and reliability rather than over-engineering.  
The program can be easily extended in the future to support features such as file extension filters, file size filters, or result sorting.

<img width="1426" height="573" alt="Screenshot 2026-01-20 150438" src="https://github.com/user-attachments/assets/e6214da0-6c6e-4bd7-a0a3-0264ea55ac54" />
<img width="1616" height="565" alt="Screenshot 2026-01-20 150457" src="https://github.com/user-attachments/assets/532553a9-b628-44e7-8ceb-e72e3f4aaaa1" />

