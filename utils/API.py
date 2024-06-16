from abc import abstractmethod
import json
import requests
import os

json_header = {
    'Content-Type': 'application/json'
}

class Employees:
    @abstractmethod
    def build_url(self, id=None):
        if not id:
            return f"{os.getenv('PETCARE_API_URL')}employees/?auth={os.getenv('PETCARE_AUTH_TOKEN')}"
        elif id:
            return f"{os.getenv('PETCARE_API_URL')}employees/{id}?auth={os.getenv('PETCARE_AUTH_TOKEN')}"
    
    @abstractmethod
    def get_all(self):
        return requests.get(
            url=self.build_url()
        )

    @abstractmethod    
    def get_one(self, id):
        return requests.get(
            url=self.build_url(id)
        )
    
    @abstractmethod    
    def validate(self, data):
        return requests.get(
            url=self.build_url(),
            headers=json_header,
            data=json.dumps(data)
        )

    @abstractmethod
    def save_one(self, data, files):            
        return requests.post(
            url=self.build_url(),
            data=data,
            files=files
        )
    
    @abstractmethod
    def update_one(self, id, new_data, new_files=None):
        return requests.patch(
            url=self.build_url(id),
            data=new_data,
            files=new_files
        )
    
    @abstractmethod
    def delete_one(self, id):
        return requests.delete(
            url=self.build_url(id)
        )

