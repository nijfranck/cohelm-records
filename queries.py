import json


EXTRACTIONS = [
    "Patient’s chief complaint",
    "Treatment plan the doctor is suggesting",
    "Treatment plan the doctor is suggesting"
    "A list of allergies the patient has",
    "A list of medications the patient is taking, with any known side-effects"
]

QUESTIONS = [
    "Does the patient have a family history of colon cancer in their first-degree relatives?",
    "Has the patient experienced minimal bright red blood per rectum?",
    "Has the patient had significant loss of blood?",
    "Does the patient have a history of skin problems?",
    "Has the patient used hydrocortisone cream for the haemorrhoids that they are currently experiencing?",
    "Were any high risk traits found on the patient’s genetic test?",
    "Has the patient had a colonoscopy in the last 5 years?",
    "Has the patient had any recent foreign travel?",
    "How long has the patient been known to healthcare services?"
]

def generate_medical_record_query(text):
    """Generate a query for the OpenAI API."""

    extraction_text = "\n".join(f"{i+1}. {e}" for i, e in enumerate(EXTRACTIONS)) 
    question_text = "\n".join(f"{i+1}. {q}" for i, q in enumerate(QUESTIONS))

    return f"""Here is the patient's medical record: \n{text} 
        Extract the following information: {extraction_text} \n 
        Think step by step for each extraction above, and you must: 
            1. Justify its reasoning, ie provide conclusive evidence for each answer 
            2. Provide a confidence score where 10/10 is very confident of its answer 
        Also, answer the following questions using the text: {question_text} \n
        Think step by step for each answer above, and you must: 
            1. Justify its reasoning, ie provide conclusive evidence for each answer 
            2. Provide a confidence score where 10/10 is very confident of its answer \n 
        Then, Finally, your application should suggest whether the treatment plan is appropriate.
        The metric and clinical accuracy does not need to be accurate  
        and can simply be a comparison of how many questions are answered as Yes vs No. \n. 
        """

class Medication:
    def __init__(self, name, side_effects):
        self.name = name
        self.side_effects = side_effects

class PatientInfo:
    def __init__(self, chief_complaint, treatment_plan, allergies, medications):
        self.chief_complaint = chief_complaint
        self.treatment_plan = treatment_plan
        self.allergies = allergies
        self.medications = medications

class QuestionAnswer:
    def __init__(self, question, answer, confidence, evidence):
        self.question = question
        self.answer = answer
        self.confidence = confidence
        self.evidence = evidence

class SuggestedTreatment:
    def __init__(self, accept_treatment_plan, confidence, reason):
        self.accept_treatment_plan = accept_treatment_plan
        self.confidence = confidence
        self.reason = reason

class Query:
    def __init__(self, patient_info, question_answers, suggested_treatment):
        self.patient_info = patient_info
        self.question_answers = question_answers
        self.suggested_treatment = suggested_treatment

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


def generate_json_query(text):
    """Generate a query for the OpenAI API."""

    return f"""Here is the patient's medical record reading: \n" + {text} \n
    Extract the following information and format the response as a JSON string:
    {json_block()}
    """

def json_block():
    medications = [Medication("<medication1>", ["<side effect1>", "<side effect2>"]), Medication("<medication2>", ["<side effect1>", "<side effect2>"])]
    patient_info = PatientInfo(chief_complaint="<chief complaint>", 
                               treatment_plan="<treatment plan>", 
                               allergies=["<allergy1>", "<allergy2>"], 
                               medications=medications)
    question_answers = [QuestionAnswer("<question1>", "<answer1>", "<confidence1>", "<evidence1>"), QuestionAnswer("<question2>", "<answer2>", "<confidence2>", "<evidence2>")]
    suggested_treatment = SuggestedTreatment("<Yes/No>", "<confidence>", "<reason>")
    query = Query(patient_info, question_answers, suggested_treatment)
    json_query = query.to_json()
    return json_query
