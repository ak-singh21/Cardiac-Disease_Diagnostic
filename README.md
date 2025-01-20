# Rare Disease Diagnostic Assistant

## Overview
The **Rare Disease Diagnostic Assistant** is a Python-based tool made to assist users in identifying potential rare diseases based on the symptoms they input into the program. It uses a premade dataset of rare diseases and symptoms tied to it to provide suggestions.

## Features
- Matches user-provided symptoms to rare diseases in the dataset.
- Provides a list of potential rare diseases based on symptom overlap.
- Easy-to-use interface through the command line.

## How It Works
1. The program includes a dataset of rare diseases mapped to their symptoms.
2. Users input their symptoms as a comma-separated list.
3. The program checks the input symptoms against the dataset.
4. If matches are found, it lists the diseases that matches to the symptoms; otherwise, it tells the user that no matches were found.

## Dataset
The dataset currently includes the following rare diseases and their symptoms:

| Disease                  | Symptoms                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| Apert Syndrome           | Skull deformities, fusion of fingers, hearing loss                      |
| Ehlers-Danlos Syndrome   | Hyper-flexible joints, skin that bruises easily, chronic pain            |
| Marfan Syndrome          | Tall stature, long limbs, heart problems                                |
| Kleine-Levin Syndrome    | Excessive sleep, hyperphagia, behavioral changes                        |
| Stiff Person Syndrome    | Muscle stiffness, muscle spasms, anxiety                                |

## Functions
### `diagnose_disease(symptoms)`
- **Input:** A list of symptoms (e.g., `["excessive sleep", "anxiety"]`).
- **Output:** A list of diseases that match the symptoms.
- **Logic:** Matches any input symptom to the symptoms in the dataset.

### `main()`
- **Purpose:** Serves as the entry point for the program.
- **Functionality:**
  1. Prompts the user for symptoms.
  2. Processes the input and calls the `diagnose_disease` function.
  3. Displays matched diseases or indicates no matches found.
