from locust import HttpUser, task, between
import random

class TractionUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task(4)
    def get_student_id(self):
        student_number = f"{random.randint(1, 1000):04d}"
        self.client.get(f"/sis/student-id?studentNumber={student_number}")

    @task(2)
    def download_transcript(self):
        transcript_id = f"{random.randint(1, 500)}"
        self.client.post("/api/transcripts/download", json={"transcriptId": transcript_id})

    @task(1)
    def approve_transcript(self):
        transcript_id = f"{random.randint(1, 500)}"
        self.client.put("/api/transcripts/approve", json={"transcriptId": transcript_id, "approver": "automated-test"})
