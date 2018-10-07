# trogan1
The first edition of the STAND Haiti patient tracking system

This project was created to aid the organization STAND: the Haiti Project in collecting information on patient
demographics, treatment, and care plans. STAND (www.standhaitiproject.com) provides orthopedic rehabilitation in 
Port-de-Paix, Haiti.

The STAND clinic is setup such that patients line up outside of the front entrance in the morning. STAND decides 
how many patients can be seen that day (usually 150-200) and hands a card with a number on it to each person seeking
treatment, so that the order in which patients showed up is preserved once they enter the waiting area. As patients 
are let into the waiting area with their numbered card, translators begin the intake process using adroid tablets. 
This involves entering the patient's card number, demographics and a chief complaint (why the patient needs treatment) 
into a Patient intake form. The person in charge of triaging can then see this information as it starts to be entered 
via various admin views on a laptop in the clinic. By looking at the patients' ages and chief complaints, a queue can
be created. Very old and very young patients are seen first, and patients with very severe or emergent cases are given
priority. Each care provider has a translator who comes to the triage desk, is told by the triager which patient to 
bring in, and then escorts the patient back to be seen. As the provider is treating the patient, she can collect a
number of pieces of structured data as well as free-text notes via an encounter form. This encounter data is stored
in a postgres database and can be seen via an admin view.

Trogan has three main components: 
  1.) Patient Intake
  2.) An Admin view used for Queuing and triaging of patients
  3.) Patient Encounter


Notes:
Intake: It is important that all users be logged into the "intake" username during the intake period. If a translator is signed in as a provider during intake, all of the patients that translator captures will be assigned to that provider's queue. 
  
