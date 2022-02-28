from typing import List
from .day import Day

class Subject:
	def __init__(
		self,
		_id             : int,
		name            : str,
		group           : str,
		time_zones      : List[Day],
		professor1      : str,
		professor_email1: str,
		professor2      : str,
		professor_email2: str,
		**kwargs
	) -> None:
		self._id              = _id
		self.name             = name
		self.group            = group
		self.time_zones       = time_zones
		self.professor1       = professor1
		self.professor_email1 = professor_email1
		self.professor2       = professor2
		self.professor_email2 = professor_email2

	def __str__(self) -> str:
		params = ''
		for d in dir(self):
			if '__' not in d:
				if "time_zones" not in d:
					params += f"{d}: {getattr(self, d)}\n"
				else:
					for index, day in enumerate(getattr(self, d)):
						params += f"Day{index+1}: {str(day)}\n"

		print(params)
		return "Ready"
		