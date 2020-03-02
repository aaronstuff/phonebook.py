from .DbUpdater import DbUpdate


class PhoneBook:
	db_update = DbUpdate()

	def add_contact(self, name, phone_no):
		search_result = self.search_contact(name)
		if len(search_result) != 0:
			return False
		self.db_update.add_new_contact(name, phone_no)
		return True

	def search_contact(self, name):
		search_result = self.db_update.search_by_name(name)
		if search_result != None:
			return [[search_result[0], search_result[1]]]
		else:
			return []

	def delete_contact(self, name):
		search_result = self.search_contact(name)
		if len(search_result) == 0:
			return False
		self.db_update.delete_contact(name)
		return True

	def update_contact(self, name, phone_no):
		search_result = self.search_contact(name)
		if len(search_result) == 0:
			return False
		self.db_update.modify_contact(name, phone_no)
		return True

	def all_contacts(self):
		return self.db_update.find_all_contacts()

