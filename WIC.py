import time

class Candidate:
    def __init__(self, name):
        self.name = name
        self.skills = []
        self.experience = {}
        self.program = {}
        self.participation={}

    def introduce(self):
        print(f"🚀 Running Candidate: {self.name}")
        time.sleep(1.5)

    def get_experience(self):
        print("\n🔹 Experience:")
        time.sleep(1)
        for category, items in self.experience.items():
            print(f"  {category}:")
            for item in items:
                print(f"    - {item}")
                time.sleep(1)
    
    def get_participation(self):
        print("\nMy WIC Participation:")
        for category, items in self.participation.items():
            print(f"\n{category}:")
            for item in items:
                print(f"- {item}")
                time.sleep(1)

    def get_skills(self):
        print("\n🔹 Skills:\n")
        time.sleep(1)
        for skill in self.skills:
            print(f"✔️ {skill}")
            time.sleep(0.8)

    def get_program(self):
        print("\n🔹 Initiative: Quarter-Long Skill Path Series\n")
        time.sleep(1.5)
        print(self.program["Description"])
        time.sleep(2)
        print("\n🎯 Goals:")
        time.sleep(1)
        for goal in self.program["Goals"]:
            print(f"   - {goal}")
            time.sleep(1)
        print()
        time.sleep(2)

class Me(Candidate):
    def __init__(self):
        super().__init__("Me")
        self.skills = ["Public Speaking", "Event Planning", "Technical Teaching", "Python", "Java"]
        self.experience = {
            "Writing & Research": [
                "📝 Science Writer & Director at The Affair Magazine (6000+ readership)",
                "📊 Mind Out Loud Research Committee: Synthesized mental health research.",
                "📚 Project: Addressing Student Mental Health – Led data analytics for guidebook."
            ],
            "Leadership & Mentorship": [
                "🎾 Tennis Co-Captain: Coordinated team logistics & mentored players.",
                "💡 Mind Out Loud Admin: Led wellness moments & community-building.",
                "🧮 Mathematics Student Aide: Reinforced math concepts for young learners."
            ],
            "Technical & Project Experience": [
                "🌐 WIC Project Team – Triton Treasure Map: Developed interactive site.",
                "🎶 DSC 10 Midterm – Taylor Swift Analysis: Built song recommender.",
                "📺 DSC 10 Final – Rebooting Friends: Simulated an optimal reboot using data."
            ],
            "Community & Volunteer Work": [
                "📚 Library Volunteer: Designed displays & assisted in events.",
                "📖 Tutor at Kumon: Tutored ages 3-16 in Math & English."
            ]
        }
        self.program = {
            "Initiative": "Quarter-Long Skill Path Series",
            "Description": (
                "Each quarter, students focus deeply on a technical skill.\n"
                "Examples: a 10-week C++ series with weekly mini-projects, LeetCode prep, & a final project in the last 2 weeks that can be expanded upon\n"
                "or a Machine Learning series with each week dedicated learning a new type of model, and each student researches a specific model more deeply as a final project\n"
            ),
            "Goals": [
                "📌 Provide first-years with a head start in industry skills.",
                "📌 Offer structured learning with hands-on projects & mentorship.",
                "📌 Help students build technical confidence early."
            ]
        }
        self.participation = {
            "Workshops": ["HTML Workshop", "CSS Workshop"], "Project Teams": ["Fall 2024"], "Company Events": ["WIC x ServiceNow", "WIC x CoStar", "WIC x Intuit", "WIC x Qualcomm", "WIC x Northrop Gruman"],
            "Information Panels": ["ERSP Informational Panel", "WIC x HKN: Professor Panel"]

        }
class WIC:
    def get_best_tech_dev_chair(self, candidate):
        print("\n🛠️  Compiling the best Tech Dev-Events Chair... ")
        time.sleep(1)  

        
        for _ in range(3):
            print("🔎 Evaluating candidate...")
            time.sleep(1)

        print(f"\n🎉 Congratulations! WIC has selected {candidate.name} as the best Tech Dev-Events Chair!")
        print("💡 Why? Innovation, mentorship, a strong technical foundation in the making, and a vision for WIC.")
        print("\n✅ Candidate successfully installed!")
        time.sleep(3)

me = Me()
wic = WIC()

me.introduce()
time.sleep(1)
me.get_participation()
time.sleep(1)
me.get_experience()
time.sleep(0.5)
me.get_skills()
time.sleep(0.5)
me.get_program()
time.sleep(3)

wic.get_best_tech_dev_chair(me)