class Customer:
    def __init__(self, id, names, surnames, document_type, document_number, address, phone, email):
        self.id = id
        self.names = names
        self.surnames = surnames
        self.document_type = document_type
        self.document_number = document_number
        self.address = address
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "names": self.names,
            "surnames": self.surnames,
            "document_type": self.document_type,
            "document_number": self.document_number,
            "address": self.address,
            "phone": self.phone,
            "email": self.email
        }       