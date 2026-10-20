
DISEASES = {

    "healthy": {

        "id": "healthy",
        "name": "Healthy",
        "icon": "",
        "color": "#10B981",
        "tagline": "Normal respiratory function",
        "key_stat": "Healthy lungs take ~20,000 breaths/day",
        "overview": (
            "Healthy lungs produce clear, consistent breath sounds without any abnormal "
            "noises such as wheezing, crackling, or stridor. Normal respiratory function "
            "involves smooth, unobstructed airflow through the airways with an average "
            "adult respiratory rate of 12–20 breaths per minute at rest.\n\n"
            "The lungs contain approximately 300 million alveoli providing a total surface "
            "area of about 70 square meters for gas exchange. Healthy lung tissue is elastic, "
            "expanding and contracting efficiently with each breath. Maintaining lung health "
            "is essential for overall well-being, as the respiratory system is the primary "
            "mechanism for oxygen delivery and carbon dioxide removal.\n\n"
            "Regular exercise, avoiding smoking, and minimizing exposure to air pollution "
            "are key factors in preserving lung function throughout life. Lung function "
            "naturally declines with age, but healthy habits can slow this decline significantly."
        ),

        "breath_sounds": (
            "Normal breath sounds include vesicular sounds (soft, rustling sounds heard over "
            "most of the lung fields during inspiration), bronchial sounds (louder, hollow sounds "
            "heard over the trachea), and bronchovesicular sounds (intermediate sounds heard near "
            "the main bronchi). All sounds are clear, symmetrical, and without additional noises."
        ),

        "symptoms": [

            {
                "name": "Clear breathing",
                "description": "Smooth, effortless airflow with no wheezing, crackling, or labored breathing. Respiratory rate is 12–20 breaths per minute at rest.",
                "icon": ""
            },

            {

                "name": "Good exercise tolerance",
                "description": "Ability to perform moderate physical activity without excessive shortness of breath or unusual fatigue.",
                "icon": ""

            },

            {

                "name": "Normal oxygen saturation",
                "description": "Blood oxygen levels (SpO2) consistently between 95–100%, indicating efficient gas exchange in the lungs.",
                "icon": ""

            },

            {

                "name": "Symmetrical chest expansion",
                "description": "Both sides of the chest expand equally during breathing, indicating uniform lung inflation.",
                "icon": ""

            },

            {

                "name": "No persistent cough",
                "description": "Absence of chronic cough or excessive mucus production, indicating healthy airway clearance mechanisms.",
                "icon": ""

            },

            {

                "name": "Restful sleep",
                "description": "No breathing difficulties during sleep, no snoring related to airway obstruction, and waking feeling refreshed.",
                "icon": ""

            }

        ],

        "causes_risk_factors": [

            {
                "name": "Regular exercise",
                "description": "Aerobic activities like walking, swimming, and cycling strengthen respiratory muscles and improve lung capacity by up to 15%.",
                "icon": ""

            },

            {

                "name": "Non-smoking status",
                "description": "Avoiding tobacco smoke is the single most important factor for maintaining lung health. Smoke damages cilia and alveoli irreversibly.",
                "icon": ""

            },

            {

                "name": "Clean air environment",
                "description": "Living in areas with low air pollution and using air purifiers indoors reduces exposure to particulate matter and irritants.",
                "icon": ""

            },

            {

                "name": "Balanced nutrition",
                "description": "Diets rich in antioxidants (vitamins C, E), omega-3 fatty acids, and anti-inflammatory foods support lung tissue health.",
                "icon": ""

            },

            {

                "name": "Vaccinations",
                "description": "Staying up-to-date with influenza and pneumococcal vaccines prevents infections that can damage lung tissue.",
                "icon": ""

            }

        ],

        "stages": [

            {

                "name": "Vesicular sounds",
                "description": "Soft, low-pitched, rustling sounds heard over most of the peripheral lung fields. Inspiratory phase is longer than expiratory. This is the most common normal breath sound.",
                "severity": "mild"

            },

            {

                "name": "Bronchovesicular sounds",
                "description": "Medium-pitched sounds heard near the main bronchi (anterior first and second intercostal spaces, posterior between scapulae). Equal inspiratory and expiratory phases.",
                "severity": "mild"

            },

            {

                "name": "Bronchial (tracheal) sounds",
                "description": "Loud, high-pitched, hollow sounds heard over the trachea and larynx. Expiratory phase is longer than inspiratory. Normal only when heard over the trachea.",
                "severity": "mild"

            }

        ],

        "diagnosis": [

            {

                "method": "Auscultation",
                "description": "Listening to breath sounds with a stethoscope to confirm clear, symmetric airflow without adventitious sounds."

            },

            {

                "method": "Spirometry",
                "description": "Pulmonary function test measuring FEV1 and FVC. Normal FEV1/FVC ratio is ≥0.70 in adults, confirming no obstruction."

            },

            {

                "method": "Pulse oximetry",
                "description": "Non-invasive measurement of blood oxygen saturation. Normal SpO2 is 95–100%."

            },

            {

                "method": "Chest X-ray",
                "description": "Imaging to confirm clear lung fields without infiltrates, masses, or pleural effusions."

            }

        ],

        "treatments": [

            {

                "name": "Regular aerobic exercise",
                "type": "lifestyle",
                "description": "At least 150 minutes of moderate aerobic activity per week strengthens respiratory muscles and improves oxygen utilization efficiency."

            },

            {

                "name": "Breathing exercises",
                "type": "therapy",
                "description": "Diaphragmatic breathing and pursed-lip breathing techniques improve lung capacity and respiratory efficiency. Practice 10–15 minutes daily."

            },

            {

                "name": "Annual check-ups",
                "type": "lifestyle",
                "description": "Regular pulmonary function screenings, especially for those over 40 or with occupational exposure risks, help detect changes early."

            },

            {

                "name": "Hydration",
                "type": "lifestyle",
                "description": "Adequate fluid intake (2–3 liters daily) keeps the mucosal lining of airways thin, aiding in natural clearance of particles and pathogens."

            }

        ],

        "medications": [

            {

                "name": "Vitamin D supplement",
                "generic_name": "Cholecalciferol",
                "type": "Supplement",
                "description": "Supports immune function in the lungs. Deficiency is associated with increased respiratory infections and reduced lung function.",
                "usage": "1000–2000 IU daily, or as recommended by a healthcare provider based on blood levels.",
                "side_effects": ["Rare at recommended doses", "Hypercalcemia at very high doses", "Nausea"]

            },

            {

                "name": "Vitamin C",
                "generic_name": "Ascorbic acid",
                "type": "Antioxidant supplement",
                "description": "Powerful antioxidant that protects lung tissue from oxidative stress caused by environmental pollutants and free radicals.",
                "usage": "500–1000 mg daily through diet or supplementation.",
                "side_effects": ["GI upset at high doses", "Kidney stones (rare)", "Diarrhea"]

            },

            {

                "name": "Omega-3 fish oil",
                "generic_name": "EPA/DHA",
                "type": "Anti-inflammatory supplement",
                "description": "Reduces systemic inflammation and may protect against decline in lung function. Studies show benefits for airway inflammation.",
                "usage": "1000–2000 mg combined EPA/DHA daily with food.",
                "side_effects": ["Fishy aftertaste", "GI upset", "Increased bleeding risk with anticoagulants"]

            },

            {

                "name": "N-Acetylcysteine (NAC)",
                "generic_name": "N-Acetylcysteine",
                "type": "Mucolytic / Antioxidant",
                "description": "Acts as a mucolytic to thin mucus and as a precursor to glutathione, the body's primary antioxidant. Supports airway clearance.",
                "usage": "600 mg once or twice daily.",
                "side_effects": ["Nausea", "Vomiting", "Diarrhea", "Rash (rare)"]

            }

        ],

        "prevention": [

            {

                "tip": "Quit or avoid smoking",
                "description": "Tobacco smoke is the leading preventable cause of lung disease. Even secondhand smoke exposure damages airways. Quitting at any age improves lung health.",
                "icon": ""

            },

            {

                "tip": "Exercise regularly",
                "description": "Aim for at least 30 minutes of moderate exercise 5 days a week. Swimming, cycling, and brisk walking are excellent for lung conditioning.",
                "icon": ""

            },

            {

                "tip": "Monitor air quality",
                "description": "Check daily AQI (Air Quality Index) readings. Avoid outdoor exercise when AQI exceeds 100. Use HEPA air purifiers indoors during high pollution days.",
                "icon": ""

            },

            {

                "tip": "Practice good hygiene",

                "description": "Wash hands frequently, avoid close contact with sick individuals, and wear masks in crowded indoor spaces during respiratory illness seasons.",

                "icon": ""

            },

            {

                "tip": "Stay vaccinated",

                "description": "Annual influenza vaccination and pneumococcal vaccines (PCV15/PCV20 or PPSV23) significantly reduce risk of respiratory infections.",

                "icon": ""

            }

        ],

        "when_to_see_doctor": [

            "Persistent cough lasting more than 3 weeks",

            "Unexplained shortness of breath during normal activities",

            "Coughing up blood or blood-streaked mucus",

            "Recurring chest infections (more than 2 per year)",

            "Unexplained weight loss combined with breathing difficulties",

            "Wheezing or noisy breathing that develops suddenly"

        ],

        "statistics": {

            "prevalence": "~80% of adults maintain healthy lung function throughout life with proper care",

            "annual_deaths": "Chronic respiratory diseases account for ~4 million deaths globally per year",

            "age_group": "Lung function peaks at ages 20–25, then gradually declines ~1% per year after 35",

            "trend": "stable"

        },

        "references": [

            {

                "title": "The Lung Health of Adults",

                "source": "World Health Organization",

                "url": "https://www.who.int/health-topics/chronic-respiratory-diseases"

            },

            {

                "title": "How Lungs Work",

                "source": "National Heart, Lung, and Blood Institute (NHLBI)",

                "url": "https://www.nhlbi.nih.gov/health/lungs"

            },

            {

                "title": "Lung Health and Diseases",

                "source": "American Lung Association",

                "url": "https://www.lung.org/lung-health-diseases"

            }

        ]

    },

    "asthma": {

        "id": "asthma",

        "name": "Asthma",

        "icon": "",

        "color": "#F59E0B",

        "tagline": "Chronic airway inflammation",

        "key_stat": "262 million affected worldwide",

        "overview": (

            "Asthma is a chronic inflammatory disease of the airways characterized by "

            "variable and recurring symptoms of airflow obstruction and bronchospasm. "

            "The airways become swollen, narrow, and produce excess mucus, making breathing "

            "difficult. Symptoms include wheezing, coughing, chest tightness, and shortness "

            "of breath, which can range from mild to life-threatening.\n\n"

            "Asthma affects people of all ages but most often starts during childhood. In the "

            "United States alone, approximately 25 million people have asthma, including 5 million "

            "children. The exact cause is not fully understood, but it involves a combination of "

            "genetic predisposition and environmental factors. The immune system overreacts to "

            "certain triggers, causing inflammation and muscle constriction around the airways.\n\n"

            "While there is no cure for asthma, it can be effectively managed with proper medication, "

            "trigger avoidance, and an action plan. Most people with asthma can live active, normal "

            "lives with appropriate treatment. However, poorly controlled asthma can lead to permanent "

            "airway remodeling and fixed airflow limitation."

        ),

        "breath_sounds": (

            "Asthmatic breath sounds are characterized by high-pitched, musical wheezing, "

            "especially during expiration. During acute exacerbations, wheezing may be heard "

            "during both inspiration and expiration. In severe attacks, the chest may become "

            "'silent' due to severely restricted airflow — this is a medical emergency. "

            "Prolonged expiratory phase is common."

        ),

        "symptoms": [

            {

                "name": "Wheezing",

                "description": "A high-pitched whistling sound when breathing out, caused by air flowing through narrowed airways. Most common symptom of asthma and may worsen at night.",

                "icon": ""

            },

            {

                "name": "Shortness of breath",

                "description": "Difficulty breathing or feeling like you cannot get enough air into your lungs. May occur at rest or during physical activity. Often described as chest tightness.",

                "icon": ""

            },

            {

                "name": "Chest tightness",

                "description": "A feeling of pressure or constriction in the chest, as if a band is squeezing around the ribcage. Often worsens during exacerbations or exposure to triggers.",

                "icon": ""

            },

            {

                "name": "Chronic cough",

                "description": "Persistent cough, often worse at night or early morning. May be dry or productive. In some patients, cough is the only symptom (cough-variant asthma).",

                "icon": ""

            },

            {

                "name": "Nocturnal symptoms",

                "description": "Worsening of symptoms during the night, leading to sleep disruption. Caused by circadian changes in airway tone and increased mucus production.",

                "icon": ""

            },

            {

                "name": "Exercise-induced symptoms",

                "description": "Coughing, wheezing, or breathlessness during or shortly after physical exertion. Affects up to 90% of asthma patients and may be the only trigger in some.",

                "icon": ""

            },

            {

                "name": "Difficulty speaking",

                "description": "During moderate to severe attacks, patients may only be able to speak in short phrases or single words due to severe breathlessness.",

                "icon": ""

            }

        ],

        "causes_risk_factors": [

            {

                "name": "Allergens",

                "description": "Dust mites, pet dander, pollen, mold spores, and cockroach droppings can trigger allergic asthma, the most common form. About 60% of asthma cases are allergic.",

                "icon": ""

            },

            {

                "name": "Respiratory infections",

                "description": "Viral upper respiratory infections (common cold, flu, RSV) are the most common trigger for asthma exacerbations, especially in children.",

                "icon": ""

            },

            {

                "name": "Air pollution & irritants",

                "description": "Cigarette smoke, vehicle exhaust, industrial emissions, strong odors, and chemical fumes irritate and inflame airways, worsening asthma control.",

                "icon": ""

            },

            {

                "name": "Exercise",

                "description": "Physical activity, especially in cold, dry air, triggers exercise-induced bronchoconstriction in up to 90% of asthmatics due to airway cooling and drying.",

                "icon": ""

            },

            {

                "name": "Weather changes",

                "description": "Cold air, sudden temperature changes, high humidity, and thunderstorms can trigger asthma attacks. Cold air causes airway constriction.",

                "icon": ""

            },

            {

                "name": "Genetic predisposition",

                "description": "Asthma runs in families. Having a parent with asthma increases the risk by 3–6 times. Multiple genes related to immune response and airway reactivity are involved.",

                "icon": ""

            },

            {

                "name": "Stress and strong emotions",

                "description": "Anxiety, stress, laughter, or crying can trigger hyperventilation and bronchospasm. Stress also worsens inflammatory responses in the airways.",

                "icon": ""

            }

        ],

        "stages": [

            {

                "name": "Intermittent asthma",

                "description": "Symptoms ≤2 days/week, nighttime awakenings ≤2x/month, SABA use ≤2 days/week, no interference with normal activity. FEV1 ≥80% predicted. Normal PEF between exacerbations.",

                "severity": "mild"

            },

            {

                "name": "Mild persistent asthma",

                "description": "Symptoms >2 days/week but not daily, nighttime awakenings 3–4x/month, SABA use >2 days/week. Minor limitation with normal activity. FEV1 ≥80% predicted.",

                "severity": "moderate"

            },

            {

                "name": "Moderate persistent asthma",

                "description": "Daily symptoms, nighttime awakenings >1x/week but not nightly, daily SABA use. Some limitation with normal activity. FEV1 60–80% predicted.",

                "severity": "severe"

            },

            {

                "name": "Severe persistent asthma",

                "description": "Symptoms throughout the day, frequent nighttime awakenings (often 7x/week), SABA use several times daily. Extremely limited activity. FEV1 <60% predicted. Requires multiple controller medications.",

                "severity": "critical"

            }

        ],

        "diagnosis": [

            {

                "method": "Spirometry",

                "description": "The gold standard test. Measures FEV1 (forced expiratory volume in 1 second) and FVC (forced vital capacity). A reduced FEV1/FVC ratio (<0.70) with ≥12% improvement after bronchodilator confirms reversible obstruction."

            },

            {

                "method": "Peak expiratory flow (PEF)",

                "description": "Portable measurement of maximum exhalation speed. Daily PEF monitoring helps track asthma control. Variability >20% suggests poorly controlled asthma."

            },

            {

                "method": "Methacholine challenge test",

                "description": "Bronchoprovocation test where inhaled methacholine causes airway narrowing. A positive test (≥20% drop in FEV1 at low doses) indicates airway hyperresponsiveness."

            },

            {

                "method": "Fractional exhaled nitric oxide (FeNO)",

                "description": "Measures nitric oxide in exhaled breath, a marker of eosinophilic airway inflammation. Levels >50 ppb in adults suggest allergic/eosinophilic asthma responsive to corticosteroids."

            },

            {

                "method": "Allergy testing",

                "description": "Skin prick tests or specific IgE blood tests identify allergen triggers. Helps guide allergen avoidance strategies and immunotherapy decisions."

            },

            {

                "method": "Chest X-ray",

                "description": "Usually normal in asthma but used to rule out other conditions (pneumonia, foreign body, heart failure). May show hyperinflation during acute exacerbation."

            }

        ],

        "treatments": [

            {

                "name": "Quick-relief inhalers (rescue)",

                "type": "medication",

                "description": "Short-acting beta-agonists (SABAs) like albuterol provide rapid bronchodilation within 5–15 minutes. Used as-needed for acute symptoms. Overuse (>2 days/week) indicates poor control."

            },

            {

                "name": "Inhaled corticosteroids (ICS)",

                "type": "medication",

                "description": "The most effective long-term controller therapy. Reduces airway inflammation, prevents exacerbations, and prevents airway remodeling. Daily use regardless of symptoms."

            },

            {

                "name": "Combination inhalers (ICS/LABA)",

                "type": "medication",

                "description": "Combines an inhaled corticosteroid with a long-acting beta-agonist for both anti-inflammatory and bronchodilator effects. Used for moderate-to-severe persistent asthma."

            },

            {

                "name": "Biologic therapies",

                "type": "medication",

                "description": "Targeted antibody treatments (anti-IgE, anti-IL5, anti-IL4/13) for severe asthma uncontrolled by standard therapy. Given as injection every 2–8 weeks."

            },

            {

                "name": "Allergen immunotherapy",

                "type": "therapy",

                "description": "Gradual exposure to increasing doses of identified allergens to build tolerance. Available as subcutaneous injections (SCIT) or sublingual tablets (SLIT)."

            },

            {

                "name": "Bronchial thermoplasty",

                "type": "surgical",

                "description": "Procedure that delivers controlled thermal energy to airway walls, reducing smooth muscle mass and decreasing bronchoconstriction. Reserved for severe refractory asthma."

            }

        ],

        "medications": [

            {

                "name": "ProAir / Ventolin",

                "generic_name": "Albuterol (Salbutamol)",

                "type": "Short-acting beta-agonist (SABA)",

                "description": "Rapid-acting bronchodilator that relaxes airway smooth muscle within minutes. The most commonly prescribed rescue inhaler worldwide.",

                "usage": "2 puffs every 4–6 hours as needed for acute symptoms. Use a spacer for better delivery.",

                "side_effects": ["Tremor", "Increased heart rate", "Nervousness", "Headache", "Throat irritation"]

            },

            {

                "name": "Flovent / Flixotide",

                "generic_name": "Fluticasone propionate",

                "type": "Inhaled corticosteroid (ICS)",

                "description": "Potent anti-inflammatory that reduces airway swelling, mucus production, and hyperreactivity. Cornerstone of asthma controller therapy.",

                "usage": "1–2 puffs twice daily. Rinse mouth after use to prevent oral thrush.",

                "side_effects": ["Oral thrush (candidiasis)", "Hoarseness", "Sore throat", "Cough", "Bruising (high doses)"]

            },

            {

                "name": "Singulair",

                "generic_name": "Montelukast",

                "type": "Leukotriene receptor antagonist (LTRA)",

                "description": "Oral medication that blocks leukotrienes — inflammatory chemicals released during allergic reactions. Effective for allergic asthma and exercise-induced bronchoconstriction.",

                "usage": "10 mg tablet once daily in the evening (adults). Available as chewable tablets for children.",

                "side_effects": ["Headache", "Upper respiratory infection", "Abdominal pain", "Neuropsychiatric effects (rare — mood changes, sleep disturbances)"]

            },

            {

                "name": "Symbicort",

                "generic_name": "Budesonide/Formoterol",

                "type": "Combination ICS/LABA",

                "description": "Dual-action inhaler combining anti-inflammatory corticosteroid with long-acting bronchodilator. Can be used as both maintenance therapy and reliever (MART approach).",

                "usage": "1–2 puffs twice daily for maintenance. Can also be used as needed for relief (per physician guidance).",

                "side_effects": ["Oral thrush", "Headache", "Tremor", "Palpitations", "Throat irritation"]

            },

            {

                "name": "Xolair",

                "generic_name": "Omalizumab",

                "type": "Anti-IgE biologic",

                "description": "Monoclonal antibody that binds free IgE, preventing it from triggering allergic cascades. For moderate-to-severe allergic asthma not controlled by ICS.",

                "usage": "Subcutaneous injection every 2–4 weeks. Dose based on serum IgE levels and body weight.",

                "side_effects": ["Injection site reactions", "Headache", "Anaphylaxis risk (rare, observe 2 hrs after first doses)", "Joint pain"]

            },

            {

                "name": "Atrovent",

                "generic_name": "Ipratropium bromide",

                "type": "Short-acting anticholinergic",

                "description": "Blocks acetylcholine-mediated bronchoconstriction. Often used as add-on to SABA in acute exacerbations for additive bronchodilation, especially in emergency settings.",

                "usage": "2 puffs 4 times daily, or via nebulizer (0.5 mg) combined with albuterol during acute attacks.",

                "side_effects": ["Dry mouth", "Cough", "Headache", "Blurred vision (if sprayed in eyes)", "Urinary retention (rare)"]

            }

        ],

        "prevention": [

            {

                "tip": "Identify and avoid triggers",

                "description": "Keep a symptom diary to identify personal triggers. Common ones include dust mites, pet dander, pollen, mold, smoke, and strong odors. Minimize exposure systematically.",

                "icon": ""

            },

            {

                "tip": "Follow your asthma action plan",

                "description": "Work with your doctor to create a written plan with green/yellow/red zones based on symptoms and peak flow readings. Know when to adjust medications and when to seek emergency care.",

                "icon": ""

            },

            {

                "tip": "Use controller medications daily",

                "description": "Take prescribed inhaled corticosteroids every day, even when feeling well. Stopping controller medications is the most common cause of asthma flare-ups.",

                "icon": ""

            },

            {

                "tip": "Monitor air quality",

                "description": "Check daily Air Quality Index (AQI) via apps or weather services. Stay indoors with windows closed on high pollution or high pollen days.",

                "icon": ""

            },

            {

                "tip": "Allergen-proof your home",

                "description": "Use dust mite covers on pillows/mattresses, wash bedding weekly in hot water, use HEPA filters, keep humidity below 50%, and remove carpets from bedrooms.",

                "icon": ""

            },

            {

                "tip": "Get vaccinated",

                "description": "Annual influenza and COVID-19 vaccines are strongly recommended as respiratory infections are the most common trigger for severe asthma exacerbations.",

                "icon": ""

            }

        ],

        "when_to_see_doctor": [

            "Quick-relief inhaler is needed more than twice a week",

            "Symptoms wake you up at night more than twice a month",

            "Difficulty performing daily activities due to breathing problems",

            "Peak flow readings consistently below 80% of personal best",

            "Symptoms do not improve after using rescue inhaler",

            "Severe attack: inability to speak in full sentences, blue lips or fingernails, extreme difficulty breathing — CALL EMERGENCY SERVICES"

        ],

        "statistics": {

            "prevalence": "~262 million people affected worldwide (WHO, 2021)",

            "annual_deaths": "~455,000 deaths per year globally",

            "age_group": "Can develop at any age; ~80% of cases develop before age 6. Adult-onset asthma is more common in women.",

            "trend": "increasing"

        },

        "references": [

            {

                "title": "Asthma Fact Sheet",

                "source": "World Health Organization",

                "url": "https://www.who.int/news-room/fact-sheets/detail/asthma"

            },

            {

                "title": "Guidelines for the Diagnosis and Management of Asthma (EPR-3)",

                "source": "National Heart, Lung, and Blood Institute (NHLBI)",

                "url": "https://www.nhlbi.nih.gov/health-topics/asthma"

            },

            {

                "title": "Global Strategy for Asthma Management and Prevention (GINA 2023)",

                "source": "Global Initiative for Asthma",

                "url": "https://ginasthma.org/gina-reports/"

            },

            {

                "title": "Asthma - Symptoms and Causes",

                "source": "Mayo Clinic",

                "url": "https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653"

            }

        ]

    },

    "copd": {

        "id": "copd",

        "name": "COPD",

        "icon": "",

        "color": "#EF4444",

        "tagline": "Chronic obstructive pulmonary disease",

        "key_stat": "3rd leading cause of death globally",

        "overview": (

            "Chronic Obstructive Pulmonary Disease (COPD) is a group of progressive lung diseases "

            "that cause obstructed airflow from the lungs. It includes emphysema (destruction of "

            "the alveoli) and chronic bronchitis (long-term inflammation of the bronchial tubes with "

            "excess mucus production). COPD makes breathing increasingly difficult over time, and the "

            "damage to the lungs is largely irreversible.\n\n"

            "Approximately 380 million people worldwide are affected by COPD, and it is the third "

            "leading cause of death globally, responsible for over 3.23 million deaths annually. "

            "Cigarette smoking is the primary cause in developed countries, accounting for 80–90% of "

            "cases. However, significant numbers of COPD cases in developing countries are caused by "

            "exposure to biomass fuel smoke used for cooking and heating in poorly ventilated homes.\n\n"

            "COPD develops slowly over many years, and most people are at least 40 years old when "

            "symptoms begin. While there is no cure, treatments can slow disease progression, relieve "

            "symptoms, reduce exacerbation frequency, and improve quality of life. Early diagnosis "

            "through spirometry is crucial, as significant lung function can be lost before noticeable "

            "symptoms appear."

        ),

        "breath_sounds": (

            "COPD breath sounds include diminished vesicular sounds (due to air trapping and hyperinflation), "

            "coarse crackles (from mucus in larger airways, especially in chronic bronchitis), expiratory "

            "wheezing (from narrowed airways), and prolonged expiratory phase. In emphysema, breath sounds "

            "are notably distant and quiet due to loss of lung tissue and air trapping."

        ),

        "symptoms": [

            {

                "name": "Chronic cough",

                "description": "Persistent cough that lasts for months or years, often dismissed as 'smoker's cough.' May be productive (with sputum) or dry. Usually the first symptom to appear.",

                "icon": ""

            },

            {

                "name": "Sputum production",

                "description": "Excessive mucus (phlegm) production, particularly in the morning. Sputum may be clear, white, yellow, or green. Increased or discolored sputum can signal an exacerbation.",

                "icon": ""

            },

            {

                "name": "Progressive dyspnea",

                "description": "Shortness of breath that gradually worsens over years. Initially occurs only with exertion, but in advanced stages affects even basic activities like dressing or eating.",

                "icon": ""

            },

            {

                "name": "Wheezing",

                "description": "Whistling or squeaky sound during breathing, caused by narrowed or inflamed airways. More prominent during exacerbations and physical activity.",

                "icon": ""

            },

            {

                "name": "Chest tightness",

                "description": "A sensation of constriction or heaviness in the chest, worsening with activity. Caused by hyperinflation of the lungs trapping air.",

                "icon": ""

            },

            {

                "name": "Fatigue",

                "description": "Persistent tiredness and low energy due to the extra effort required for breathing and reduced oxygen delivery to muscles. Affects daily functioning significantly.",

                "icon": ""

            },

            {

                "name": "Frequent respiratory infections",

                "description": "Increased susceptibility to colds, flu, and pneumonia due to impaired airway defense mechanisms. Each infection can cause further permanent lung damage.",

                "icon": ""

            },

            {

                "name": "Unintended weight loss",

                "description": "In advanced COPD, the body burns significantly more calories for breathing (up to 10x normal). Combined with reduced appetite, this leads to muscle wasting (cachexia).",

                "icon": ""

            }

        ],

        "causes_risk_factors": [

            {

                "name": "Cigarette smoking",

                "description": "The primary cause of COPD, responsible for 80–90% of cases. Risk increases with pack-years (packs/day × years smoked). Even passive/secondhand smoke exposure increases risk.",

                "icon": ""

            },

            {

                "name": "Occupational exposures",

                "description": "Long-term exposure to dust, chemicals, fumes, and gases in the workplace (mining, construction, textile, farming) accounts for ~15% of COPD cases.",

                "icon": ""

            },

            {

                "name": "Biomass fuel smoke",

                "description": "Burning wood, charcoal, crop residues, or animal dung for cooking/heating in poorly ventilated homes is a leading cause of COPD in developing countries, especially among women.",

                "icon": ""

            },

            {

                "name": "Alpha-1 antitrypsin deficiency",

                "description": "Rare genetic condition (affects ~1 in 3,000 people) causing lack of a protective lung protein. Can cause early-onset COPD, even in non-smokers. Testable via blood test.",

                "icon": ""

            },

            {

                "name": "Air pollution",

                "description": "Chronic exposure to outdoor air pollution (particulate matter PM2.5, ozone, nitrogen dioxide) is an independent risk factor. Urban populations have higher COPD rates.",

                "icon": ""

            },

            {

                "name": "Childhood respiratory infections",

                "description": "Severe lower respiratory infections during childhood (especially before age 5) can impair lung development and increase COPD risk later in life.",

                "icon": ""

            }

        ],

        "stages": [

            {

                "name": "GOLD Stage I — Mild",

                "description": "FEV1 ≥80% predicted. Mild airflow limitation. Patient may not be aware of reduced lung function. Chronic cough and sputum production may be present.",

                "severity": "mild"

            },

            {

                "name": "GOLD Stage II — Moderate",

                "description": "FEV1 50–79% predicted. Worsening airflow limitation. Shortness of breath typically develops, especially during exertion. Most patients seek medical attention at this stage.",

                "severity": "moderate"

            },

            {

                "name": "GOLD Stage III — Severe",

                "description": "FEV1 30–49% predicted. Significant airflow limitation. Increased breathlessness, reduced exercise capacity, repeated exacerbations impacting quality of life. Fatigue and functional limitation.",

                "severity": "severe"

            },

            {

                "name": "GOLD Stage IV — Very Severe",

                "description": "FEV1 <30% predicted, or <50% with chronic respiratory failure. Life-threatening exacerbations. Severely impaired quality of life. May require long-term oxygen therapy or lung transplant consideration.",

                "severity": "critical"

            }

        ],

        "diagnosis": [

            {

                "method": "Spirometry",

                "description": "Essential for diagnosis. A post-bronchodilator FEV1/FVC ratio <0.70 confirms persistent airflow limitation. Unlike asthma, obstruction in COPD is not fully reversible."

            },

            {

                "method": "Chest X-ray",

                "description": "May show hyperinflation, flattened diaphragm, and increased lung transparency (emphysema). Useful to rule out other conditions like lung cancer, heart failure, and pneumonia."

            },

            {

                "method": "CT scan (HRCT)",

                "description": "High-resolution CT provides detailed images showing emphysema distribution, bronchial wall thickening, and air trapping. Important for surgical planning (LVRS, transplant evaluation)."

            },

            {

                "method": "Arterial blood gas (ABG)",

                "description": "Measures oxygen and carbon dioxide levels in arterial blood. Assesses severity of gas exchange impairment. Important in advanced COPD for determining need for oxygen therapy."

            },

            {

                "method": "Alpha-1 antitrypsin testing",

                "description": "Blood test recommended for all COPD patients, especially those diagnosed under age 45, non-smokers, or with a family history. Identifies the genetic form of COPD."

            },

            {

                "method": "6-minute walk test",

                "description": "Measures the distance walked in 6 minutes on a flat surface. Assesses functional exercise capacity and helps monitor disease progression and response to treatment."

            }

        ],

        "treatments": [

            {

                "name": "Bronchodilators",

                "type": "medication",

                "description": "Mainstay of COPD treatment. Relax airway smooth muscle to improve airflow. Available as short-acting (SABA, SAMA) for quick relief and long-acting (LABA, LAMA) for maintenance."

            },

            {

                "name": "Inhaled corticosteroids",

                "type": "medication",

                "description": "Added for patients with frequent exacerbations (≥2/year) despite dual bronchodilator therapy. Reduce eosinophilic inflammation but increase pneumonia risk."

            },

            {

                "name": "Pulmonary rehabilitation",

                "type": "therapy",

                "description": "Structured program of exercise training, education, and behavior change. Proven to reduce dyspnea, improve exercise tolerance, and decrease hospitalizations. 6–12 week programs."

            },

            {

                "name": "Long-term oxygen therapy",

                "type": "therapy",

                "description": "For patients with chronic hypoxemia (PaO2 ≤55 mmHg or SpO2 ≤88%). Used ≥15 hours/day, improves survival and quality of life. Requires regular pulse oximetry monitoring."

            },

            {

                "name": "Smoking cessation",

                "type": "lifestyle",

                "description": "The single most effective intervention to slow disease progression at any stage. Combining behavioral counseling with pharmacotherapy (NRT, varenicline, bupropion) doubles quit rates."

            },

            {

                "name": "Lung volume reduction surgery (LVRS)",

                "type": "surgical",

                "description": "Removes damaged, hyperinflated portions of the lung to allow remaining lung tissue to function better. Suitable for upper-lobe predominant emphysema with poor exercise capacity."

            }

        ],

        "medications": [

            {

                "name": "Spiriva",

                "generic_name": "Tiotropium bromide",

                "type": "Long-acting anticholinergic (LAMA)",

                "description": "Long-acting muscarinic antagonist providing 24-hour bronchodilation. Reduces air trapping and hyperinflation. The most widely prescribed LAMA for COPD worldwide.",

                "usage": "One capsule (18 mcg) inhaled once daily via HandiHaler device, or 2 puffs (2.5 mcg each) via Respimat inhaler.",

                "side_effects": ["Dry mouth", "Constipation", "Urinary retention", "Blurred vision", "Increased heart rate (rare)"]

            },

            {

                "name": "Serevent",

                "generic_name": "Salmeterol",

                "type": "Long-acting beta-agonist (LABA)",

                "description": "Provides sustained bronchodilation for 12 hours by relaxing airway smooth muscle. Often combined with an inhaled corticosteroid. Not for acute rescue.",

                "usage": "One puff (50 mcg) twice daily via dry powder inhaler. Take doses 12 hours apart.",

                "side_effects": ["Tremor", "Headache", "Palpitations", "Muscle cramps", "Throat irritation"]

            },

            {

                "name": "Daliresp",

                "generic_name": "Roflumilast",

                "type": "PDE4 inhibitor",

                "description": "Oral anti-inflammatory that reduces exacerbations in severe COPD with chronic bronchitis phenotype and history of frequent exacerbations. Targets intracellular inflammation.",

                "usage": "500 mcg tablet once daily. May take 4–8 weeks for full benefit. Take with food to reduce GI side effects.",

                "side_effects": ["Diarrhea", "Nausea", "Weight loss", "Headache", "Insomnia", "Depression/mood changes"]

            },

            {

                "name": "Advair",

                "generic_name": "Fluticasone/Salmeterol",

                "type": "Combination ICS/LABA",

                "description": "Combines anti-inflammatory corticosteroid with long-acting bronchodilator. For COPD patients with frequent exacerbations despite long-acting bronchodilator monotherapy.",

                "usage": "One inhalation (250/50 mcg) twice daily. Rinse mouth after each use.",

                "side_effects": ["Oral thrush", "Hoarseness", "Increased pneumonia risk", "Bone density reduction (long-term)", "Bruising"]

            },

            {

                "name": "Theo-Dur",

                "generic_name": "Theophylline",

                "type": "Methylxanthine bronchodilator",

                "description": "Oral bronchodilator with modest anti-inflammatory effects. Used as add-on therapy when inhaled medications are insufficient. Requires blood level monitoring due to narrow therapeutic window.",

                "usage": "200–400 mg twice daily (sustained-release). Target serum level: 5–12 mcg/mL. Avoid caffeine.",

                "side_effects": ["Nausea", "Insomnia", "Tachycardia", "Seizures (at toxic levels)", "Tremor", "Drug interactions (many)"]

            },

            {

                "name": "Zithromax",

                "generic_name": "Azithromycin",

                "type": "Macrolide antibiotic (prophylactic)",

                "description": "Low-dose chronic macrolide therapy reduces exacerbation frequency by ~25% through anti-inflammatory and immunomodulatory effects (beyond its antibiotic properties).",

                "usage": "250 mg once daily or 500 mg three times per week for exacerbation prevention. Requires baseline ECG and hearing assessment.",

                "side_effects": ["Hearing impairment", "QT prolongation", "Diarrhea", "Antibiotic resistance development", "Nausea"]

            }

        ],

        "prevention": [

            {

                "tip": "Quit smoking immediately",

                "description": "Smoking cessation is the single most important step. Lung function decline slows to near-normal rate after quitting. Seek help through quitlines (1-800-QUIT-NOW), counseling, and medications.",

                "icon": ""

            },

            {

                "tip": "Avoid secondhand smoke",

                "description": "Even passive exposure accelerates lung damage. Make your home and car smoke-free zones. Support smoke-free workplace policies.",

                "icon": ""

            },

            {

                "tip": "Use occupational protection",

                "description": "Wear appropriate respiratory protection (N95 masks, respirators) when exposed to dust, chemicals, or fumes at work. Ensure proper workplace ventilation.",

                "icon": ""

            },

            {

                "tip": "Get vaccinated",

                "description": "Annual influenza vaccine reduces severe exacerbations by ~50%. Pneumococcal vaccines (PCV20 or PCV15 + PPSV23) prevent bacterial pneumonia complications.",

                "icon": ""

            },

            {

                "tip": "Exercise regularly",

                "description": "Even moderate exercise (walking 30 min/day) improves cardiovascular fitness, reduces dyspnea, and slows functional decline. Pulmonary rehabilitation programs are highly recommended.",

                "icon": ""

            },

            {

                "tip": "Reduce indoor air pollution",

                "description": "Use clean cooking fuels, ensure proper ventilation, avoid burning biomass indoors, and use exhaust fans. This is especially critical in developing countries.",

                "icon": ""

            }

        ],

        "when_to_see_doctor": [

            "Persistent cough that doesn't go away after 3 weeks",

            "Increasing breathlessness, especially if you are or were a smoker",

            "Coughing up more mucus than usual or a change in mucus color",

            "Swollen ankles, feet, or legs (sign of right heart failure/cor pulmonale)",

            "Unexplained weight loss or muscle wasting",

            "Blue or grey discoloration of lips or fingernails (cyanosis) — EMERGENCY",

            "Rapid worsening of breathlessness that doesn't respond to inhalers — CALL EMERGENCY SERVICES"

        ],

        "statistics": {

            "prevalence": "~380 million people affected globally (Lancet, 2022)",

            "annual_deaths": "~3.23 million deaths per year — 3rd leading cause of death worldwide (WHO, 2023)",

            "age_group": "Most commonly diagnosed after age 40. Risk increases significantly with age and cumulative smoke/pollution exposure.",

            "trend": "increasing"

        },

        "references": [

            {

                "title": "Chronic Obstructive Pulmonary Disease (COPD) Fact Sheet",

                "source": "World Health Organization",

                "url": "https://www.who.int/news-room/fact-sheets/detail/chronic-obstructive-pulmonary-disease-(copd)"

            },

            {

                "title": "Global Strategy for Diagnosis, Management, and Prevention of COPD (GOLD 2024)",

                "source": "Global Initiative for Chronic Obstructive Lung Disease",

                "url": "https://goldcopd.org/gold-reports/"

            },

            {

                "title": "COPD - Learn More, Breathe Better",

                "source": "National Heart, Lung, and Blood Institute (NHLBI)",

                "url": "https://www.nhlbi.nih.gov/health/copd"

            },

            {

                "title": "COPD: Causes, Symptoms, Diagnosis, Treatment",

                "source": "Mayo Clinic",

                "url": "https://www.mayoclinic.org/diseases-conditions/copd/symptoms-causes/syc-20353679"

            }

        ]

    },

    "pneumonia": {

        "id": "pneumonia",

        "name": "Pneumonia",

        "icon": "",

        "color": "#8B5CF6",

        "tagline": "Lung infection with inflammation",

        "key_stat": "2.5 million deaths per year globally",

        "overview": (

            "Pneumonia is an infection that inflames the air sacs (alveoli) in one or both lungs. "

            "The alveoli may fill with fluid or pus, causing cough with phlegm, fever, chills, and "

            "difficulty breathing. A variety of organisms can cause pneumonia, including bacteria, "

            "viruses, and fungi. The severity ranges from mild ('walking pneumonia') to life-threatening, "

            "particularly in infants, young children, the elderly, and immunocompromised individuals.\n\n"

            "Pneumonia is the leading infectious cause of death in children worldwide, killing more "

            "than 700,000 children under age 5 every year. In adults, community-acquired pneumonia "

            "(CAP) is the most common type, with Streptococcus pneumoniae being the most frequent "

            "bacterial cause. Hospital-acquired pneumonia (HAP) and ventilator-associated pneumonia "

            "(VAP) are significant concerns in healthcare settings.\n\n"

            "Diagnosis typically involves chest X-ray and blood tests. Treatment depends on the cause "

            "and severity — bacterial pneumonia is treated with antibiotics, while viral pneumonia may "

            "require antivirals or supportive care. Vaccines (pneumococcal and influenza) are effective "

            "preventive measures. Most healthy individuals recover within 1–3 weeks, but recovery can "

            "take months for severe cases."

        ),

        "breath_sounds": (

            "Pneumonia produces characteristic auscultatory findings including fine crackles (rales) — "

            "short, crackling sounds heard during inspiration as air opens fluid-filled alveoli. "

            "Bronchial breath sounds may be heard over consolidated areas (where they should normally be "

            "vesicular). Egophony ('E-to-A' changes), dullness to percussion, and increased tactile "

            "fremitus are classic signs of lung consolidation."

        ),

        "symptoms": [

            {

                "name": "Productive cough",

                "description": "Cough producing phlegm (sputum) that may be yellow, green, rust-colored, or blood-tinged. Rust-colored sputum is classic for pneumococcal pneumonia.",

                "icon": ""

            },

            {

                "name": "High fever with chills",

                "description": "Temperature often exceeds 38.5°C (101.3°F) with rigors (shaking chills). Bacterial pneumonia typically causes higher fevers than viral. Elderly patients may not mount a fever.",

                "icon": ""

            },

            {

                "name": "Difficulty breathing",

                "description": "Shortness of breath at rest or with minimal exertion due to reduced lung capacity from fluid-filled alveoli. May progress to respiratory distress in severe cases.",

                "icon": ""

            },

            {

                "name": "Sharp chest pain",

                "description": "Pleuritic chest pain — sharp, stabbing pain that worsens with deep breaths or coughing. Caused by inflammation of the pleura (lining of the lungs).",

                "icon": ""

            },

            {

                "name": "Fatigue and malaise",

                "description": "Profound tiredness, weakness, and general feeling of illness. The body diverts energy to fight infection. Recovery fatigue can persist for weeks after the infection clears.",

                "icon": ""

            },

            {

                "name": "Sweating and clammy skin",

                "description": "Profuse sweating, especially at night, as the body fights infection. Skin may feel cool and clammy despite having a fever.",

                "icon": ""

            },

            {

                "name": "Confusion (in elderly)",

                "description": "Sudden confusion, delirium, or altered mental status may be the primary or only symptom in adults over 65. An important atypical presentation to watch for.",

                "icon": ""

            },

            {

                "name": "Nausea, vomiting, or diarrhea",

                "description": "Gastrointestinal symptoms can accompany pneumonia, particularly in children and when caused by certain organisms like Legionella or Mycoplasma.",

                "icon": ""

            }

        ],

        "causes_risk_factors": [

            {

                "name": "Bacterial infection",

                "description": "Streptococcus pneumoniae is the most common cause of community-acquired pneumonia. Other bacteria include Haemophilus influenzae, Staphylococcus aureus, and Legionella.",

                "icon": ""

            },

            {

                "name": "Viral infection",

                "description": "Influenza, RSV (respiratory syncytial virus), SARS-CoV-2 (COVID-19), and rhinoviruses can cause viral pneumonia. Often milder but can be severe in vulnerable populations.",

                "icon": ""

            },

            {

                "name": "Weakened immune system",

                "description": "HIV/AIDS, organ transplant recipients, chemotherapy patients, and those on immunosuppressive drugs are at significantly higher risk of developing pneumonia and its complications.",

                "icon": ""

            },

            {

                "name": "Age extremes",

                "description": "Children under 2 years (immature immune system) and adults over 65 (declining immune function) are at highest risk. Pneumonia is the leading killer of children under 5 globally.",

                "icon": ""

            },

            {

                "name": "Chronic diseases",

                "description": "COPD, asthma, heart disease, diabetes, and kidney disease increase pneumonia risk. Chronic lung diseases impair airway defense mechanisms.",

                "icon": ""

            },

            {

                "name": "Smoking",

                "description": "Damages the lung's natural defense mechanisms (cilia, macrophages) and increases susceptibility to respiratory infections. Smokers have 2–4x higher pneumonia risk.",

                "icon": ""

            },

            {

                "name": "Hospitalization",

                "description": "Hospital-acquired pneumonia (HAP) develops ≥48 hours after admission. Ventilator-associated pneumonia (VAP) occurs in mechanically ventilated patients. These are often caused by drug-resistant organisms.",

                "icon": ""

            }

        ],

        "stages": [

            {

                "name": "Walking pneumonia (mild)",

                "description": "Mild form often caused by Mycoplasma pneumoniae. Patient may not feel sick enough to stay home. Symptoms include mild cough, low fever, and fatigue. Usually resolves with oral antibiotics.",

                "severity": "mild"

            },

            {

                "name": "Moderate pneumonia",

                "description": "Significant symptoms requiring medical attention: productive cough, fever >38.5°C, pleuritic chest pain, and mild hypoxia (SpO2 91–94%). Usually managed with oral antibiotics at home with close follow-up.",

                "severity": "moderate"

            },

            {

                "name": "Severe pneumonia",

                "description": "Requires hospitalization. Criteria include: respiratory rate ≥30/min, SpO2 ≤90%, multilobar infiltrates, confusion, hypotension. IV antibiotics, oxygen therapy, and close monitoring required.",

                "severity": "severe"

            },

            {

                "name": "Critical / ARDS",

                "description": "Progresses to sepsis, acute respiratory distress syndrome (ARDS), or respiratory failure requiring ICU admission and mechanical ventilation. Mortality rate 20–50%. Multi-organ dysfunction possible.",

                "severity": "critical"

            }

        ],

        "diagnosis": [

            {

                "method": "Chest X-ray",

                "description": "Primary diagnostic tool showing infiltrates, consolidation, or air bronchograms. Confirms pneumonia diagnosis and identifies affected lung regions. Bilateral involvement suggests atypical or viral cause."

            },

            {

                "method": "Blood tests",

                "description": "Complete blood count (CBC) shows elevated white blood cells. C-reactive protein (CRP) and procalcitonin levels help distinguish bacterial from viral causes and monitor treatment response."

            },

            {

                "method": "Sputum culture and Gram stain",

                "description": "Identifies the causative organism and its antibiotic sensitivity. Most useful when obtained before antibiotics are started. Helps guide targeted antibiotic therapy."

            },

            {

                "method": "Pulse oximetry",

                "description": "Non-invasive measurement of blood oxygen saturation. SpO2 <94% indicates significant hypoxia requiring supplemental oxygen. Critical for triage and severity assessment."

            },

            {

                "method": "CT scan",

                "description": "More sensitive than chest X-ray for detecting early or subtle pneumonia, cavitation, empyema, or complications. Used when X-ray findings are inconclusive or patient isn't responding to treatment."

            },

            {

                "method": "Blood cultures",

                "description": "Identifies bacteria in the bloodstream (bacteremia), which occurs in ~10% of hospitalized pneumonia patients. Positive blood cultures indicate severe infection and guide IV antibiotic selection."

            }

        ],

        "treatments": [

            {

                "name": "Antibiotics",

                "type": "medication",

                "description": "Mainstay treatment for bacterial pneumonia. Empiric therapy started immediately, then narrowed based on culture results. Outpatient: oral macrolide or doxycycline. Inpatient: IV beta-lactam + macrolide."

            },

            {

                "name": "Antivirals",

                "type": "medication",

                "description": "For viral pneumonia: oseltamivir (influenza), remdesivir (COVID-19). Most effective when started within 48 hours of symptom onset. Supportive care is primary for most viral pneumonias."

            },

            {

                "name": "Oxygen therapy",

                "type": "therapy",

                "description": "Supplemental oxygen via nasal cannula, face mask, or high-flow nasal cannula to maintain SpO2 ≥94%. Critical for severe pneumonia. May require non-invasive or mechanical ventilation."

            },

            {

                "name": "Supportive care",

                "type": "therapy",

                "description": "Rest, adequate fluid intake (2–3L/day), fever management with acetaminophen/ibuprofen, and adequate nutrition. Chest physiotherapy and postural drainage may help clear secretions."

            },

            {

                "name": "Vaccination (prevention)",

                "type": "lifestyle",

                "description": "Pneumococcal vaccines (PCV15/PCV20) and annual influenza vaccination are the most effective preventive measures. COVID-19 vaccination also reduces viral pneumonia risk."

            },

            {

                "name": "Mechanical ventilation",

                "type": "surgical",

                "description": "For critical cases with respiratory failure (ARDS). Invasive ventilation via endotracheal tube in ICU. Low tidal volume ventilation strategy (6 mL/kg) reduces mortality in ARDS."

            }

        ],

        "medications": [

            {

                "name": "Amoxil",

                "generic_name": "Amoxicillin",

                "type": "Penicillin antibiotic",

                "description": "First-line treatment for mild-to-moderate community-acquired pneumonia in many guidelines. Effective against Streptococcus pneumoniae, the most common bacterial cause.",

                "usage": "500 mg–1 g three times daily for 5–7 days (adults). Take with or without food.",

                "side_effects": ["Diarrhea", "Nausea", "Rash", "Allergic reaction (penicillin allergy)", "Yeast infection"]

            },

            {

                "name": "Zithromax",

                "generic_name": "Azithromycin",

                "type": "Macrolide antibiotic",

                "description": "Covers both typical and atypical organisms (Mycoplasma, Chlamydophila, Legionella). Preferred for outpatient treatment of CAP in patients without comorbidities.",

                "usage": "500 mg on day 1, then 250 mg daily on days 2–5 (Z-pack). Take on empty stomach or with food.",

                "side_effects": ["Diarrhea", "Nausea", "Abdominal pain", "QT prolongation (cardiac risk)", "Hearing changes (rare)"]

            },

            {

                "name": "Levaquin",

                "generic_name": "Levofloxacin",

                "type": "Respiratory fluoroquinolone",

                "description": "Broad-spectrum antibiotic covering both typical and atypical pneumonia organisms. Reserved for patients with comorbidities, recent antibiotic use, or penicillin allergy.",

                "usage": "750 mg once daily for 5 days (adults). Can be taken with or without food. Maintain hydration.",

                "side_effects": ["Tendon rupture/inflammation", "Nausea", "Diarrhea", "Dizziness", "Peripheral neuropathy", "QT prolongation"]

            },

            {

                "name": "Tamiflu",

                "generic_name": "Oseltamivir",

                "type": "Neuraminidase inhibitor (antiviral)",

                "description": "Antiviral medication for influenza-related pneumonia. Reduces symptom duration by 1–2 days and severity if started within 48 hours. Also used prophylactically during outbreaks.",

                "usage": "75 mg twice daily for 5 days (treatment). 75 mg once daily for 10 days (prophylaxis).",

                "side_effects": ["Nausea", "Vomiting", "Headache", "Neuropsychiatric events (rare, more common in children)"]

            },

            {

                "name": "Rocephin",

                "generic_name": "Ceftriaxone",

                "type": "Third-generation cephalosporin",

                "description": "Broad-spectrum IV antibiotic used for hospitalized pneumonia patients. Excellent coverage of common CAP pathogens. Often combined with azithromycin for comprehensive coverage.",

                "usage": "1–2 g IV once daily. Usually given in hospital setting for moderate-to-severe pneumonia.",

                "side_effects": ["Diarrhea", "Injection site pain", "Rash", "Biliary sludging", "Clostridium difficile infection"]

            },

            {

                "name": "Vibramycin",

                "generic_name": "Doxycycline",

                "type": "Tetracycline antibiotic",

                "description": "Alternative to macrolides for outpatient CAP treatment. Effective against typical and atypical organisms. Good option for patients unable to take macrolides or fluoroquinolones.",

                "usage": "100 mg twice daily for 5–7 days. Take with full glass of water; stay upright for 30 minutes after.",

                "side_effects": ["Photosensitivity", "GI upset", "Esophageal irritation", "Yeast infection", "Tooth discoloration (children <8)"]

            }

        ],

        "prevention": [

            {

                "tip": "Get pneumococcal vaccine",

                "description": "PCV15 followed by PPSV23, or PCV20 alone, is recommended for all adults ≥65, immunocompromised individuals, and those with chronic diseases. Prevents the most common bacterial cause.",

                "icon": ""

            },

            {

                "tip": "Annual influenza vaccination",

                "description": "Influenza is a common precursor to secondary bacterial pneumonia. Annual vaccination reduces pneumonia hospitalizations by 40–60% in high-risk groups.",

                "icon": ""

            },

            {

                "tip": "Practice good hand hygiene",

                "description": "Wash hands frequently with soap for ≥20 seconds, especially before eating and after coughing/sneezing. Use alcohol-based hand sanitizer (≥60%) when soap is unavailable.",

                "icon": ""

            },

            {

                "tip": "Don't smoke",

                "description": "Smoking destroys the cilia that line the airways and filter out germs, significantly increasing pneumonia risk. Quitting restores airway defenses over several months.",

                "icon": ""

            },

            {

                "tip": "Maintain a healthy immune system",

                "description": "Adequate sleep (7–9 hours), regular exercise, balanced nutrition, stress management, and moderate alcohol consumption all support robust immune function.",

                "icon": ""

            },

            {

                "tip": "Practice respiratory hygiene",

                "description": "Cover mouth and nose when coughing or sneezing with elbow or tissue. Dispose of tissues immediately. Avoid close contact with people who have respiratory infections.",

                "icon": ""

            }

        ],

        "when_to_see_doctor": [

            "Persistent high fever (>39°C/102.2°F) that doesn't respond to over-the-counter medications",

            "Difficulty breathing or rapid breathing (>24 breaths/min) at rest",

            "Chest pain that worsens with breathing or coughing",

            "Coughing up blood-streaked or rust-colored sputum",

            "Symptoms worsening after initial improvement (suggests secondary infection)",

            "Confusion or altered mental status (especially in elderly) — EMERGENCY",

            "Blue or grey discoloration of lips, fingernails, or skin (cyanosis) — CALL EMERGENCY SERVICES"

        ],

        "statistics": {

            "prevalence": "~450 million cases per year worldwide",

            "annual_deaths": "~2.5 million deaths per year globally — leading infectious cause of death in children under 5",

            "age_group": "Highest risk in children <5 years and adults >65 years. Mortality increases significantly with age.",

            "trend": "stable"

        },

        "references": [

            {

                "title": "Pneumonia Fact Sheet",

                "source": "World Health Organization",

                "url": "https://www.who.int/news-room/fact-sheets/detail/pneumonia"

            },

            {

                "title": "Pneumonia: Diagnosis and Treatment",

                "source": "American Thoracic Society / Infectious Diseases Society of America",

                "url": "https://www.thoracic.org/patients/patient-resources/resources/top-pneumonia-facts.pdf"

            },

            {

                "title": "Pneumonia - Symptoms and Causes",

                "source": "Mayo Clinic",

                "url": "https://www.mayoclinic.org/diseases-conditions/pneumonia/symptoms-causes/syc-20354204"

            },

            {

                "title": "Pneumonia",

                "source": "Centers for Disease Control and Prevention (CDC)",

                "url": "https://www.cdc.gov/pneumonia/"

            }

        ]

    },

}

def get_all_diseases() -> list[dict]:

    summaries = []

    for disease in DISEASES.values():

        summaries.append({

            "id": disease["id"],

            "name": disease["name"],

            "icon": disease["icon"],

            "color": disease["color"],

            "tagline": disease["tagline"],

            "key_stat": disease["key_stat"],

            "overview_short": disease["overview"].split("\n\n")[0],  

        })

    return summaries

def get_disease_detail(disease_id: str) -> dict | None:

    return DISEASES.get(disease_id.lower())

