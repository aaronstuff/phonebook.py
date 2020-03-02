class DbUpdate:
    contact = {}

	def add_new_contact(self, name, phone_no):
		self.contact[name] = phone_no

	def modify_contact(self, name, phone_no):
		self.contact[name] = phone_no


	def delete_contact(self, name):
		del self.contact[name]

	def search_by_name(self, name):
		if name in self.contact:
			return name, self.contact[name]
		else:
			return

	def find_all_contacts(self):
		return self.contact.items()
