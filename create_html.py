import pandas as pd
import os

links = pd.read_csv("links.csv") 

names = ["Cangrelor During PCI",
"Clopidogrel plus Aspirin versus Aspirin Alone in High-Risk Patients",
"Colchicine in Patients with Recent Myocardial Infarction",
"Clopidogrel in Patients with Acute Coronary Syndromes",
"Eplerenone in Patients with Left Ventricular Dysfunction after Myocardial Infarction",
"Enoxaparin versus Unfractionated Heparin in Unstable Coronary Artery Disease",
"Mortality and Morbidity with Thrombolytic Regimens in Myocardial Infarction: The GUSTO Trial",
"Intraaortic Balloon Counterpulsation in Acute Myocardial Infarction-Complicated Cardiogenic Shock",
"Ezetimibe Added to Statin Therapy after Acute Coronary Syndromes",
"Prophylactic Implantation of a Defibrillator in Patients with Myocardial Infarction and Reduced Ejection Fraction",
"Fondaparinux versus Enoxaparin in Acute Coronary Syndromes (OASIS-5 Trial)",
"Percutaneous Coronary Intervention in Stable Patients with Occluded Infarct-Related Artery",
"Ticagrelor in Patients  to 3 Years after Myocardial Infarction",
"Rivaroxaban with or without Aspirin in Patients with Recent PCI and Atrial Fibrillation",
"Ticagrelor versus Clopidogrel in Patients with Acute Coronary Syndromes",
"Intensive Lipid Lowering with Atorvastatin in Patients with Stable Coronary Disease",
"Captopril in Patients with Left Ventricular Dysfunction After Myocardial Infarction",
"Early Revascularization in Acute Myocardial Infarction Complicated by Cardiogenic Shock",
"Early Versus Delayed Intervention in Acute Coronary Syndromes",
"Prasugrel versus Clopidogrel in Patients with Acute Coronary Syndromes",
"Aspirin in Unstable Angina Trial",
"Valsartan, Captopril, or Both in Myocardial Infarction Complicated by Heart Failure, Left Ventricular Dysfunction, or Both",
"Darbepoetin Alfa in Systolic Heart Failure and Anemia",
"Transcatheter versus Surgical Aortic-Valve Replacement in Intermediate-Risk Patients",
"TAVR versus Surgery for Aortic Stenosis in Patients at Low Surgical Risk",
"Transcatheter versus Surgical Aortic-Valve Replacement in High-Risk Patients",
"Transcatheter Aortic-Valve Implantation for Inoperable Severe Aortic Stenosis",
"TAVR versus Surgery in Patients with Intermediate-Risk Aortic Stenosis",
"Aspirin Use for the Primary Prevention of Cardiovascular Disease and Colorectal Cancer in the Elderly",
"Clopidogrel with Aspirin in High-Risk Patients with Atrial Fibrillation (ACTIVE A)",
"Management Strategies for Atrial Fibrillation",
"Apixaban versus Warfarin in Patients with Atrial Fibrillation",
"Antithrombotic Therapy in Patients with Atrial Fibrillation following Acute Coronary Syndrome or PCI", 
"Apixaban versus Aspirin in Patients with Atrial Fibrillation", 
"Bridging Anticoagulation in Patients with Atrial Fibrillation",
"Catheter Ablation for Atrial Fibrillation with Heart Failure", 
"Catheter Ablation vs. Antiarrhythmic Drug Therapy for Atrial Fibrillation",
"Early Rhythm-Control Therapy in Patients with Atrial Fibrillation",
"Atrial fibrillation detection after stroke",
"Edoxaban versus Warfarin in Patients with Atrial Fibrillation",
"Cryoballoon or Radiofrequency Ablation for Paroxysmal Atrial Fibrillation",
"Lenient vs Strict Rate Control in Patients with Atrial Fibrillation",
"Dabigatran versus Warfarin in Patients with Atrial Fibrillation",
"Rivaroxaban versus Warfarin in Nonvalvular Atrial Fibrillation",
"Biventricular Pacing in Patients with Atrioventricular Block and Heart Failure",
"Dual-Chamber versus Ventricular Pacing in Sinus-Node Dysfunction", 
"Vitamin D, Omega-3 Trial (VITAL)",
"Mild Therapeutic Hypothermia to Improve the Neurologic Outcome after Cardiac Arrest",
"Targeted Temperature Management at 33°C Versus 36°C after Cardiac Arrest",
"Hypothermia vs. Normothermia after Out-of-Hospital Cardiac Arrest",
"Coronary-Artery Revascularization before Elective Major Vascular Surgery (CARP Trial)",
"Aspirin in Patients Undergoing Noncardiac Surgery",
"Rosuvastatin and Cardiovascular Events in Patients Undergoing Hemodialysis", 
"Renal-Artery Stenting versus Medical Therapy for Atherosclerotic Renal-Artery Stenosis",
"Combined Effects of Lowering LDL Cholesterol and Blood Pressure on Cardiovascular Disease",
"Liraglutide and Cardiovascular Outcomes in Type 2 Diabetes",
"Intensive Lifestyle Intervention in Type 2 Diabetes", 
"Comparing Angiotensin Receptor Blockers and ACE Inhibitors for Patients with Vascular Disease or High-Risk Diabetes",
"N-3 Fatty Acids in High-Risk Patients with Dysglycemia",
"Carotid-Artery Stenting versus Endarterectomy in Asymptomatic Patients",
"Carotid Stenting vs. Endarterectomy Trial (CREST)", 
"Dapagliflozin in Patients with Chronic Kidney Disease",
"Fenofibrate and Simvastatin Not Beneficial in Reducing Cardiovascular Events in Patients with Type 2 Diabetes",
"Bioresorbable Vascular Scaffolds versus Metallic Stents in Routine PCI",
"Outcomes after Bilateral vs. Single Internal Thoracic Artery Grafting in Coronary-Artery Bypass Surgery",
"Intensive Medical Therapy for Type 2 Diabetes and Stable Ischemic Heart Disease",
"Comparison of Everolimus-Eluting Stents or Bypass Surgery for Multivessel Disease (BEST Trial)",
"Canakinumab Antiinflammatory Thrombosis Outcome Study (CANTOS)",
"Clopidogrel with or without Omeprazole in Coronary Artery Disease",
"FFR-Guided PCI in ST-Segment Elevation Myocardial Infarction",
"Rivaroxaban with or without Aspirin in Stable Cardiovascular Disease", 
"Percutaneous Coronary Intervention for Stable Coronary Artery Disease",
"Culprit Lesion Only PCI versus Multivessel PCI in Cardiogenic Shock (CULPRIT-SHOCK)",
"Dual Antiplatelet Therapy with Clopidogrel and Aspirin in Coronary Stenting",
"Percutaneous Coronary Intervention vs. Coronary Artery Bypass Grafting in Left Main Coronary Artery Disease",
"Fractional Flow Reserve-Guided PCI versus Angiography for Multivessel Evaluation (FAME) Study",
"Fractional Flow Reserve-Guided PCI for Stable Coronary Artery Disease",
"Evolocumab in Patients with Cardiovascular Disease",
"CABG vs. PCI in Diabetes with Multivessel Disease",
"Ramipril in High-Risk Patients",
"Extended-Release Niacin or Laropiprant and Vascular Outcomes",
"Instantaneous Wave-Free Ratio versus Fractional Flow Reserve in Patients with Stable Angina Pectoris or Acute Coronary Syndrome",
"Ticagrelor versus Prasugrel in Acute Coronary Syndromes",
"Invasive Strategy vs. Conservative Strategy in Stable Coronary Disease and Moderate or Severe Ischemia",
"Rosuvastatin to Prevent Vascular Events in Men and Women with Elevated C-Reactive Protein",
"Colchicine in Patients with Chronic Coronary Disease",
"Dual Antiplatelet Therapy Duration in High-Bleeding-Risk Patients After Stent Implantation",
"Bivalirudin versus Heparin in Acute Coronary Syndrome",
"Long-term Outcomes with Drug-Eluting Stents versus Bare-Metal Stents in Norway",
"Celecoxib vs. Ibuprofen or Naproxen in Patients with Increased Cardiovascular Risk",
"Mediterranean Diet for Primary Prevention of Cardiovascular Disease",
"Dual Antithrombotic Therapy with Dabigatran after PCI in Atrial Fibrillation", 
"Icosapent Ethyl for Elevated Triglyceride Levels",
"CABG in Patients with Heart Failure and Coronary Artery Disease",
"Comparative Efficacy of PCI with Drug-Eluting Stents vs. CABG in Three-Vessel or Left Main Coronary Artery Disease",
"Early Invasive vs. Conservative Strategy in Unstable Angina and Non-ST-Segment Elevation Myocardial Infarction",
"Mortality and Morbidity in Patients with Stable Coronary Heart Disease and LDL Cholesterol Levels",
"Pravastatin in the Primary Prevention of Coronary Events",
"Inflammation and risk of atherothrombosis: Methotrexate versus placebo",
"Extended Thromboprophylaxis with Rivaroxaban in Acutely Ill Medical Patients",
"Aspirin for Primary Prevention in Diabetes Mellitus",
"Canagliflozin in Patients with Type 2 Diabetes and Cardiovascular Disease", 
"Empagliflozin in High Cardiovascular Risk Patients with Type 2 Diabetes",
"Early Surgery versus Conventional Treatment for Infective Endocarditis",
"Iso-Dinitrate Plus Hydralazine in Black Patients with Heart Failure",
"Acetazolamide in Patients with Acute Decompensated Heart Failure with Volume Overload",
"Atrial Fibrillation and Congestive Heart Failure Treatment Strategies", 
"Tafamidis in Transthyretin Amyloid Cardiomyopathy",
"Comparison of Ultrafiltration and Pharmacologic Therapy in Acute Decompensated Heart Failure",
"Enalapril in Severe Congestive Heart Failure",
"Rosuvastatin in Older Patients with Systolic Heart Failure",
"Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction",
"Mortality and Morbidity with an Implantable Cardioverter–Defibrillator in Patients with Nonischemic Dilated Cardiomyopathy",
"Dapagliflozin in Heart Failure with Preserved Ejection Fraction (DELIVER)",
"Mortality and Hospitalization in Heart Failure Patients on Digoxin",
"Mortality and Morbidity in Patients Receiving Encainide, Flecainide, or Placebo",
"Transplantation Outcomes in Organ Recipients from Donors with HCV Viremia",
"Diuretic Strategies in Patients with Acute Decompensated Heart Failure", 
"Eplerenone in Patients with Systolic Heart Failure and Mild Symptoms",
"Iron Supplementation in Heart Failure with Reduced Ejection Fraction and Iron Deficiency",
"Comparison of Continuous-Flow and Pulsatile-Flow Left Ventricular Assist Devices in Advanced Heart Failure",
"Cardiac-Resynchronization Therapy for the Prevention of Heart-Failure Events",
"Clinical Outcomes in Advanced Heart Failure Patients with Centrifugal-Flow vs. Axial-Flow Pump",
"Nitrates in Patients with Heart Failure and Preserved Ejection Fraction (NEAT-HFpEF Trial)",
"LCZ696 versus Enalapril in Heart Failure",
"Sacubitril-Valsartan in Heart Failure with Preserved Ejection Fraction",
"Sacubitril–Valsartan vs. Enalapril in Acute Decompensated Heart Failure",
"Cardiac-Resynchronization Therapy in Heart Failure with QRS Complex",
"Spironolactone for Severe Heart Failure",
"Left Ventricular Assist Device as Destination Therapy in End-Stage Heart Failure",
"Implantable Cardioverter-Defibrillator in Patients with Congestive Heart Failure",
"Enalapril for Chronic Heart Failure with Reduced Ejection Fraction",
"Spironolactone for Heart Failure with Preserved Ejection Fraction (TOPCAT Study)",
"Vasodilator Therapy for Chronic Congestive Heart Failure", 
"Enalapril vs. Hydralazine-Isosorbide Dinitrate in the Treatment of Chronic Congestive Heart Failure",
"Valsartan in Heart Failure Patients Already Treated with ACE Inhibitors", 
"Andexanet Alfa for Reversing Anticoagulation from Factor Xa Inhibitors", 
"Alirocumab for Hypercholesterolemia in Statin-Treated Patients",
"Benazepril-Amlodipine or Benazepril-Hydrochlorothiazide in High-Risk Patients with Hypertension",
"Barbershop Interventions for Blood Pressure Reduction in Black Men",
"Dietary Approaches to Stop Hypertension (DASH) Study",
"Hypertension Treatment in the Very Elderly",
"Systolic Blood Pressure Intervention Trial (SPRINT)",
"Systolic Blood Pressure Intervention in Elderly Hypertensive Patients",
"Transcatheter Mitral-Valve Repair in Heart Failure Patients with Mitral Regurgitation",
"Hematocrit Targeting in Polycythemia Vera",
"Routine Oxygen Therapy in Suspected Acute Myocardial Infarction",
"Preventive Angioplasty in Acute Myocardial Infarction (PRAMI)",
"Closure or Medical Therapy for Cryptogenic Stroke with Patent Foramen Ovale",
"PFO Closure vs. Medical Therapy in Stroke Prevention",
"Colchicine for Acute Pericarditis (ICAP)", 
"Rivaroxaban in Peripheral Artery Disease after Revascularization (VOYAGER PAD Trial)",
"Ticagrelor versus Clopidogrel in Patients with Symptomatic Peripheral Artery Disease",
"Warfarin versus Aspirin for Symptomatic Intracranial Disease (WASID) Trial",
"Wearable Cardioverter-Defibrillator after Myocardial Infarction",
"Clinical Question",
"Dabigatran versus Warfarin in Patients with Mechanical Heart Valves",
"ICD in Patients with Nonischemic Systolic Heart Failure and the Risk of Sudden Cardiac Death",
"Electrophysiologically Guided Antiarrhythmic Therapy in Coronary Artery Disease Patients",
"Ventricular Tachycardia Ablation versus Escalation of Antiarrhythmic Drugs",
"Timing of Renal Replacement Therapy in Acute Kidney Injury",
"Intensity of Renal Support in Critically Ill Patients with Acute Kidney Injury",
"Renal-Replacement Therapy in Septic Shock with Acute Kidney Injury",
"Balanced Crystalloids versus Saline in Noncritically Ill Adults",
"Cisatracurium in Early Acute Respiratory Distress Syndrome",
"Ventilation with Lower Tidal Volumes as Compared with Traditional Tidal Volumes for Acute Lung Injury and the Acute Respiratory Distress Syndrome",
"Fluid Management Strategies in Acute Lung Injury",
"High-Frequency Oscillation in Early Acute Respiratory Distress Syndrome",
"Prone Positioning in Severe Acute Respiratory Distress Syndrome",
"Early Neuromuscular Blockade in the Acute Respiratory Distress Syndrome",
"Restrictive versus Liberal Transfusion Strategy in Critically Ill Patients",
"Transfusion Requirements in Septic Shock (TRISS) Trial",
"Catheter-Related Infections and Thrombosis in ICU Patients",
"Antipsychotic Medications for Delirium in the Intensive Care Unit",
"Saline versus Albumin Fluid Evaluation (SAFE) in ICU Patients",
"Balanced Crystalloids versus Saline in Critically Ill Adults",
"Weaning from Mechanical Ventilation: Predictive Indices", 
"Haloperidol for Delirium in Intensive Care Unit Patients",
"Dexmedetomidine for Sedation in Mechanically Ventilated ICU Patients (SPICE III)",
"Acetaminophen for Fever in Critically Ill Patients with Suspected Infection",
"Risk Factors for Gastrointestinal Bleeding in Critically Ill Patients",
"Hydrocortisone in Severe Community-Acquired Pneumonia",
"Tenecteplase in Normotensive Patients with Pulmonary Embolism",
"Daily Interruption of Sedative Infusions in Critically Ill Patients Undergoing Mechanical Ventilation",
"Hydrocortisone for Patients with Septic Shock on Mechanical Ventilation",
"Albumin Replacement in Patients with Severe Sepsis or Septic Shock",
"Corticosteroids in Septic Shock: The APROCCHSS Trial",
"Early Goal-Directed Therapy in the Treatment of Septic Shock",
"Corticosteroid Therapy of Septic Shock (CORTICUS)",
"Ventilation with Lower Tidal Volumes as Compared with Traditional Tidal Volumes for Acute Respiratory Distress Syndrome",
"Protocol-Based Care for Early Septic Shock",
"Protocolized Resuscitation in Early Septic Shock (ProMISe)",
"Drotrecogin Alfa (Activated) in Severe Sepsis",
"Drotrecogin Alfa (Activated) in Adults with Septic Shock",
"Early Goal-Directed Therapy in the Treatment of Severe Sepsis and Septic Shock",
"Mean Arterial Pressure Targets in Septic Shock",
"Dopamine and Norepinephrine in Shock",
"Vasopressin vs Norepinephrine in Septic Shock",
"Angiotensin II for the Treatment of Vasodilatory Shock",
"Fluid Boluses in African Children with Severe Infection",
"Combination Therapy in Patients with Diabetic Nephropathy",
"Intensive Glucose Control in Type 2 Diabetes",
"Semaglutide in Adults with Overweight or Obesity",
"Zoledronic Acid and Fracture Risk Reduction", 
"Corticosteroids in the Treatment of Severe Alcoholic Hepatitis",
"Steroids or Pentoxifylline for Alcoholic Hepatitis (STOPAH) Trial",
"Albumin Infusion in Patients with Cirrhosis and Spontaneous Bacterial Peritonitis",
"Early Use of TIPS in Patients with Cirrhosis and Variceal Bleeding",
"Fecal Microbiota Transplantation for Recurrent Clostridium difficile Infection",
"Fidaxomicin versus Vancomycin for Clostridium difficile Infection",
"Bezlotoxumab for Prevention of Recurrent Clostridium difficile Infection",
"Comparative Effectiveness of Colonoscopy vs Fecal Immunochemical Testing for Colorectal Cancer Screening",
"Infliximab, Azathioprine, or Combination for Crohns Disease",
"High-Dose Proton-Pump Inhibitor for Peptic Ulcer Hemorrhage",
"Restrictive versus Liberal Transfusion Strategy in Patients with Acute Upper Gastrointestinal Bleeding",
"Sofosbuvir–Ribavirin for Hepatitis C Genotype 2 or 3 in Patients without Treatment Options",
"Minimally Invasive Step-Up Approach Versus Open Necrosectomy in Necrotizing Pancreatitis",
"Contraceptive CHOICE Project and Its Impact on Teen Pregnancy",
"Hemoglobin Target in Chronic Kidney Disease", 
"Liberal or Restrictive Transfusion after Hip Fracture Surgery",
"Restrictive Red-Cell Transfusion Strategy in Cardiac Surgery",
"Ibrutinib–Rituximab or Chemoimmunotherapy for CLL",
"Imatinib versus Interferon Alfa plus Cytarabine in Newly Diagnosed Chronic-Phase Chronic Myeloid Leukemia", 
"Apixaban versus Conventional Therapy in Venous Thromboembolism",
"Extended Anticoagulation with Apixaban for Venous Thromboembolism",
"BRIXABAN for Acute Medical Illness",
"Pharmacomechanical Catheter-Directed Thrombolysis for Deep-Vein Thrombosis",
"Apixaban for Thromboprophylaxis in Cancer Patients",
"Apixaban for the Treatment of Venous Thromboembolism in Patients with Cancer",
"Thromboprophylaxis with Rivaroxaban in High-Risk Ambulatory Patients with Cancer",
"Dalteparin versus Oral Anticoagulant Therapy for the Prevention of Recurrence in Patients with Cancer and Venous Thromboembolism",
"Rivaroxaban for the Prevention of Venous Thromboembolism",
"Extended Thromboprophylaxis with Aspirin versus Rivaroxaban after Total Hip or Knee Arthroplasty",
"Edoxaban versus Dalteparin for Cancer-Associated Venous Thromboembolism",
"Extended Thromboprophylaxis with Rivaroxaban in Acutely Ill Medical Patients", 
"Efficacy of Vena Caval Filters in Preventing Pulmonary Embolism in Patients with Deep-Vein Thrombosis",
"Duration of Anticoagulation after Venous Thromboembolism", 
"Dabigatran versus Warfarin in the Treatment of Acute Venous Thromboembolism",
"Screening for Occult Cancer in Unprovoked Venous Thromboembolism",
"Aspirin for the Secondary Prevention of Venous Thromboembolism",
"Reversal of Anticoagulation",
"Idarucizumab for Dabigatran Reversal",
"ATRA plus Arsenic Trioxide for Acute Promyelocytic Leukemia",
"Ibrutinib for Previously Treated Waldenströms Macroglobulinemia",
"CAR T-Cell Therapy bb22 in Relapsed or Refractory Multiple Myeloma",
"Clinical Question",
"Eculizumab in Patients with Paroxysmal Nocturnal Hemoglobinuria",
"Rivaroxaban versus Standard Therapy for Pulmonary Embolism Treatment",
"Pulmonary Embolism Prevalence in Patients Hospitalized for Syncope",
"Multidetector Computed Tomographic Angiography in Diagnosis of Pulmonary Embolism",
"Voxelotor in Patients with Sickle Cell Disease (HOPE Trial)",
"Hydroxyurea for the Treatment of Sickle Cell Anemia",
"Crizanlizumab in Sickle Cell Disease",
"Prophylactic Platelet Transfusions in Hematologic Cancers",
"Aspirin for the Prevention of Recurrent Venous Thromboembolism",
"Remdesivir for the Treatment of Covid-9 — Final Report",
"Dexamethasone in Hospitalized Patients with Covid-9",
"Partial Oral versus Intravenous Antibiotic Treatment of Endocarditis",
"Antiretroviral Preexposure Prophylaxis for HIV Prevention in Men Who Have Sex with Men",
"Azidothymidine (AZT) in Patients with AIDS or Advanced AIDS-Related Complex",
"Antiretroviral Therapy for the Prevention of HIV- Transmission", 
"Immediate Antiretroviral Therapy in Early HIV Infection",
"Preexposure Prophylaxis with FTC-TDF for HIV Prevention in Men",
"Timing of Antiretroviral Therapy for HIV- Infection and Mortality",
"Antibiotic Therapy for Intraabdominal Infection after Adequate Source Control", 
"Dexamethasone in Adults with Bacterial Meningitis",
"Oral versus Intravenous Antibiotics for Bone and Joint Infection (OVIVA)",
"Intrapleural Use of Tissue Plasminogen Activator and DNase in Pleural Infection",
"Empirical Antibiotic Treatment Strategies for Community-Acquired Pneumonia",
"Rifapentine and Isoniazid for 3 Months versus Isoniazid for 9 Months",
"Stenting vs. Aggressive Medical Therapy for Intracranial Arterial Stenosis",
"Rituximab versus Cyclophosphamide in ANCA-Associated Vasculitis",
"Cinacalcet in Patients Undergoing Hemodialysis", 
"Benazepril in Patients with Advanced Chronic Renal Insufficiency",
"Dialysis Dose and the Effect of Membrane Flux in Maintenance Hemodialysis",
"Initiating Dialysis Early and Late (IDEAL) Study",
"Morbidity Effects of Hemodialysis Dose and Membrane Flux",
"Revascularization versus Medical Therapy for Renal-Artery Stenosis", 
"Daclizumab, Mycophenolate Mofetil, and Corticosteroids Combined with Low-Dose Tacrolimus, Cyclosporine, or Sirolimus in Renal Transplantation", 
"Carotid Endarterectomy for Moderate Stenosis",
"Intramuscular versus Intravenous Therapy for Prehospital Status Epilepticus",
"Treatment of Generalized Convulsive Status Epilepticus",
"Atorvastatin for Stroke Prevention",
"Decompressive Craniectomy in Diffuse Traumatic Brain Injury",
"Clopidogrel with Aspirin in High-Risk Patients with Acute Non-Disabling Cerebrovascular Events (CHANCE)",
"Thrombectomy 6 to 24 Hours after Stroke",
"Alteplase for Stroke 3 to 4.5 Hours after Onset", 
"Intraarterial Treatment for Acute Ischemic Stroke in the MR CLEAN Trial",
"Endovascular Therapy for Ischemic Stroke with Perfusion-Imaging Selection",
"Rivaroxaban versus Aspirin in Secondary Prevention of Stroke and Prevention of Systemic Embolism in Patients with Recent Embolic Stroke of Undetermined Source (NAVIGATE ESUS)",
"Clopidogrel and Aspirin in Acute Ischemic Stroke and High-Risk TIA",
"Comparison of Aspirin plus Extended-Release Dipyridamole versus Clopidogrel for Recurrent Stroke",
"Ticagrelor versus Aspirin in Acute Stroke or Transient Ischemic Attack",
"Clopidogrel with Aspirin in Acute Minor Stroke or Transient Ischemic Attack",
"Warfarin vs. Aspirin in Patients with Recurrent Ischemic Stroke",
"Periconceptional Multivitamin and Folic Acid Supplementation Prevents Neural Tube Defects",
"Trastuzumab Emtansine for HER2-Positive Advanced Breast Cancer",
"Trastuzumab for HER2-Positive Early Breast Cancer",
"Programmed Death  Blockade in Cancer Treatment",
"Palliative Care in Patients with Metastatic Non–Small-Cell Lung Cancer",
"Cisplatin-Based Adjuvant Chemotherapy in Patients with Completely Resected Non-Small-Cell Lung Cancer",
"Pembrolizumab versus Chemotherapy for PD-L–Positive Non–Small-Cell Lung Cancer",
"National Lung Screening Trial (NLST)", 
"Twice-Daily versus Once-Daily Thoracic Radiotherapy in Limited Small-Cell Lung Cancer Treated with Cisplatin and Etoposide",
"Vemurafenib versus Dacarbazine for Metastatic Melanoma with BRAF V600E Mutation",
"Nab-Paclitaxel plus Gemcitabine for Metastatic Pancreatic Cancer",
"FOLFIRINOX versus Gemcitabine for Metastatic Pancreatic Cancer",
"European Randomized Study of Screening for Prostate Cancer (ERSPC)",
"Finasteride in the Prevention of Prostate Cancer",
"Nephrectomy Plus Interferon Alfa-2b versus Interferon Alfa-2b Alone in Metastatic Renal-Cell Cancer",
"Bevacizumab and Ranibizumab for Neovascular Age-Related Macular Degeneration (AMD)",
"Epidural Glucocorticoids for Spinal Stenosis",
"Arthroscopic Partial Meniscectomy versus Physical Therapy in Patients with Degenerative Meniscus Tears",
"A Randomized, Placebo-Controlled Trial of Arthroscopy for Osteoarthritis of the Knee",
"Clinical Effectiveness of Colonoscopy Screening in Reducing Colorectal Cancer Risk",
"Cytisine versus Nicotine-Replacement Therapy for Smoking Cessation",
"Atypical Antipsychotic Drugs in Alzheimers Disease",
"Effect of Antidepressant Discontinuation vs. Maintenance on Relapse in Primary Care Patients",
"Effectiveness of Antipsychotic Drugs in Patients with Chronic Schizophrenia",
"As-needed Budesonide–Formoterol in Mild Asthma",
"Tiotropium in Asthma Poorly Controlled with Standard Combination Therapy", 
"Indacaterol–Glycopyrronium versus Salmeterol–Fluticasone for COPD",
"Mortality and Morbidity in Patients with Severe Emphysema Treated with Lung-Volume-Reduction Surgery or Medical Therapy", 
"Salmeterol and Fluticasone Propionate and Survival in Chronic Obstructive Pulmonary Disease",
"Tiotropium and Outcomes in Chronic Obstructive Pulmonary Disease",
"Inhaled Glucocorticoids in Triple Therapy for Severe COPD",
"Nintedanib for Idiopathic Pulmonary Fibrosis",
"Pirfenidone in Patients with Idiopathic Pulmonary Fibrosis",
"Rituximab versus Cyclophosphamide for ANCA-Associated Vasculitis"]
html = []
txt = []
num = []
l = len(names)
#l = 2
for i in range(0,l):
    names[i] = links["Acronym"][i+2] + " - " + names[i]
    num.append(i+2)
    txt.append("article" + str(i+2) + ".txt")
    html.append("\"article" + str(i+2) + ".html\"")

title = pd.DataFrame()
title['title'] = names
title['html'] = html
title['txt'] = txt
title['num'] = num
#title = title.drop([0, 1])
title = title.sort_values(by=['title'])
title = title.reset_index(drop=True)

index_html_template = """ <html>
    <head>
        <link rel="icon" href="favicon.png">
        <title>Journal2Wiki</title>
        <link rel="stylesheet" type="text/css" href="layout.css" />
    </head>

    <div class="header"><h2>Index of Articles</h2></div>

    <div class="sidenav">
        <a href="about.html">About</a>
        <a href="index.html">Index</a>
    </div>
    <div class="main">
        <ul>
        """
cur_let = ""
for entry_num in range(0, len(title)):
    i = title['num'][entry_num]
    acronym = links['Acronym'][i]
    wiki = links['wiki'][i]
    article = links['article'][i]

    letters = acronym[0].split()
    if cur_let != letters[0]:
        cur_let = letters[0]
        if cur_let.isalpha():
           index_html_template = index_html_template + """<h2 style="margin-bottom:0;">""" + cur_let + """</h2>"""
        index_html_template = index_html_template + """ <hr width="100%", align = "left", size="2">"""
        
        
    index_entry = """<li><a href=""" + title['html'][entry_num] +""">""" + title['title'][entry_num] + """</a></li>"""
    index_html_template = index_html_template + index_entry
    
    file_name = "text/article" + str(i) + ".txt"
    output = "article" + str(i) + ".html"

    file1 = open(file_name, 'r')
    count = 0

    chunks = []
    temp = []

    while True:
        count += 1

        line = file1.readline()

        if line == '\n':
            chunks.append(temp)
            temp = []
        else:
            temp.append(line)

        if not line:
            chunks.append(temp)
            break

    file1.close()

    f = open(output, 'w') 

    html_template = """<html>
        <head>
            <link rel="stylesheet" type="text/css" href="layout.css" />
        </head>
        <style> 
            .right { 
                margin-left: 160px;
            } 
        </style>
        
        <div class="sidenav">
            <a href="about.html">About</a>
            <a href="index.html">Index</a>
        </div>
    """ 
    html_template = html_template + """<div class="header"><h3>""" + acronym + """</h3></div>"""
    chunks[0]=["".join(chunks[0])]
    temp = chunks[0][0].split()

    index = 0
    for t in temp:
        if 'PubMed' in t:
            letters = list(t)
            remove = []
            for x in letters:
                if x == 'P':
                    temp = temp[0:index+1]
                    break
                else:
                    remove.append(x)
            if len(remove):
                temp[index] = "".join(remove)
        index += 1

    chunks[0][0] = " ".join(temp)
    html_template = html_template + """<p><span class="main">""" + chunks[0][0] + """ </span></p>"""
    html_template = html_template + """<p><span class="contents">
                                        Links to original sources:
                                        <a href=""" + wiki + """>Wiki Journal Post</a>
                                        <a href=""" + article + """>Full Journal Article</a>
                                        </span></p>"""
    
    sections = ["Clinical Question", "Criticisms", "Bottom Line", "Major Points", "Guidelines", "Design", "Population", "Interventions", "Outcomes", "Funding", "Further Reading"]
    
    
    for c in chunks[1:len(chunks) + 1]:
        if len(c)>0:
            is_section = "no"
            for s in sections:
                if s in c[0] and len(c[0]) <35 and c[0] !="1. Clinical Question\n" and c[0] != "1 Clinical Question\n" and c[0] != "1Clinical Question\n":
                    c[0] = s
                    label = """<h2><span class="labels">""" + c[0] + "</span></h2>"
                    line = """ <hr width="88.5%", align = "right", size="2">"""
                    text = c[1:len(c)+1]

                    body = """<p><span class="main">""" + "".join(text) + """ </span></p>"""
                    html_template = html_template + label + line + body
                    is_section = "yes"
            if is_section == "no":
                body = """<p><span class="main">""" + "".join(c) + """ </span></p>"""
                html_template = html_template + body

    html_template = html_template + """    	
        <div class="footer">Footer</div>
        </body>
        </html>"""

    f.write(html_template) 

    f.close()

index_html_template = index_html_template + """    
<ul>
                                                </div>
                                                </html>
                                                """
index_f = open('index.html', 'w') 
index_f.write(index_html_template)
index_f.close()
