import requests
from bs4 import BeautifulSoup

#Scrape WebMD for heart disease information
def get_heart_info(disease_name):
    #WebMD URLs for diseases
    disease_urls = {
        "Coronary Artery Disease": "https://www.webmd.com/heart-disease/coronary-artery-disease",
        "Heart Failure": "https://www.webmd.com/heart-disease/heart-failure/what-is-heart-failure",
        "Arrhythmia": "https://www.webmd.com/heart-disease/atrial-fibrillation/heart-disease-abnormal-heart-rhythm",
        "Cardiomyopathy": "https://www.webmd.com/heart-disease/muscle-cardiomyopathy",
        "Heart Valve Disease": "https://www.webmd.com/heart-disease/heart-valve-disease"
    }

    #Check if disease exists in our list
    url = disease_urls.get(disease_name)

    if not url:
        print(f"No URL found for {disease_name}")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                      "AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Get the title and first few paragraphs from the page
            title = soup.find("h1").text.strip() if soup.find("h1") else "No Title Found"
            paragraphs = soup.find_all("p")

            print(f"\n===== {title} =====\n")

            # Print first 5 paragraphs of info
            for para in paragraphs[:6]:
                print(para.get_text())
                print()

        else:
            print(f"Failed to get data from WebMD for {disease_name}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while fetching {disease_name}: {e}")

#Welcome message
print("Hello! I am your Heart Disease Diagnostic Bot!\nI will helping diagnose your heart disease today!")
print("Please answer the following questions with 'yes' or 'no'.")

#Collect symptoms from the user
symptoms = {}

symptoms["chest_pain"] = input("Do you have chest pain? ").lower()
symptoms["shortness_of_breath"] = input("Do you have shortness of breath? ").lower()
symptoms["fatigue"] = input("Do you feel unusually tired (fatigue)? ").lower()
symptoms["swelling_in_legs"] = input("Do you have swelling in your legs, ankles, or feet? ").lower()
symptoms["irregular_heartbeat"] = input("Do you have an irregular or fast heartbeat? ").lower()

#Scoring system for heart diseases
diseases = {
    "Coronary Artery Disease": 0,
    "Heart Failure": 0,
    "Arrhythmia": 0,
    "Cardiomyopathy": 0,
    "Heart Valve Disease": 0
}

#Add points to diseases based on symptoms
if symptoms["chest_pain"] == "yes":
    diseases["Coronary Artery Disease"] += 2
    diseases["Heart Valve Disease"] += 1

if symptoms["shortness_of_breath"] == "yes":
    diseases["Heart Failure"] += 2
    diseases["Cardiomyopathy"] += 1

if symptoms["fatigue"] == "yes":
    diseases["Heart Failure"] += 1
    diseases["Cardiomyopathy"] += 1

if symptoms["swelling_in_legs"] == "yes":
    diseases["Heart Failure"] += 2

if symptoms["irregular_heartbeat"] == "yes":
    diseases["Arrhythmia"] += 2
    diseases["Cardiomyopathy"] += 1

#Sort diseases by likelihood (highest score first)
sorted_diseases = sorted(diseases.items(), key=lambda x: x[1], reverse=True)

#Show top 5 diseases ranked 1-5
print("\nBased on your symptoms, here are the possible heart diseases:")
rank = 1
for disease, score in sorted_diseases:
    print(f"{rank}. {disease} ")
    rank += 1

#Call the WebMD scraping function
top_disease, top_score = sorted_diseases[0]
get_heart_info(top_disease)